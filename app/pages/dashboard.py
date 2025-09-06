import streamlit as st
from ..data import get_crypto_tickers, get_commodity_prices
from ..strategy import load_strategies
from ..executor import StrategyExecutor


def render():
    st.header("داشبورد")
    st.subheader("بازار رمز ارزها")
    crypto = get_crypto_tickers(10)
    st.dataframe(crypto)

    st.subheader("بازار کامودیتی ها")
    comm = get_commodity_prices()
    st.dataframe(comm)

    st.subheader("استراتژی‌های فعال")
    strategies = load_strategies()
    for s in strategies:
        st.write(
            f"{s['name']} - {s['market']} - {s.get('asset','')} - SL:{s.get('stop_loss','-')} TP:{s.get('take_profit','-')} V:{s.get('volume',1)} - {'فعال' if s['enabled'] else 'غیرفعال'}"
        )
    if st.button("اجرای همزمان استراتژی‌ها"):
        executor = StrategyExecutor()
        results = executor.run_all()
        st.json(results)
