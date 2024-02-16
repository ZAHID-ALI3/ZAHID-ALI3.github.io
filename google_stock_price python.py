# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:13:20 2023

@author: aaa
"""
import plotly.express as px
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
gsp=pd.read_csv("C:\\Users\\aaa\\Downloads\\GOOGLE.csv", delimiter=',', header=0)
print(gsp)
print(gsp.columns)

#Converting the column Date to Datetime
gsp['Date'] = pd.to_datetime(gsp['Date'])

# Sort the DataFrame by date
gsp = gsp.sort_values(by='Date')

# Plotting the time series line chart of all the prices
plt.figure(figsize=(12, 6))
plt.plot(gsp['Date'], gsp['Close'], label='Closing Price', color='blue',linestyle='-', linewidth=2)
plt.plot(gsp['Date'], gsp['Open'], label='Opening Price', color='red', linestyle='--', linewidth=2)
plt.plot(gsp['Date'], gsp['Low'], label='Lowest Price', color='green', linestyle=':', linewidth=2)
plt.plot(gsp['Date'], gsp['High'], label='Highest Price', color='Yellow', linestyle='-.', linewidth=2)
plt.title('Google Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Prices')
plt.legend()
plt.grid(True)
plt.show()

# Plot the correlation matrix
file=gsp[['Volume','Open','High','Low','Close', 'Adj Close']]
correlation_matrix = file.corr()
print(correlation_matrix)


# Create a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()



#Lineplot of closing prices
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Close', data=gsp)
plt.title('Google Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()


#Line plot of daily percentage change in closing prices
gsp['Daily Change'] = gsp['Close'].pct_change() * 100

plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Daily Change', data=gsp)
plt.title('Daily Percentage Change in Closing Prices')
plt.xlabel('Date')
plt.ylabel('Daily Change (%)')
plt.show()

# Assuming a 30-day moving average
gsp['30 Day MA'] = gsp['Close'].rolling(window=30).mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Close', data=gsp, label='Closing Price')
sns.lineplot(x='Date', y='30 Day MA', data=gsp, label='30 Day Moving Average')
plt.title('Google Stock Price with 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

#Trading Volume over time
plt.figure(figsize=(10,8))
sns.lineplot(x='Date', y='Volume', data=gsp, color='green')
plt.title('Trading Volume over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()


