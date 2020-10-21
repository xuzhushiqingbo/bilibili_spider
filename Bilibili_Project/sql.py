# Author : Троцкий

# 2019-03-05 9:00


import pymysql


def get_data():

    db = pymysql.connect(user="", password="", port=3306, db="", host="127.0.0.1", charset="utf8")

    list_result = []

    sql_list = ["select count(*) from bilibili_comment WHERE COMMENT LIKE '%无情铁手%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%宽油%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%王刚%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%宽水%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%劝退%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%宽饭%'","select count(*) from bilibili_comment WHERE COMMENT LIKE '%摊主%'"]

    for sql in sql_list:

        cursor = db.cursor()

        cursor.execute(sql)

        # col = cursor.description

        result = cursor.fetchall()

        list_result += result[0]

    db.close()

    return list_result



