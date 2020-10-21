# Author : Троцкий

# 2019-03-05 9:22


import numpy as np

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

import sql

font = FontProperties(fname=r"/Users/apple/PycharmProjects/Bilibili_Project/venv/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.ttf", size=14)

fraces = sql.get_data()

plt.boxplot(fraces,whis=1.5)

plt.title('B站UP主"美食作家王刚R"的关键词分布',fontproperties=font)

plt.show()