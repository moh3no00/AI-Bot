import streamlit as st
from pages import dashboard, exchange_settings, broker_settings, strategy_builder, market_analysis

PAGES = {
    "داشبورد": dashboard,
    "تنظیمات صرافی": exchange_settings,
    "تنظیمات بروکر": broker_settings,
    "استراتژی‌ها": strategy_builder,
    "تحلیل بازار": market_analysis,
}


def main():
    st.set_page_config(page_title="ربات معامله‌گر", layout="wide")
    choice = st.sidebar.selectbox("صفحه", list(PAGES.keys()))
    PAGES[choice].render()


if __name__ == "__main__":
    main()
