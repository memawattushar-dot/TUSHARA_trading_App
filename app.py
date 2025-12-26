import streamlit as st
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go

# Katti simple setup - No Error Zone
st.set_page_config(page_title="TUSHARA trading")

# Simple Title (Is line se error nahi aayega)
st.title("TUSHARA trading")

# Sidebar
ticker = st.sidebar.text_input("Stock Symbol", "TATAMOTORS.NS")
timeframe = st.sidebar.selectbox("Timeframe", ["15m", "1h", "1d"])

try:
    df = yf.download(ticker, period="5d", interval=timeframe)
    if not df.empty:
        # RSI aur Patterns scan karna
        df.ta.cdl_pattern(name="all", append=True)
        
        # Chart banana
        fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], 
                                           high=df['High'], low=df['Low'], 
                                           close=df['Close'])])
        
        # Patterns ko mark karna
        pattern_cols = [col for col in df.columns if col.startswith('CDL_')]
        for p in pattern_cols:
            hits = df[df[p] != 0]
            for idx, row in hits.iterrows():
                fig.add_annotation(x=idx, y=row['High'], text="●", showarrow=False, font=dict(color="yellow"))

        fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
        st.write("✅ Owner: SUJAL MEMAWAT")
    else:
        st.error("Data nahi mila! Symbol check karein.")
except Exception as e:
    st.error(f"Error: {e}")
