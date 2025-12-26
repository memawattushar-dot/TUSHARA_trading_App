import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# App ka Title aur Setup
st.set_page_config(page_title="TUSHARA trading", layout="wide")

st.title("📈 TUSHARA trading - Sujal Memawat Special")
st.subheader("Bhopal ki Sabse Tez Trading App")

# Sidebar - Settings ke liye
st.sidebar.header("Control Panel")
market = st.sidebar.selectbox("Market Chuno", ["Crypto", "Indian Stocks", "Forex"])
symbol = st.sidebar.text_input("Symbol Daalo (e.g. BTCUSDT, RELIANCE)", "BTCUSDT")

# Ek Dummy Data Banate hain (Asli trading ke liye API lagegi)
def get_mock_data():
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [0.1, 0.1],
        columns=['Price', 'Volume']
    )
    return chart_data

data = get_mock_data()

# Main Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.write(f"### {symbol} ka Live Chart")
    # Chart dikhane ke liye
    fig = go.Figure(data=[go.Candlestick(x=list(range(len(data))),
                open=data['Price']+0.01, high=data['Price']+0.02,
                low=data['Price']-0.01, close=data['Price'])])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("### Buy/Sell Panel")
    quantity = st.number_input("Kitna Maal Kharedna Hai?", min_value=1)
    
    if st.button("BUY (Kharedo)", use_container_width=True):
        st.success(f"Miyan, {quantity} {symbol} khared liye gaye hain!")
        st.balloons()
        
    if st.button("SELL (Becho)", type="primary", use_container_width=True):
        st.error(f"{quantity} {symbol} bech diye! Munafa ghar le jao.")

# Market News Section
st.divider()
st.write("### Market ki Garma-Garam Khabrein")
st.info("Bhopali Market Update: Aaj market upar jane ke poore chances hain!")
