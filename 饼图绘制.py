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



# 按年龄切分为6份且为整数,并统计各个年龄段的球员数量
age_cut = pd.cut(df["Age"], 6,precision=0,labels=["20岁以下","20-25岁","25-30岁","30-35岁","35-40岁","40岁以上"])
print(age_cut)
age_count = df["Age"].groupby(age_cut).count()

# 绘制饼图
# autopct: 显示百分比
# explode: 突出显示某一部分
# shadow: 阴影
# startangle: 起始角度
# pctdistance: 百分比标签与圆心的距离
# labeldistance: 标签与圆心的距离
# radius: 半径
# counterclock: 逆时针
# wedgeprops: 饼图内外边界的属性
# title: 标题
# kind: 图形类型

age_count.plot(kind="pie",title="NBA球员年龄分布",autopct="%1.2f%%",explode=[0.1,0,0,0,0,0],radius=1.2)
plt.show()
