import streamlit as st
from ..settings import load_settings, save_settings


def render():
    st.header("تنظیمات بروکر")
    settings = load_settings()
    name = st.text_input("نام بروکر", "demo")
    api_key = st.text_input("API Key", value=settings["brokers"].get(name, {}).get("apiKey", ""))
    secret = st.text_input("Secret", type="password", value=settings["brokers"].get(name, {}).get("secret", ""))
    if st.button("ذخیره"):
        settings["brokers"][name] = {"apiKey": api_key, "secret": secret}
        save_settings(settings)
        st.success("ذخیره شد")
