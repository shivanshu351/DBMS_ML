import pymongo
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
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
lottie_stock=load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_F3v2Nj.json")
with header_section:
    lottie_column,title_column=st.columns([1,2])
    with title_column:
        st.title("Top Performing stocks in India")
    with lottie_column:
        st_lottie(lottie_stock)
AxisBank=st.container()
AdaniPorts=st.container()
BharatAirtel=st.container()
AsianPaints=st.container()
BajajAuto=st.container()
IciciBank=st.container()
with AxisBank:
    st.header("AXIS-BANK")
    if __name__=="__main__":
        client=1;
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['project_test_database_1']
        col=db['AXISBANK']
        a = st.text_input("Enter date for which the data is to be fetched : ",'2001-01-01')
        a=a+''
        print(a)
        data=col.find_one({'Date': a})
        print(data)
        val_col,disp_col=st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1,val_col_2,disp_col_2,disp_col_3,disp_col_4,disp_col_5=st.columns(6)
        with val_col_1:
            a1=st.text_input("Enter Start Date : ",'2000-01-03')
        with val_col_2:
            a2=st.text_input("Enter End Date",'2000-01-05')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                         {'$group': {'_id': '$Symbol', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)
with AdaniPorts:
    st.header('ADANI-PORTS')
    if __name__=="__main__":
        client=1;
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['project_test_database_1']
        col=db['ADANIPORTS']
        a = st.text_input("Enter date for which the data is to be fetched : ",'2007-11-28')
        a=a+''
        print(a)
        data=col.find_one({'Date': a})
        print(data)
        val_col,disp_col=st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1,val_col_2,disp_col_2,disp_col_3,disp_col_4,disp_col_5=st.columns(6)
        with val_col_1:
            a1=st.text_input("Enter Start Date : ",'2007-11-28')
        with val_col_2:
            a2=st.text_input("Enter End Date",'2007-11-29')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                         {'$group': {'_id': '$Symbol', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)
with BharatAirtel:
    st.header('BHARAT-AIRTEL')
    if __name__ == "__main__":
        client = 1;
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['project_test_database_1']
        col = db['BHARTIARTL']
        a = st.text_input("Enter date for which the data is to be fetched : ", '2002-02-18')
        a = a + ''
        print(a)
        data = col.find_one({'Date': a})
        print(data)
        val_col, disp_col = st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1, val_col_2, disp_col_2, disp_col_3, disp_col_4, disp_col_5 = st.columns(6)
        with val_col_1:
            a1 = st.text_input("Enter Start Date : ", '2002-02-18')
        with val_col_2:
            a2 = st.text_input("Enter End Date", '2002-05-18')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)
with AsianPaints:
    st.header('ASIAN-PAINTS')
    if __name__ == "__main__":
        client = 1;
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['project_test_database_1']
        col = db['ASIANPAINTS']
        a = st.text_input("Enter date for which the data is to be fetched : ", '2003-01-22')
        a = a + ''
        print(a)
        data = col.find_one({'Date': a})
        print(data)
        val_col, disp_col = st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1, val_col_2, disp_col_2, disp_col_3, disp_col_4, disp_col_5 = st.columns(6)
        with val_col_1:
            a1 = st.text_input("Enter Start Date : ",'2003-02-18')
        with val_col_2:
            a2 = st.text_input("Enter End Date", '2003-05-18')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)
with BajajAuto:
    st.header('BAJAJ-AUTO')
    if __name__ == "__main__":
        client = 1;
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['project_test_database_1']
        col = db['BAJAJAUTO']
        a = st.text_input("Enter date for which the data is to be fetched : ", '2008-05-26')
        a = a + ''
        print(a)
        data = col.find_one({'Date': a})
        print(data)
        val_col, disp_col = st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1, val_col_2, disp_col_2, disp_col_3, disp_col_4, disp_col_5 = st.columns(6)
        with val_col_1:
            a1 = st.text_input("Enter Start Date : ", '2008-06-05')
        with val_col_2:
            a2 = st.text_input("Enter End Date", '2008-06-06')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)
with IciciBank:
    st.header('ICICI-BANK')
    if __name__ == "__main__":
        client = 1;
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['project_test_database_1']
        col = db['ICICIBANK']
        a = st.text_input("Enter date for which the data is to be fetched : ", '2001-01-05')
        a = a + ''
        print(a)
        data = col.find_one({'Date': a})
        print(data)
        val_col, disp_col = st.columns(2)
        with val_col:
            st.write("Data Fetched :")
        with disp_col:
            st.write(data)
        st.subheader("Avg opening , Avg closing Max opening and Min closing Prices")
        val_col_1, val_col_2, disp_col_2, disp_col_3, disp_col_4, disp_col_5 = st.columns(6)
        with val_col_1:
            a1 = st.text_input("Enter Start Date : ", '2008-06-03')
        with val_col_2:
            a2 = st.text_input("Enter End Date", '2008-06-08')
        with disp_col_2:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Open_avg_price': {'$avg': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_3:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '_id', 'Close_avg_price': {'$avg': '$Close'}}}])
            for i in data:
                st.write(i)
        with disp_col_4:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Max_open_price': {'$max': '$Open'}}}])
            for i in data:
                st.write(i)
        with disp_col_5:
            data = col.aggregate([{'$match': {'Date': {'$gte': a1, '$lte': a2}}},
                                  {'$group': {'_id': '$Symbol', 'Min_Close_price': {'$min': '$Close'}}}])
            for i in data:
                st.write(i)






