import os

import pandas as pd
# 财报路径
from matplotlib import pyplot as plt, ticker

bar_colors = {
    "2020": "r",
    "2021": "g",
    "2022": "b",
    "2023": "y"
}

# 绘制小图
def create_kline_subplots(df):
    # 同比增长图片目录
    image_dir = "images/klines"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    collumns = list()
    with open("datas/collumns.txt", "r") as f:
        for line in f.readlines():
            collumns.append(line.strip())
    df = df[df["S&P Capital IQ - Standard"].isin(collumns)]
    for index in range(len(df)):
        row = df.iloc[index]
        title = row[0]
        row = row[1:]
        row.plot(kind="line", marker="o", title=title,rot=90,figsize=(8,4),fontsize=8)
        # 添加数据标签
        for x, y in zip(range(len(row.index)), row.values):
            plt.text(x,y,f"{y:.2f}",ha="center",va="bottom")

        # 显示横向网格线
        plt.grid(axis="y", linestyle="--", color="gray", alpha=0.5)
        # 网格线位于柱状图的后面,需要将网格线放到柱状图之后
        plt.gca().set_axisbelow(True)

        # 设置x轴刻度
        # rotation: 刻度标签旋转角度,默认为0
        plt.xticks(range(len(row.index)),row.index,rotation=45,fontsize=8,ha="right")

        plt.savefig(f"images/klines/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()
        print(f"生成图片: {title.replace('/','_')}.png")




def create_bar_subplots(df):
    ''' 绘制柱状图'''
    # 同比增长图片目录
    image_dir = "images/bars"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

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
        row.plot(kind="bar",title=title,rot=90,figsize=(8,4),width=0.3,fontsize=8)
        # 根据x轴的标签选择不同的颜色
        for x in range(len(row.index)):
            for year,color in bar_colors.items():
                if row.index[x].find(year) != -1:
                    plt.gca().get_children()[x].set_color(color)
                    break
        # 添加数据标签
        for x, y in zip(range(len(row.index)), row.values):
            plt.text(x,y,f"{y:.2f}",ha="center",va="bottom",size=8)

        # 显示横向网格线
        plt.grid(axis="y", linestyle="--", color="gray", alpha=0.5)
        # 网格线位于柱状图的后面,需要将网格线放到柱状图之后
        plt.gca().set_axisbelow(True)

        plt.savefig(f"images/bars/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()
        print(f"生成图片: {title.replace('/','_')}.png")


def yoy_growth(df):
    '''
        绘制同比增长率
    '''
    # 同比增长图片目录
    image_dir = "images/bars_yoy"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

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

        # 采用横向柱状图
        # plt.barh是横向柱状图,需要将x轴和y轴的数据对调,即y轴的数据为索引,而x轴的数据为值
        plt.figure(figsize=(8, 4))
        plt.barh(range(len(yoy.index)),yoy.values,align="center",alpha=0.8)
        # 设置长宽比为16:9

        plt.title(title,fontsize=8)
        # 设置y轴刻度
        plt.yticks(range(len(yoy.index)),yoy_indexs,fontsize=8)
        # 设置x轴刻度
        plt.xticks(fontsize=8)

        # 添加数据标签
        for x, y in zip(range(len(yoy.index)), yoy.values):
            plt.text(y+0.02,x,f"{round(y*100,2)}%",ha="left",va="center",size=8)

        # 根据y轴的标签选择不同的颜色
        for y in range(len(yoy.index)):
            for year,color in bar_colors.items():
                if yoy_indexs[y].find(year) != -1:
                    plt.gca().get_children()[y].set_color(color)
                    break




        # 生成柱形图,设置长宽比为16:9
        # width=0.8,设置柱形图的宽度
        # figsize=(16,9),设置图片的长宽比
        # fontsize=6,设置字体大小
        #yoy.plot(kind="bar",title=title,rot=0,figsize=(16,9),width=0.5,fontsize=8)
        # 采用横向图形,需要将x轴和y轴的数据对调



        # 根据x轴的标签选择不同的颜色
        # for x in range(len(row.index)):
        #     for year,color in bar_colors.items():
        #         if row.index[x].find(year) != -1:
        #             plt.gca().get_children()[x].set_color(color)
        #             break


        #print(yoy.values)
        # for x, y in zip(range(len(yoy.index)), yoy.values):
        #     plt.text(x,y+0.01,f"{round(y*100,2)}%",ha="center",va="bottom",size=8)

        # 添加X轴刻度,并旋转45度,旋转中心位于刻度的中间
        # ha是水平对齐方式,va是垂直对齐方式
        print(len(yoy.index))
        #plt.xticks(range(len(yoy.index)),yoy_indexs,rotation=45,ha="right")

        # 添加y轴坐标
        plt.xlabel("YoY Growth Rate")

        # 显示横向网格线
        plt.grid(axis="x", linestyle="--", color="gray", alpha=0.5)
        # 网格线位于柱状图的后面,需要将网格线放到柱状图之后
        plt.gca().set_axisbelow(True)


        # 将x轴的坐标数据变成百分比
        plt.gca().xaxis.set_major_formatter(lambda x, _: '{:.0%}'.format(x))

        #plt.gca().yaxis.set_major_formatter(lambda y, _: '{:.0%}'.format(y))



        plt.savefig(f"{image_dir}/{title.replace('/','_')}.png",dpi=300, bbox_inches="tight")
        plt.close()

        print(f"生成图片: {title.replace('/','_')}.png")
        #break




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

if __name__ == "__main__":
    finacy_report_path = "datas/DeutscheTelekomAGXTRADTE_Report_06-01-2023 的副本.xls"
    # 读取Financial Highlights这一页的数据
    df = pd.read_excel(finacy_report_path, sheet_name="Financial Highlights", skiprows=12)
    # 生成折线图
    create_kline_subplots(df)
    # 生成柱状图
    #create_bar_subplots(df)
    # 生成同比增长率
    #yoy_growth(df)