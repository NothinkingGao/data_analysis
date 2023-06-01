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
print(df.head(10).to_string())

print(df.describe().to_string())




# 统计每个球队的平均年龄
average_age = df.groupby("Team")["Age"].mean()
print(type(average_age))
print(average_age)
print(average_age.index)
print(average_age["Atlanta Hawks"])
average_age["Atlanta Hawks"] = 30.5

# 第二列数据保留两位小数
average_age = average_age.round(2)
# 正向排序
average_age = average_age.sort_values(ascending=True)
print(average_age)

# 修改average_age的索引
average_age.index = ["老鹰", "凯尔特人", "黄蜂", "公牛", "骑士", "小牛", "掘金", "活塞", "勇士", "火箭", "步行者", "快船", "湖人", "灰熊", "热火", "雄鹿", "森林狼", "篮网", "鹈鹕", "尼克斯", "雷霆", "魔术", "76人", "太阳", "开拓者", "国王", "马刺", "猛龙", "爵士", "奇才"]

# 设置列名
average_age.name = "平均年龄"
# 保存到csv文件
average_age.to_csv("datas/average_age.csv")

# 显示x轴全部标签
average_age.plot(kind="line",marker="1",title="NBA球队平均年龄")
plt.xlabel("球队")

# 设置x轴的刻度
plt.xticks(range(len(average_age.index)), average_age.index, rotation=90)


def on_mouse_move(event):
    if event.inaxes:
        x = event.xdata
        y = event.ydata
        print(f'x={x}, y={y}')

plt.connect('motion_notify_event', on_mouse_move)
# 保存图片,中文乱码
plt.savefig("datas/average_age.png", dpi=300, bbox_inches="tight")
plt.show()





