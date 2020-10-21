import requests
import re
import time
import random

baconFile = open('aid.txt', 'r')
Av_list = baconFile.read().split('[')[1].split(']')[0].split(',')
baconFile.close()
Cid_list = []
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    # Windows Opera
    'Upgrade-Insecure-Requests': '1',
    'Host': 'space.bilibili.com'
}
for i in Av_list:
    url = "http://api.bilibili.com/x/player/pagelist?aid=" + i.split("'")[1] + "&jspon=jspon"
    print(i.split("'")[1])
    time.sleep(random.randint(0, 2))  # 随机暂停，防止被判断成机器人
    res = requests.get(url, headers)
    html_doc = res.content.decode("utf-8")
    cid_compile = re.compile('"cid":(.*?),')
    cid = re.findall(cid_compile, html_doc)
    Cid_list = Cid_list + cid

baconFile = open('cid.txt', 'w')
baconFile.write(str(Cid_list))
baconFile.close()