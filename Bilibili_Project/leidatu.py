# Author : Троцкий

# 2019-03-06 10:31


from pyecharts import Radar

import sql

radar = Radar("雷达图", "王刚弹幕关键词分布")

radar_data1 = [sql.get_data()]

schema = [
    ("无情铁手", 7000), ("宽油",7000), ("王刚", 7000),
    ("宽水", 7000), ("劝退", 7000), ("宽饭", 7000),
    ("摊主", 7000)
]

radar.config(schema)

radar.add("弹幕关键词出现次数",radar_data1)

radar.render()