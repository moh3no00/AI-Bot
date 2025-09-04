import streamlit as st
from ..data import get_crypto_tickers, get_commodity_prices
from ..strategy import load_strategies


def render():
    st.header("داشبورد")
    st.subheader("بازار رمز ارزها")
    crypto = get_crypto_tickers(10)
    st.dataframe(crypto)

    st.subheader("بازار کامودیتی ها")
    comm = get_commodity_prices()
    st.dataframe(comm)

    st.subheader("استراتژی‌های فعال")
    for s in load_strategies():
        st.write(f"{s['name']} - {s['market']} - {'فعال' if s['enabled'] else 'غیرفعال'}")
