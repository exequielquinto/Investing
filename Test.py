import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2019,12,10)
end = dt.datetime(2019,12,31)
yesterday=dt.datetime(2019,12,20)
today = date.today()

df = web.DataReader('SPEM', 'yahoo', today, today)

#print(df.head())
#print(df.tail())

print (df)
print('test')
#print ((df)['Close'])
print(df['Close'].iloc[0])
print(df['Adj Close'].iloc[0])

df.to_csv('XAW.csv')

df = pd.read_csv('XAW.csv', parse_dates=True, index_col=0)
print('test2')
print (df)
x=((df)['Close'])
print (x)
print (list(df)[5])
print(df.Close.iloc[0])
print(df['Adj Close'].iloc[0])


#df['Close'].plot()
#df['Adj Close'].plot()
plt.show()