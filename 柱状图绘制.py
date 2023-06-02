# 饼图的绘制
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 打开csv文件,并读取数据
nba_player_data = "datas/nba.csv"
df = pd.read_csv(nba_player_data)
print(df.to_string())

# 统计每个球队的收入的平均值
team_mean = df.groupby("Team")["Salary"].mean()

# 收入排序
team_mean = team_mean.sort_values(ascending=False)


#绘制柱状图
team_mean.plot(kind="bar",title="NBA球队平均收入",rot=90)

for x,y in zip(range(len(team_mean.index)),team_mean.values):
    plt.text(x,y,f"{y:.2f}",ha="center",va="bottom")
plt.xlabel("球队")
plt.ylabel("平均收入")
plt.show()
