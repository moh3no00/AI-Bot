import streamlit as st
from ..data import (
    get_crypto_tickers,
    get_commodity_prices,
    get_crypto_history,
    get_commodity_history,
)
from ..ai import analyze_series


def render():
    st.header("تحلیل بازار")
    st.subheader("رمز ارزها")
    crypto_df = get_crypto_tickers(5)
    st.dataframe(crypto_df)
    symbol = st.selectbox("انتخاب رمز ارز برای تحلیل", crypto_df["symbol"])
    if st.button("تحلیل هوشمند رمز ارز"):
        history = get_crypto_history(symbol)
        result = analyze_series(history)
        st.write(
            f"سیگنال پیشنهادی: {result['signal']} | شیب: {result['slope']:.4f} | RSI: {result['rsi']:.2f}"
        )

    st.subheader("کامیودیتی‌ها")
    comm_df = get_commodity_prices()
    st.dataframe(comm_df)
    commodities = {"طلا": "GC=F", "نقره": "SI=F", "نفت": "CL=F"}
    comm_name = st.selectbox("انتخاب کامودیتی برای تحلیل", list(commodities.keys()))
    if st.button("تحلیل هوشمند کامودیتی"):
        history = get_commodity_history(commodities[comm_name])
        result = analyze_series(history)
        st.write(
            f"سیگنال پیشنهادی: {result['signal']} | شیب: {result['slope']:.4f} | RSI: {result['rsi']:.2f}"
        )
