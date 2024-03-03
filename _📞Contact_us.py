import streamlit as st
import pandas as pd


st.write("<p style='color:#64CCC5; font-size: 50px; font-weight: bold;'>📞Contact us</p>", unsafe_allow_html=True)
st.write("<p style='color:#F1B4BB; font-size: 30px; font-weight: bold;'>G H Patel College of Engineering & Technology</p>", unsafe_allow_html=True)

background = st.session_state["background"]
st.markdown(background, unsafe_allow_html = True)

st.sidebar.success("Select the option")
from PIL import Image
img = Image.open("download.png")
st.sidebar.image("https://www.battery.com/wp-content/uploads/2021/03/StockX_logo_white.png")

contact = {
     "Name": ["Pratham Mittal","Harsh shah","Vishnu Makupalli","Shiv Patel"],
     "Email" :["prathammittal2411@gmail.com","harshcshah7@gmail.com","mr.mv017@gmail.com","shivpatel131102@gmail.com"]
     
}

df = pd.DataFrame(contact,index=[1,2,3,4])
st.write(df)