import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

# 构造数据

label = ["节点0", "节点1", "节点2", "节点3", "节点4", "节点5"]
# source和target是label中对应元素的索引值，python列表从0开始
source = [1, 0, 0, 0, 0, 0]  # 可以看做父级节点
target = [2, 3, 5, 4, 1, 4]  # 子级节点
value = [9, 3, 6, 2, 7, 8]   # value是连接source和target之间的值
 
# 生成绘图需要的字典数据
link = dict(source = source, target = target, value = value)
node = dict(label = label, pad=200, thickness=20)  # 节点数据，间隔和厚度设置

# 添加绘图数据
data = go.Sankey(link = link, node=node)

# 绘图并显示
fig = go.Figure(data)
fig.show()