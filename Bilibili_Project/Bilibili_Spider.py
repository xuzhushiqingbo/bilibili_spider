# Author : Троцкий

# 2019-03-03 19：22


import requests

from lxml import etree

import re

import time

import pymysql

import random


def Get_All_Av():

    # 获取B站UP主美食作家王刚R所有投稿视频的aid

    Av_list = []
    for i in range(1,7):
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
        res = requests.get(url,headers)
        html_doc = res.content.decode("utf-8")
        av_compile = re.compile('"aid":(.*?),')
        av = re.findall(av_compile,html_doc)
        Av_list = Av_list + av
    return Av_list


def GET_ALL_Cid(Av_list):

    # 获取包含弹幕url的json包里所需要的所有cid

    Cid_list = []
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
    for i in Av_list:
        url = "http://api.bilibili.com/x/player/pagelist?aid="+i+"&jspon=jspon"
        time.sleep(random.randint(8, 16))   # 随机暂停，防止被判断成机器人
        res = requests.get(url,headers)
        html_doc = res.content.decode("utf-8")
        cid_compile = re.compile('"cid":(.*?),')
        cid = re.findall(cid_compile,html_doc)
        Cid_list = Cid_list + cid
    return Cid_list


def Keep_All_Dan(Cid_list):

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
    for i in Cid_list:
        url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+i
        time.sleep(random.randint(5, 25))  # 随机暂停，防止被判断成机器人
        response = requests.get(url, headers)
        res = response.content
        html = etree.HTML(res)
        item = []
        item = html.xpath("//d/text()")
        conn = pymysql.connect(user="root", password="root", port=3306, db="test", host="127.0.0.1", charset="utf8")
        cursor = conn.cursor()
        sql = "INSERT INTO bilibili_comment (comment) VALUES (%s)"
        for ii in item:
            try:
                cursor.execute(sql, (ii))
                conn.commit()
                print("插入成功  " + ii)
            except:
                pass
        conn.close()


if __name__ == '__main__':

    Av_list = []
    Cid_list = []
    Av_list = Get_All_Av()
    Cid_list = GET_ALL_Cid(Av_list)
    time.sleep(1800)    # 防止过于密集的请求
    Keep_All_Dan(Cid_list)
