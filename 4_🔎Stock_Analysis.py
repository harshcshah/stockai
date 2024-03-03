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



st.write("<p style='color:#C5EBAA; font-size: 50px; font-weight: bold;'>🔎Stock Analysis</p>", unsafe_allow_html=True)
background = st.session_state["background"]
st.markdown(background, unsafe_allow_html = True)

st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")


data = st.session_state['data']
column = st.session_state['column']
# ADF test check stationarity
st.header('Is data Stationary?')
st.write('*Note:* If p-value is less than 0.05, then data is stationary')
st.write(adfuller(data[column]))

#lets decompose the data
st.header('Decomposition of the data')
decomposition = seasonal_decompose(data[column], model='additive', period=1)
st.write(decomposition.plot())

#make same plot in plotly
st.write("## Plotting the decomposition in plotly")
st.plotly_chart(px.line(x=data["Date"], y=decomposition.trend, title='Trend', width=1200, height=400, labels={'x':'Date', 'y': 'Price'}).update_traces(line_color='Blue'))
st.plotly_chart(px.line(x=data["Date"], y=decomposition.seasonal, title='Seasonality', width=1200,labels={'x':'Date', 'y': 'Price'}).update_traces(line_color='green'))
st.plotly_chart(px.line(x=data["Date"], y=decomposition.resid, title='Residuals',width=1200, height=400, labels={'x':'Date', 'y': 'Price'}).update_traces(line_color='Red', line_dash='dot'))


