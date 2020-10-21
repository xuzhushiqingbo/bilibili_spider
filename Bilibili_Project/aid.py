import requests
import re

Av_list = []
for i in range(1, 7):
    url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=290526283&pagesize=30&tid=0&page="+str(i)+"&keyword=&order=pubdate"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',  # MAC OS Chrom
        'Upgrade-Insecure-Requests': '1',
        'Host': 'space.bilibili.com'
        }
    res = requests.get(url, headers)
    html_doc = res.content.decode("utf-8")
    av_compile = re.compile('"aid":(.*?),')
    av = re.findall(av_compile, html_doc)
    Av_list = Av_list + av

baconFile = open('aid.txt', 'w')
baconFile.write(str(Av_list))
baconFile.close()