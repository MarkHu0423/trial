import pandas as pd

import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

# 获得多条股票的数据，进行数据可视化分析
import tushare as ts

token = 'b040357522d745da48a561d627b0b977ee49b471c60e916f3cb9d4be'  # 通过注册获得的token，输入代码中用于获得股票数据
ts.set_token(token)  # 进行初始化

pro = ts.pro_api()

df = pro.daily(ts_code='000005.SZ, 000006.SZ, 000007.SZ, 000009.SZ, 000010.SZ', start_date='20200501', end_date='20200801') # 选取2020年5月1日到2020年8月1日的5支股票进行数据可视化处理
df.head(10)
print(df.head(10))


# 把时间和序号混杂在一起的股票数据分开，以便于画图
sz5 = df[::5].set_index('trade_date')
sz6 = df[1::5].set_index('trade_date')
sz7 = df[2::5].set_index('trade_date')
sz9 = df[3::5].set_index('trade_date')
sz10 = df[4::5].set_index('trade_date')

sz5.head()

# 绘制多条股票数据的折线对比图
fig, ax = plt.subplots()

sz5.plot(ax=ax, y='close', label='000005')
sz6.plot(ax=ax, y='close', label='000006')
sz7.plot(ax=ax, y='close', label='000007')
sz9.plot(ax=ax, y='close', label='000009')
sz10.plot(ax=ax, y='close', label='000010')

plt.legend(loc='upper left')
plt.show()

# 绘制多条股票数据的箱形图
closedf = pd.DataFrame()
closedf = pd.concat([closedf, sz5['close'], sz6['close'], sz7['close'], sz9['close'], sz10['close']], axis=1)  # 横向拼接数据(axis=1)
closedf.columns = ['000005', '000006', '000007', '000009', '000010']
closedf.plot(kind='box')
plt.show()

# 000007、000009、000010的箱形图出现了几个“O”，这表示这3支股票中存在温和的异常值，于是使用describe()方法对这3组数据的均值、分位数、标准差、最值等进行异常数据初步分析
print(sz7.describe())  
print(sz9.describe())
print(sz10.describe())
