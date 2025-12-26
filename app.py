import streamlit as st
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go

# Bilkul simple setup
st.set_page_config(page_title="TUSHARA trading")

# Title bina kisi special design ke
st.title("TUSHARA trading")

ticker = st.sidebar.text_input("Stock Symbol", "TATAMOTORS.NS")
timeframe = st.sidebar.selectbox("Timeframe", ["15m", "1h", "1d"])

try:
    df = yf.download(ticker, period="5d", interval=timeframe)
    if not df.empty:
        # RSI Indicator
        df['RSI'] = ta.rsi(df['Close'], length=14)
        
        # Simple Candlestick Chart
        fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
        fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False)
        
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"Showing data for: {ticker}")
        st.write("Owner: SUJAL MEMAWAT")
    else:
        st.error("Data nahi mila. Symbol check karein.")
except Exception as e:
    st.error(f"Error: {e}")
