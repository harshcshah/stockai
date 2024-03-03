import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import datetime
from datetime import date, timedelta
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import json
import requests
from streamlit_lottie import st_lottie


st.write("<p style='color:#C5EBAA; font-size: 50px; font-weight: bold;'>About</p>", unsafe_allow_html=True)

background = st.session_state["background"]
st.markdown(background, unsafe_allow_html = True)

st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")

data = st.session_state["data"]
princing_data,news = st.tabs(["Princing Data","Top 10 news"])

with princing_data:
    st.header("Price Movements")
    data2 = data
    data2["% Change"] = data['Adj Close'] / data['Adj Close'].shift(1) -1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = data2["% Change"].mean()*252*100
    st.write('Annual Return is',annual_return,"%")
    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is ',stdev*100,"%")
    st.write('Risk adj. Return is ',annual_return/(stdev*100))
    
from stocknews import StockNews 
ticker = st.session_state['ticker']
with news:
     st.subheader(f'Newa of {ticker}')
     sn = StockNews(ticker,save_news=False)
     df_news = sn.read_rss()
     for i in range(10):
         st.subheader(f'News{i+1}')
         st.write(df_news['published'][i])
         st.write(df_news['title'][i])
         st.write(df_news['summary'][i])
         title_sentiment = df_news["sentiment_title"][i]
         st.write(f'title Sentiment {title_sentiment}')
         news_sentiment = df_news['sentiment_summary'][i]
         st.write(f'News Sentiment {news_sentiment}')




