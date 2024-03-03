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

st.write("<p style='color:#64CCC5; font-size: 50px; font-weight: bold;'>💡Stock Prediction</p>", unsafe_allow_html=True)

background = st.session_state["background"]
st.markdown(background, unsafe_allow_html = True)

st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")

data = st.session_state['data']
column = st.session_state['column']
end_date = st.session_state['end_date']

#Let's Run the model
# user input for three parameters of the model and seasonal order
p = st.slider('Select the value of p', 0, 5, 2) 
d = st.slider('Select the value of d', 0, 5, 1)
q = st.slider('Select the value of q', 0, 5, 2)
seasonal_order = st.number_input('Select the value of seasonal p', 0, 24, 12)

model = sm.tsa.statespace.SARIMAX(data[column], order=(p,d,q), seasonal_order=(p,d,q,seasonal_order))
model = model.fit()
# print model summary
st.header('Model Summary')
st.write(model.summary())
st.write("---")
st.session_state['model'] = model
st.session_state['p'] = p
st.session_state['d'] = d
st.session_state['q'] = q
st.session_state['seasonal_order'] = seasonal_order

# predict the future values (Forecasting)
st.write("<p style='color:green; font-size: 50px; font-weight: bold;'>Forecasting the data</p>", unsafe_allow_html=True)
forecast_period = st.number_input('Select the number of days to forecast', 1, 365, 10)
#predict the future values
predictions = model.get_prediction(start=len(data), end=len(data)+forecast_period)
predictions = predictions.predicted_mean
st.write(predictions)
# add index to the predictions
predictions.index = pd.date_range(start=end_date, periods=len(predictions), freq='D')
predictions = pd.DataFrame(predictions)
predictions.insert(0, "Date", predictions.index, True)
st.write("Predictions", predictions)
st.write("Actual Data", data)
st.write("---")

#lets plot the data
fig= go.Figure()
#add actual data to the plot
fig.add_trace(go.Scatter(x=data["Date"], y=data[column], mode='lines',name='Actual', line=dict(color='blue')))
#add predicted data to the plot
fig.add_trace(go.Scatter(x=predictions ["Date"], y=predictions["predicted_mean"], mode='lines', name='Predicted', line=dict(color='red')))
# set the title and axis labels
fig.update_layout(title='Actual vs Predicted', xaxis_title='Date', yaxis_title='Price', width=1200, height=400)
#display the plot
st.plotly_chart(fig)
