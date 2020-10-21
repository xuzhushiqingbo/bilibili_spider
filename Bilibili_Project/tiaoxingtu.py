# Author : Троцкий

# 2019-03-05 10:30


import numpy as np

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

import sql

font = FontProperties(fname=r"/Users/apple/PycharmProjects/Bilibili_Project/venv/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.ttf", size=14)

N = 7

y = sql.get_data()

x = np.arange(N)

p1 = plt.bar(x,y,color='red')

plt.title('B站UP主"美食作家王刚R"的关键词分布',fontproperties=font)

plt.xticks(range(0,7),['无情铁手','宽油','王刚','宽水','劝退','宽饭','摊主'],fontproperties=font)

plt.show()
