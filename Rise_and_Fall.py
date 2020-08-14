# 导入数据分析库pandas，官方文档https://pandas.pydata.org/docs/
import pandas as pd

# 从本地导入数据，这里用的是相对路径，如果你的程序和文件不在同一个文件夹里请用绝对路径
df = pd.read_csv('_A_stock_k_data.csv')
# 查看数据
df.head()
# 剔除缺失数据
df = df.dropna()
df.head()
# 取出时间
raw_time = pd.to_datetime(df.pop('date'), format='%Y/%m/%d')
from matplotlib import pyplot as plt
print(df)
daily_return = df['close'][0::5].pct_change().dropna()
plt.plot(raw_time[0::5][0:40], daily_return[0:40])
plt.xlabel('Time')
plt.ylabel('Rise and Fall')
plt.show()