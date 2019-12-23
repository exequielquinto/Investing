import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use('ggplot')

cash=15.48

today = date.today()
test_day = dt.datetime(2019,12,20)
day=test_day

stocks=('VCN.TO','XAW.TO','ZAG.TO')
shares=(119,293,517)

steps=np.arange(0,len(stocks))

results = pd.DataFrame()
temp = {}

for step in steps:
    df = web.DataReader(stocks[step], 'yahoo', day, day) #alternately you can use google or quandl
    #print (df)
    #print(df['Close'].iloc[0])
    temp['1_TICKER']=(stocks[step])
    #print (stocks[step])
    #print(df['Adj Close'].iloc[0])
    temp['2_Adj_Close']=df['Adj Close'].iloc[0]
    temp['3_Shares']=shares[step]
    #print((df['Adj Close'].iloc[0])*shares[step])
    temp['4_Mkt_Value']=(df['Adj Close'].iloc[0])*shares[step]
    results = results.append(temp, ignore_index=True)
    results.to_csv('Questrade_TFSA.csv')
df = pd.read_csv('Questrade_TFSA.csv', parse_dates=True, index_col=0)
Total_Equity = cash+df['4_Mkt_Value'].iloc[0]+df['4_Mkt_Value'].iloc[1]+df['4_Mkt_Value'].iloc[2]
print (Total_Equity)
print ((df['4_Mkt_Value'].iloc[0])*100/Total_Equity)
print ((df['4_Mkt_Value'].iloc[1])*100/Total_Equity)
print ((df['4_Mkt_Value'].iloc[2])*100/Total_Equity)