import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# 建立坐标轴
plt.subplots(1,1)

# 绘制折线一
datas = pd.Series([1,2,3,4,5,6,7,8,9,10])
# plot各个参数的含义
# kind: 图形类型
# title: 图形标题
# color: 图形颜色
# label: 图形标签
# rot: x轴标签旋转角度
# fontsize: x轴标签字体大小
# figsize: 图形大小
# grid: 是否显示网格
# legend: 是否显示图例
# xlim: x轴范围
# ylim: y轴范围
# xticks: x轴刻度
# yticks: y轴刻度

datas.plot(kind="line",title="折线图",color="red")

# 绘制折线二
datas2 = pd.Series([10,9,8,7,6,5,4,3,2,1])
datas2.plot(kind="line",title="折线图")

plt.show()

