
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# 建立坐标轴
# subplots各个参数的含义
# nrows: 行数
# ncols: 列数
# sharex: 是否共享x轴
# sharey: 是否共享y轴
# figsize: 图形大小
# subplot_kw: 创建各个子图时的关键字参数
# gridspec_kw: 创建各个子图时的关键字参数
# **fig_kw: 创建figure时的关键字参数

# 2行3列,共6个子图
# fig代表整个图形
# ax代表子图列表
fig, ax1 = plt.subplots(1,2,figsize=(10,5))

# 在第一个子图中绘制柱状图
datas = pd.Series([1,2,3,4,5,6,7,8,9,10])
datas.plot(kind="bar",ax=ax1[0],title="柱状图")

# 第二个图中绘制饼图
datas.plot(kind="pie",ax=ax1[1],title="饼图",autopct="%1.2f%%",explode=[0.1,0,0,0,0,0,0,0,0,0],radius=1.2)
plt.show()

