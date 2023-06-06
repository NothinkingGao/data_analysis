import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

print(f"the matplotlib path is {matplotlib.Path()}")
# 打开csv文件,并读取数据
nba_player_data = "datas/nba.csv"
df = pd.read_csv(nba_player_data)


# 计算平均年龄和体重的关系,把年龄划分为6个区间
age_cut = pd.cut(df["Age"], 6,precision=0)
average_age = df.groupby(age_cut)["Weight"].mean()
print(average_age)

# 绘制柱状图
average_age.plot(kind="bar",title="NBA球员平均年龄和体重的关系")
plt.xlabel("年龄")
plt.ylabel("体重")
plt.show()