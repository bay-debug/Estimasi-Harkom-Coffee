import pickle
import streamlit as st

model = pickle.load(open('estimasi_Harkom_Coffee.sav', 'rb'))

st.title('Estimasi Harga Komoditas Kategori Minuman Coffee')

year = st.number_input('Input Tahun Harga Komoditas Kategori Minuman')
Cocoa = st.number_input('Input Harga Komoditas Cocoa')
Tea = st.number_input('Input Harga Komoditas Tea')


predict = ''

if st.button('Estimasi Harga Komoditas Kategori Minuman Coffee'):
    predict = model.predict(
        [[year, Cocoa, Tea]]
    )
    st.write ('Estimasi harga komoditas kategori minuman ($/Kg): ', predict)
    st.write ('Estimasi harga komoditas kategori minuman IDR (Rp/Kg) :', predict*19000)