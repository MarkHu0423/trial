import tushare as ts
import pandas as pd
from matplotlib import pyplot as plt
# 初始化
token = 'bcb5da4959a0557b641b905164d3a952ac63812d992afc6e2aad0ba0'  
ts.set_token(token) 
pro = ts.pro_api()
# 选取了5只股票，从5月1号至8月1号的k线数据
df = pro.daily(ts_code='000005.SZ, 000006.SZ, 000007.SZ, 000009.SZ, 000010.SZ', start_date='20200501', end_date='20200801') 
# 将提取的数据按照股票代码分类，并将交易日期设为行索引
sz5 = df[::5].set_index('trade_date')
sz6 = df[1::5].set_index('trade_date')
sz7 = df[2::5].set_index('trade_date')
sz9 = df[3::5].set_index('trade_date')
sz10 = df[4::5].set_index('trade_date')
# 计算并绘制平均股价
mean_share_list = [sz5['close'].mean(), sz6['close'].mean(), sz7['close'].mean(), sz9['close'].mean(), sz10['close'].mean()] 
mean_share_series = pd.Series(mean_share_list, index=['000005', '000006', '000007', '000009', '000010'])
mean_share_series.plot(kind='bar')
plt.xticks
plt.show()