# Author : Троцкий

# 2019-03-06 10:40


from pyecharts import WordCloud

import sql

name = ['无情铁手','宽油','王刚','宽水','劝退','宽饭','摊主']

value = sql.get_data()

worldcloud = WordCloud(width = 1300,height = 620)

worldcloud.add('',name,value,word_size_range = [20,100])

worldcloud.render()

