import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('_A_stock_k_data.csv')
plt.scatter(df['volume'], df['close'])
plt.xlabel('Volume')
plt.ylabel('Share Price')
plt.title('Volume & Share Price')
plt.show()