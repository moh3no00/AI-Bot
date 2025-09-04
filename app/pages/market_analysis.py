import streamlit as st
from ..data import get_crypto_tickers, get_commodity_prices


def render():
    st.header("تحلیل بازار")
    st.subheader("رمز ارزها")
    st.dataframe(get_crypto_tickers(5))
    st.subheader("کامیودیتی‌ها")
    st.dataframe(get_commodity_prices())
    st.info("بخش تحلیل هوش مصنوعی نیاز به توسعه بیشتر دارد.")
