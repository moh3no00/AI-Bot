import streamlit as st
from ..settings import load_settings, save_settings
from ..trading import ExchangeManager

manager = ExchangeManager()


def render():
    st.header("تنظیمات صرافی")
    settings = load_settings()
    name = st.selectbox("نام صرافی", ["binance", "kraken", "coinbasepro"])
    api_key = st.text_input("API Key", value=settings["exchanges"].get(name, {}).get("apiKey", ""))
    secret = st.text_input("Secret", type="password", value=settings["exchanges"].get(name, {}).get("secret", ""))
    if st.button("ذخیره و اتصال"):
        settings["exchanges"][name] = {"apiKey": api_key, "secret": secret}
        save_settings(settings)
        try:
            manager.connect(name, api_key, secret)
            st.success("اتصال موفق بود")
        except Exception as e:
            st.error(f"خطا در اتصال: {e}")
