import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                    '语文':[110,105,109],
                    '数学':[105,88,120],
                    '英语':[99,115,130]})

print(df)

# case1,语文和数学成绩加起来,并且显示在一列
# df['语文数学总分'] = df['语文'] + df['数学']
# print(df)
#
# # case2,语文成绩*2,并且显示在一列
# df['语文'] = df['语文'] * 2
# print(df)

# case3,添加一列,但是不赋值,默认为NaN
# df['体育'] = None
# print(df)

# 删除列
# axis=1 表示删除列,axis=0 表示删除行
# inplace=True 表示在原数据上进行修改
# df.drop(['语文'],axis=1,inplace=True)
# print(df)

# case4,语文和数学成绩比较,并且显示在一列
# df['语文数学比较'] = df['语文'] > df['数学']
# print(df)

# case5,汇总计算
# count() 统计每一列非空数据的个数
# sum() 统计每一列非空数据的和
# mean() 统计每一列非空数据的平均值
# max() 统计每一列非空数据的最大值
# min() 统计每一列非空数据的最小值
# axis=0 表示对列进行汇总计算,axis=1 表示对行进行汇总计算,默认为0
# median() 统计每一列非空数据的中位数
# mode() 统计每一列非空数据的众数
# std() 统计每一列非空数据的标准差
# var() 统计每一列非空数据的方差
# quantile() 统计每一列非空数据的分位数
print(df.count())
