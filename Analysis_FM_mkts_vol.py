import pandas as pd
import numpy as np 
import datetime as dt
import matplotlib as plt



#change directory
Data = pd.read_excel('/Users/fergie/Documents/Whole_data.xlsx')
data = Data.set_index('Date')


log_returns = np.log(data / data.shift(1))


daily_std = log_returns.std()
daily_std


annualized_vol = daily_std * np.sqrt(252)
annualized_vol*100 #as a per cent      
      

#Plot the trailing volatility over time 
TRADING_DAYS = 100
volatility = log_returns.rolling(100).std()*np.sqrt(100)
volatility.plot()


'''
#plot the Sharpe ratio 
#Assumptions 1% over year 252 trading days 
Rf = 0.01/252
sharpe_ratio = (log_returns.rolling(window=TRADING_DAYS).mean() - Rf) * TRADING_DAYS/volatility
sharpe_ratio.plot().update_layout(template='simple_white')
'''