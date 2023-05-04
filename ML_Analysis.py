import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import streamlit as st
import json
import requests
from keras.models import load_model
from sklearn.model_selection import StratifiedShuffleSplit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from keras.models import load_model
from sklearn.model_selection import StratifiedShuffleSplit
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
lottie_stock=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_LmW6VioIWc.json")
with header_section:
    lottie_column,title_column=st.columns([1,2])
    with title_column:
        st.title("DataBase Analysis using Machine Learning")
    with lottie_column:
        st_lottie(lottie_stock)
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2023,3,10)
user_input = st.text_input('Enter stock to be analysed','AAPL')
df = yf.download(user_input, start=start, end=end)

#creating the training and the testing arrays for our database here choosing 70% as our training data and 30% as our testing data
df=df.reset_index()
df = df.drop(['Open'], axis=1)
df = df.drop(['High'], axis=1)
df = df.drop(['Adj Close'], axis=1)
df = df.drop(['Volume'], axis=1)
df = df.drop(['Low'], axis=1)
df=df.drop(['Date'],axis=1)
#defining the date time values time period for stock analysis
close_srt=df
# print(close_srt)
#feature Scaling to scale the prices between the range of 0 to 1 using the min_Max scaler
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
close_srt=scaler.fit_transform(np.array(close_srt).reshape(-1,1))
# print(close_srt)

#Splitting of data
#creating the training and the testing arrays for our database here choosing 70% as our training data and 30% as our testing data
train_size=int(len(close_srt)*0.7)
test_size=len(close_srt)-train_size
train_data,test_data=close_srt[0:train_size,:],close_srt[train_size:len(close_srt ),:1]
#Converting values into a dataset Matrix
def create_MLdataset(dataset,time_step=1):
    data_X,data_y=[],[]
    for i in range(len(dataset)-time_step-1):
        a=dataset[i:(i+time_step),0]
        data_X.append(a)
        data_y.append(dataset[i+time_step,0])
    return np.array(data_X),np.array(data_y)
time_step=100
#creating values for our x-train and y-train arrays
x_train,y_train= create_MLdataset(train_data,time_step)
x_test,y_test=create_MLdataset(test_data,time_step)
x_train=x_train.reshape(x_train.shape[0],x_train.shape[1],1)
x_test=x_test.reshape(x_test.shape[0],x_test.shape[1],1)

#loading the model
model=load_model('final_model_2.h5')
train_predict=model.predict(x_train)
test_predict=model.predict(x_test)

train_predict=scaler.inverse_transform(train_predict)
test_predict=scaler.inverse_transform(test_predict)

look_back=100
#shift_train_data
trainPredictPlot=np.empty_like(close_srt)
trainPredictPlot[:,:]=np.nan
trainPredictPlot[look_back:len(train_predict)+look_back,:]=train_predict
#shift_test_data
testPredictPlot=np.empty_like(close_srt)
testPredictPlot[:,:]=np.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(close_srt)-1,:]=test_predict
fig=plt.figure(figsize=(12,6))
plt.plot(scaler.inverse_transform(close_srt))
plt.plot(trainPredictPlot,color='r',label='Original price')
plt.plot(testPredictPlot,color='g',label='Predicted price')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Price')
st.subheader('Days vs Closing Price Plot')
st.pyplot(fig)

