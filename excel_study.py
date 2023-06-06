import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 读取datas/average_age.xlsx文件
df = pd.read_excel("datas/average_age.xlsx")
df.head().to_string()

df.to_html("datas/average_age.html",encoding="utf-8")
df.to_json("datas/average_age.json")