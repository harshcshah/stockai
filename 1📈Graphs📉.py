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
import time



st.write("<p style='color:#C5EBAA; font-size: 50px; font-weight: bold;'>📈Graphs</p>", unsafe_allow_html=True)

background = st.session_state["background"]
st.markdown(background, unsafe_allow_html = True)

st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")

data = st.session_state["data"]
 #plot the data
ticker=st.session_state['ticker']
st.write("<p style='color:#C5EBAA; font-size: 50px; font-weight: bold;'>Data Visualization</p>", unsafe_allow_html=True)
st.subheader('Plot of the data')
st.markdown(background, unsafe_allow_html = True)
st.title(ticker)
fig = px.line(data, x='Date', y=data.columns, title='Closing price of the stock')
st.plotly_chart(fig)


st.write("<p style='color:lightblue; font-size: 50px; font-weight: bold;'>Real-time Stock Prices</p>", unsafe_allow_html=True)
# Define the ticker symbol for Apple
ticker_symbol = ticker
sym = ticker
st.header(ticker)
def open_link(url):
    import webbrowser
    webbrowser.open_new_tab(url)
if st.button("LIVE"):
    open_link("https://in.tradingview.com/chart/?symbol="+sym)


# Get the data of the stock
apple_stock = yf.Ticker(ticker_symbol)

# Create a matplotlib figure
fig, ax = plt.subplots()

# Use st.pyplot to display the plot
plot = st.pyplot(fig)

# Loop to fetch and update stock values
while True:
    # Get the historical prices for Apple stock
    historical_prices = apple_stock.history(period='1d', interval='1m')
    
    # Get the latest price and time
    latest_price = historical_prices['Close'].iloc[-1]
    latest_time = historical_prices.index[-1].strftime('%H:%M:%S')
    
    # Clear the plot and plot the new data
    ax.clear()
    ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
    ax.set_xlabel('Time')
    ax.set_ylabel('Stock Value')
    ax.set_title('Stock Value')
    ax.legend(loc='upper left')
    ax.tick_params(axis='x', rotation=45)
    
    # Update the plot in the Streamlit app
    plot.pyplot(fig)
    
    # Show the latest stock value in the app
    st.write(f"Latest Price ({latest_time}): {latest_price}")
    
    # Sleep for 1 minute before fetching new data
    time.sleep(2)


