from os import close
from numpy.lib.function_base import append
from numpy.lib.type_check import mintypecode
from numpy.lib.utils import safe_eval
import pandas as pd  # 数据处理
import datetime  # 时间格式处理
from matplotlib.pylab import date2num  # 时间格式处理
from matplotlib import pyplot as plt  # 绘图
from mplfinance.original_flavor import candlestick_ochl  # 绘制k线图
from matplotlib import ticker as mticker  # 刻度处理
from matplotlib import dates as mdates  # 时间格式处理

data = pd.read_csv('_A_stock_k_data.csv')
data = data.dropna().reset_index().drop(columns='index')
raw_time = data.pop('date')
Open = data.pop('open')
Close = data.pop('preclose')
High = data.pop('high')
Low = data.pop('low')


plot_mat = pd.DataFrame()
plot_mat['time'] = raw_time
plot_mat['open'] = Open
plot_mat['close'] = Close
plot_mat['high'] = High
plot_mat['low'] = Low
plot_mat.head()
