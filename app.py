import streamlit as st
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page setup - Sirf TUSHARA trading dikhega
st.set_page_config(page_title="TUSHARA trading", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>TUSHARA trading</h1>", unsafe_allow_stdio=True)

# Sidebar settings
st.sidebar.header("TUSHARA Settings")
ticker = st.sidebar.text_input("Stock Symbol (e.g. SBIN.NS)", "TATAMOTORS.NS")
timeframe = st.sidebar.selectbox("Timeframe", ["15m", "1h", "1d"])

try:
    # Data fetch karna
    df = yf.download(ticker, period="5d", interval=timeframe)
    
    if not df.empty:
        # Indicators aur Patterns engine
        df.ta.cdl_pattern(name="all", append=True)
        df['RSI'] = ta.rsi(df['Close'], length=14)
        
        # Professional Chart Setup
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.7, 0.3])
        
        # Candle Chart
        fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], 
                                   low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
        
        # RSI Chart
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name='RSI', line=dict(color='#00FFFF')), row=2, col=1)
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

        # Pattern Markers (Yellow dots on chart)
        pattern_cols = [col for col in df.columns if col.startswith('CDL_')]
        for p_col in pattern_cols:
            hits = df[df[p_col] != 0]
            for idx, row in hits.iterrows():
                fig.add_annotation(x=idx, y=row['High'], text="●", showarrow=False, 
                                 font=dict(color="yellow", size=12), row=1, col=1)

        fig.update_layout(template="plotly_dark", height=600, xaxis_rangeslider_visible=False, 
                          margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("✅ Owner: SUJAL MEMAWAT")
    else:
        st.error("Data nahi mila. Symbol sahi dalo (jaise RELIANCE.NS)")
except Exception as e:
    st.error(f"System Error: {e}")
