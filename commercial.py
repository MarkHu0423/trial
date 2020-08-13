from datetime import date
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取沪深A股历史K线数据 ####

rs = bs.query_history_k_data_plus("sh.600000",
    "date,time,code,open,high,low,close,volume,amount",
    start_date='2019-12-01', end_date='2019-12-05',
    frequency="15", adjustflag="3")
    # code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    # fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。详细指标列表见历史行情指标参数章节，日线与分钟线参数不同。此参数不可为空；
    # start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
    # end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
    # frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
    
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####   
result.to_csv("C:\\Users\\Mark Hu\\Desktop\\trial\\_A_stock_k_data.csv", index=False)
print(result)

#### 登出系统 ####
bs.logout()

import pandas as pd

df = pd.read_csv('_A_stock_k_data.csv')
# 查看数据
df.head()
df = df.dropna()

raw_time = pd.to_datetime(df.pop('time'), format='%Y/%m/%d %H:%M')

from matplotlib import pyplot as plt
import seaborn as sns

# 折线图：股票走势
plt.plot(raw_time, df['close'])
plt.xlabel('Time')
plt.ylabel('Share Price')
plt.title('Trend')
plt.show()