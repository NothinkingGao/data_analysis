import pandas as pd
# 财报路径
from matplotlib import pyplot as plt, ticker

bar_colors = {
    "2020": "r",
    "2021": "g",
    "2022": "b",
    "2023": "y"
}

finacy_report_path = "datas/DeutscheTelekomAGXTRADTE_Report_06-01-2023 的副本.xls"

df = pd.read_excel(finacy_report_path,sheet_name="Financial Highlights",skiprows=12)

# 绘制小图
def create_kline_subplots(df):
    collumns = list()
    with open("datas/collumns.txt", "r") as f:
        for line in f.readlines():
            collumns.append(line.strip())
    df = df[df["S&P Capital IQ - Standard"].isin(collumns)]
    for index in range(len(df)):
        row = df.iloc[index]
        title = row[0]
        row = row[1:]
        row.plot(kind="line", marker="o", title=title)
        # 添加数据标签
        for x, y in zip(range(len(row.index)), row.values):
            plt.text(x,y,f"{y:.2f}",ha="center",va="bottom")

        plt.savefig(f"images/klines/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()



def create_bar_subplots(df):
    ''' 绘制柱状图'''
    collumns = list()
    with open("datas/collumns.txt", "r") as f:
        for line in f.readlines():
            collumns.append(line.strip())
    df = df[df["S&P Capital IQ - Standard"].isin(collumns)]

    for index in range(len(df)):
        row = df.iloc[index]
        title = row[0]
        row = row[1:]
        # 生成柱形图
        row.plot(kind="bar",title=title,rot=90)
        # 根据x轴的标签选择不同的颜色
        for x in range(len(row.index)):
            for year,color in bar_colors.items():
                if row.index[x].find(year) != -1:
                    plt.gca().get_children()[x].set_color(color)
                    break
        # 添加数据标签
        for x, y in zip(range(len(row.index)), row.values):
            plt.text(x,y,f"{y:.2f}",ha="center",va="bottom",size=8)

        plt.savefig(f"images/bars/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()

def yoy_growth(df):
    '''
        绘制同比增长率
    '''
    rows = ["Total Assets","Total Debt","Total Equity","Total Revenue","Net Income"]
    df = df[df["S&P Capital IQ - Standard"].isin(rows)]

    for index in range(len(df)):
        row = df.iloc[index]
        title = row[0]
        row = row[1:]
        # 计算同比增长率,保留4位小数,移除NaN数据
        yoy = row.pct_change(4).dropna()

        # 创建新的索引2020-2023的Q1,Q2,Q3,Q4
        # create data like:2021Q1-2022Q1,2021Q2-2022Q2,2021Q3-2022Q3,2021Q4-2022Q4
        yoy_indexs = list()
        for year in range(2020,2023):
            for quarter in range(1,5):
                yoy_indexs.append(f"{year}Q{quarter}-{year+1}Q{quarter}")
        print(yoy_indexs)

        yoy_indexs = yoy_indexs[:len(yoy.index)]

        # 增加横向网格线,设置成背景,放到柱状图之后
        plt.grid(axis="y", linestyle="--", color="gray", alpha=0.5)


        # 生成柱形图
        yoy.plot(kind="bar",title=title)

        # 根据x轴的标签选择不同的颜色
        for x in range(len(row.index)):
            for year,color in bar_colors.items():
                if row.index[x].find(year) != -1:
                    plt.gca().get_children()[x].set_color(color)
                    break


        #print(yoy.values)
        for x, y in zip(range(len(yoy.index)), yoy.values):
            plt.text(x,y+0.01,f"{round(y*100,2)}%",ha="center",va="bottom",size=8)

        # 添加X轴刻度
        print(len(yoy.index))
        plt.xticks(range(len(yoy.index)),yoy_indexs)

        # 添加y轴坐标
        plt.ylabel("YoY Growth Rate")

        # 分3列绘制yoy_indexs到图下边
        #plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(3))

        # 将y轴的坐标数据变成百分比
        plt.gca().yaxis.set_major_formatter(lambda y, _: '{:.0%}'.format(y))

        plt.savefig(f"images/bars_yoy/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()

#create_kline_subplots()
#create_bar_subplots()
yoy_growth(df)


# 定义28个子图
def create_big_subplots():
    '''
        将28个子图绘制在一张大图上
    '''
    fig,ax = plt.subplots(7,4,figsize=(50,50))

    for index in range(len(df)):
        row = df.iloc[index]
        # 在每一个子图上绘制折线图
        title = row[0]
        row = row[1:]
        row_number = index//4
        collumn_number = index%4
        try:
            row.plot(kind="line",ax=ax[row_number][collumn_number],marker="o",title=title)
            # 生成柱形图
            row.plot(kind="bar",ax=ax[row_number][collumn_number],title=title)
            # 添加数据标签
            for x,y in zip(range(len(row.index)),row.values):
                y = round(y,2)
                ax[row_number][collumn_number].annotate(f"{y}",xy=(x,y),xytext=(x,y+0.5))

        except Exception as e:
            print(e)

    plt.savefig("datas/financy_report.png")
