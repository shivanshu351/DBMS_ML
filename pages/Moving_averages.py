import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
header_section=st.container()
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_stock=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_btzobis2.json")
with header_section:
    lottie_column,title_column=st.columns([1,2])
    with title_column:
        st.title("Analysis of the Moving Averages of Various stocks")
    with lottie_column:
        st_lottie(lottie_stock)
st.subheader("What are moving averages ? ")
st.write('A moving average is a statistic that captures the average change in a data series over time. In finance, moving averages are often used by technical analysts to keep track of price trends for specific securities')
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2023,3,10)
st.subheader('Enter Stock to be Analysed')
user_input = st.text_input('','AAPL')
df = yf.download(user_input, start=start, end=end)
st.subheader('Description of Min and Max Price values of the stock')
st.write(df.describe())
st.subheader('Plot of the closing Prices')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)
st.subheader('Plot of the MA100 vs Closing Price')
ma100 = df.Close.rolling(100).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)
st.subheader('Plot of MA50 MA100 MA200 vs Closing Price ')
fig=plt.figure(figsize=(12,6))
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
ma50 = df.Close.rolling(50).mean()
plt.plot(ma50)
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)