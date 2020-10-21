# Author : Троцкий

# 2019-02-28 19：22


import requests

from lxml import etree

import re


def GET_ALL_Cid(av):

    # 获取包含弹幕url的json包里所需要的所有cid

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',  # Windows Opera
        'Upgrade-Insecure-Requests': '1',
        'Host': 'space.bilibili.com'
    }

    url = "http://api.bilibili.com/x/player/pagelist?aid="+av+"&jspon=jspon"

    res = requests.get(url,headers)
    html_doc = res.content.decode("utf-8")
    cid_compile = re.compile('"cid":(.*?),')
    cid = re.findall(cid_compile,html_doc)
    return cid[0]


def Keep_All_Dan(cid):

    # 直接求情弹幕的json文件并保存到mysql数据库

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',  # Ubuntu FireFox
        'Upgrade-Insecure-Requests': '1',
        'Host': 'space.bilibili.com'
    }
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+cid
    response = requests.get(url, headers)
    res = response.content
    html = etree.HTML(res)
    item = []
    item = html.xpath("//d/text()")
    for ii in item:
        print(ii)


if __name__ == '__main__':
    av = input("输入av号")
    cid = GET_ALL_Cid(av)
    Keep_All_Dan(cid)


