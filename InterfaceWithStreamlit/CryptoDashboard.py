import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Crypto charts")
tickers = ['ETH-USD', 'BTC-USD', 'LTC-USD','TSLA', 'AAPL']
st.header("streamlit Package")

dropdwon = st.multiselect("Select Crypto", tickers)
start = st.date_input("Start", value = pd.to_datetime("2023-01-01"))
end = st.date_input("End", value = pd.to_datetime('today'))

if len(dropdwon) > 0:
    for crypto in dropdwon:
        st.write(crypto)
        data = yf.download(crypto, start = start, end = end)['close']
        st.line_chart(data.Close)

        st.write(crypto+" Volume" )
        st.line_chart(data.Volume)
        
        st.write(crypto+" Data" )
        st.write(data)
