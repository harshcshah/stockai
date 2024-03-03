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

st.set_page_config(
    page_title="Home_page",
    page_icon="🏠",
    )

page_bg_img= """
<style>
[data-testid="stAppViewContainer"]
      {
        background-image: url("https://getwallpapers.com/wallpaper/full/6/c/d/129192.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        
       }
[data-testid="stSidebar"]{ 
    background-image: url("https://w0.peakpx.com/wallpaper/57/269/HD-wallpaper-gradient-black-amoled-color-dark-simple-thumbnail.jpg");
    top:50px;
    background-repeat: repeat-y;
    height: 100%;
   background-size: contain;
    opacity:1;
}

  
[data-testid="collapsedControl"]{
    top:50px;
}
  
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html = True)




# def creds_entered():
#         allowed_usernames = ["stockx"]
#         allowed_passwd = ["stockx"]
#         if st.session_state["user"].strip() in allowed_usernames and st.session_state["passwd"].strip() in allowed_passwd:
#             st.session_state["authenticated"] = True
#         else:
#                 st.session_state["authenticated"] = False 
#                 if not st.session_state["passwd"]:
#                        st.warning("Please enter password.")
#                 elif not st.session_state["user"]:
#                         st.warning("Please enter username.")
#                 else:
#                         st.error("Invalid Username/Password:face_with_raised_eyebrow:")


# def authenticate_user():
#         from PIL import Image
#         img = Image.open("download.png")
#         st.image(img)
#         st.header("Login " )
#         if "authenticated" not in st.session_state:
#             st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
#             st.text_input(label="Password:", value="", key="passwd", type="password", on_change=creds_entered) 
#             return False

#         else:
#             if st.session_state["authenticated"]:
#                 return True

#             else:
#                 st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
#                 st.text_input(label="Password", value="", key="passwd", type="password", on_change=creds_entered) 
#                 return False

# if authenticate_user():
    

# Title
app_name = 'Welcome to Stock Dashboard'

st.write("<p style='color:#EADFB4; font-size: 50px; font-weight: bold;'>Welcome to Stock Dashboard</p>", unsafe_allow_html=True)
#st.balloons()
st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")

st.session_state["background"] = page_bg_img

#date selection code range
st.write("<p style='color:#51829B; font-size: 40px; font-weight: bold;'>Select the parameters from below</p>", unsafe_allow_html=True)
start_date = st.date_input('Start date', date(2020, 1, 1))
end_date = st.date_input('End date', date (2020, 12, 31))

#add ticker symbol list
ticker_list = ["AAPL", "MSFT", "GOOG", "GOOGL", "META", "TSLA", "NVDA", "ADBE", "PYPL", "INTC", "CMCSA", "NFLX", "PEP"]
ticker = st.selectbox('Select the company', ticker_list)

# fetch data from user inputs using yfinance library
data = yf.download(ticker,start=start_date,end=end_date)
data.insert(0, "Date", data.index, True)
data.reset_index(drop=True, inplace=True)
st.write('Data from', start_date, 'to', end_date)
st.write(data)

st.session_state['end_date'] = end_date


st.session_state["data"]=data
st.session_state['ticker'] = ticker

#add a select box to select column from data
column = st.selectbox('Select the column to be used for forecasting',data.columns[1:])
# subsetting the data
data = data[['Date', column]]
st.write("Selected Data")
st.write(data)
st.session_state['column']=column