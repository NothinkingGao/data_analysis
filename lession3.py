import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 打开csv文件,并读取数据
nba_player_data = "datas/nba.csv"
df = pd.read_csv(nba_player_data)


# 统计各个年龄段的球员数量
age_count = df.groupby("Age")["Weight"].count()
#print(type(age_count))


# 统计每个球队的平均年龄
age_count = df.groupby("Age")["Weight"].count()
age_weight_sum = df.groupby("Age")["Weight"].sum()

#print(age_weight_sum/age_count)

# 将体重切割成10份
weight_cut = pd.cut(df["Weight"], 10)
print(df["Weight"].groupby(weight_cut).count())


#print(df["Age"].groupby(weight_cut).count())

average_weight = df.groupby("Age")["Weight"].mean()
print(average_weight)

# 显示数据标签
for x, y in zip(average_weight.index, average_weight.values):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")


average_weight.plot(kind="line",marker="o",title="NBA球队平均体重",label="平均体重")
plt.grid(True)
plt.xlabel("年龄")
plt.ylabel("体重")
plt.show()