# 饼图的绘制
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
# df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
#                     '语文':[110,105,109],
#                     '数学':[105,88,120],
#                     '英语':[99,115,130]})
#
# print(df1)
#
# df2 = pd.DataFrame({'编号':['mr002','mr001','mr003','mr004'],
#                     '体育':[34.5,39.7,38,45]})
#
# print(df2)
# df_merge=pd.merge(df1,df2,on='编号')
# print(df_merge)

# case 2
# 关键键'编号01' 和 '编号02' 不同,但是数据相同,如何合并?
# df1 = pd.DataFrame({'编号01':['mr001','mr002','mr003'],
#                     '语文':[110,105,109],
#                     '数学':[105,88,120],
#                     '英语':[99,115,130]})
# print(df1)
# df2 = pd.DataFrame({'编号02':['mr002','mr001','mr003','mr004'],
#                     '体育':[34.5,39.7,38,45]})
# print(df2)
# df_merge=pd.merge(df1,df2,)
# print(df_merge)


# case 3
# 采用left_index=True,right_index=True 两个参数,可以实现两个DataFrame的索引合并
# QA:DataFrame的第一列是索引吗?

# df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
#                     '语文':[110,105,109],
#                     '数学':[105,88,120],
#                     '英语':[99,115,130]})
# print(f"df1's index is: ")
# for item in df1.index:
#     print(item)
#
# print(df1)
# df2 = pd.DataFrame({'编号':['mr002','mr001','mr003','mr004'],
#                     '体育':[34.5,39.7,38,45]})
# print(df2)
# df_merge=pd.merge(df1,df2,how='outer',left_index=True,right_index=True)
# print(df_merge)


# case 4
# import pandas as pd
# #解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
#
# # df1记录的是每个学生的信息
# df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
#                     '学生姓名':['明日同学','高猿员','钱多多']})
# print(df1)
# df2 = pd.DataFrame({'编号':['mr001','mr001','mr003'],
#                     '语文':[110,105,109],
#                     '数学':[105,88,120],
#                     '英语':[99,115,130],
#                     '时间':['1月','2月','1月']})
# print(df2)
# df_merge=pd.merge(df1,df2,on='编号')
# print(df_merge)

import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.DataFrame({'编号':['mr001','mr002','mr003','mr001','mr001'],
                    '体育':[34.5,39.7,38,33,35]})
print(df1)
df2 = pd.DataFrame({'编号':['mr001','mr001','mr003','mr003','mr003'],
                    '语文':[110,105,109,110,108],
                    '数学':[105,88,120,123,119],
                    '英语':[99,115,130,109,128]})
print(df2)
df_merge=pd.merge(df1,df2,on='编号')
print(df_merge)
