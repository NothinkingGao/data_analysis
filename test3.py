import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

# 创建图表和第一个y轴
fig, ax1 = plt.subplots()

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 第一个y轴数据
data_y1 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

# 第二个y轴数据，随机生成
data_y2 = np.random.randint(1, 10, 10)

# 绘制第一条折线
line1 = ax1.plot(x, data_y1, color="red", label="折线一")

# 在第一条折线的每个数据点上添加数据标签
for x1, y1 in zip(x, data_y1):
    ax1.text(x1, y1 + 10, y1, ha="center", va="bottom", fontsize=10)

# 设置第一个y轴的标签
ax1.set_ylabel("折线一")

# 设置图例
ax1.legend(loc="upper left")

# 创建第二个y轴
ax2 = ax1.twinx()

# 绘制第二条折线
line2 = ax2.plot(x, data_y2, color="blue", label="折线二")

# 在第二条折线的每个数据点上添加数据标签
for x2, y2 in zip(x, data_y2):
    ax2.text(x2, y2 + 10, y2, ha="center", va="top", fontsize=10)

# 设置第二个y轴的标签
ax2.set_ylabel("折线二")

# 设置第二个y轴的图例
ax2.legend(loc="upper right")

plt.show()
