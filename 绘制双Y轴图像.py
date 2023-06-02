import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 建立坐标轴
plt.subplots(1,1)

x = np.array([1,2,3,4,5,6,7,8,9,10])

# 特别大的Y轴数据
data_y1 = np.array([100,200,300,400,500,600,700,800,900,1000])

# 特别小的Y轴数据,随机生成
# randint参数的含义是
# low: 最小值,包含,默认是0
# high: 最大值,不包含
# size: 生成的随机数的个数
data_y2 = np.random.randint(1,10,10)


# 绘制折线一
plt.plot(x,data_y1,color="red",label="折线一")

for x1,y1 in zip(x,data_y1):
    plt.text(x1,y1+10,y1,ha="center",va="bottom",fontsize=10)
# 设置Y轴标签
plt.ylabel("折线一")



# 设置图例
# loc: 图例位置
# loc的取值是什么意思
# upper right: 右上角
# upper left: 左上角
# lower left: 左下角
# lower right: 右下角
# right: 右边
# center left: 左中
# center right: 右中
# lower center: 下中
# upper center: 上中
# center: 中间
plt.legend(loc="upper left")


# 设置第二个Y轴
# twinx函数的作用是将两个Y轴绑定在一起,这样两个Y轴的刻度就是一样的
# twinx函数的参数是一个Axes对象,这个Axes对象是第一个Y轴的Axes对象,也就是ax1,所以第二个Y轴的刻度和第一个Y轴的刻度是一样的
plt.twinx()

# QA:双y轴如何显示第二条折线的数据标签
# A:使用plt.text函数,在for循环中绘制数据标签,



# 此时plt的axes对象是第二个Y轴的axes对象,获取第二个Y轴的axes对象
print(plt.gca())


# 绘制折线二
plt.plot(x,data_y2,color="blue",label="折线二")

# 绘制折线二的数据标签
for x2,y2 in zip(x,data_y2):
    plt.text(x2,y2+10,y2,ha="center",va="bottom",fontsize=10)


# 设置Y轴标签
plt.ylabel("折线二")
plt.legend(loc="upper right")

plt.show()
