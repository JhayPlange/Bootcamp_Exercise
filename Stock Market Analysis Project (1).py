#!/usr/bin/env python
# coding: utf-8

# # STOCK MARKET ANALYSIS PROJECT

# # Importing the necessary libraries 

# In[1]:


import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


today = date.today()


# In[3]:


d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2


# # Downloading Microsoft stock data from online

# In[4]:


data = yf.download('MSFT', 
                      start=start_date, 
                      end=end_date, 
                      progress=False)


# In[5]:


data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", 
             "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())


# # Displaying the candlesticks - a handy tool to analyze the price movements of stock prices

# In[6]:


figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Microsoft Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()


# # Using Bar Plot to also visualize price movements

# In[7]:


figure = px.bar(data, x = "Date", y= "Close")
figure.show()


# # Using Range Slider - It helps analyze the stock market between two specific points by interactively selecting the time period.

# In[8]:


figure = px.line(data, x='Date', y='Close', 
                 title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()


# # Using Time Period Selectors - Time period selectors are like buttons that show you the graph of a specific time period

# In[9]:


figure = px.line(data, x='Date', y='Close', 
                 title='Stock Market Analysis with Time Period Selectors')

figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()


# # Removing weekend trends from the stock market visualization

# In[10]:


figure = px.scatter(data, x='Date', y='Close', range_x=['2021-07-12', '2022-07-11'],
                 title="Stock Market Analysis by Hiding Weekend Gaps")
figure.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat","sun"])
    ]
)
figure.show()


# # Summary
# 
# 
# # So this is how you may use the Python computer language to examine the stock market interactively. Stock market analysis entails examining current and past stock market trends in order to determine future purchasing and selling decisions. I hope you enjoyed my post on Stock Market Analysis with Python. Please leave valuable questions in the comments area below.

# In[ ]:




