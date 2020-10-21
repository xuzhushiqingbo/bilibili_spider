# Author : Троцкий

# 2019-03-06 10:31


from pyecharts import Pie

import sql

attr = ['无情铁手', '宽油', '王刚', '宽水', '劝退', '宽饭', '摊主']

v1 = sql.get_data()

pie = Pie('关键词分布')

pie.add('', attr, v1, is_label_show=True)

pie.render()
