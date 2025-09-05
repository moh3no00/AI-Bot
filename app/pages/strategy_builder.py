import streamlit as st
from ..strategy import load_strategies, save_strategies, add_strategy


def render():
    st.header("ساخت استراتژی")
    with st.form("new_strategy"):
        name = st.text_input("نام استراتژی")
        market = st.selectbox("بازار", ["crypto", "commodity"])
        asset = st.text_input("نماد دارایی")
        stop_loss = st.number_input("حد ضرر", value=0.0)
        take_profit = st.number_input("حد سود", value=0.0)
        volume = st.number_input("حجم معامله", value=1.0)
        script = st.text_area("دستور متنی")
        submitted = st.form_submit_button("ذخیره")
        if submitted:
            add_strategy(
                name,
                script,
                market,
                asset,
                True,
                stop_loss if stop_loss > 0 else None,
                take_profit if take_profit > 0 else None,
                volume,
            )
            st.success("استراتژی اضافه شد")

    st.subheader("مدیریت استراتژی‌ها")
    strategies = load_strategies()
    for idx, s in enumerate(strategies):
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.write(f"{s['name']} - {s['market']}")
        s['enabled'] = col2.checkbox("فعال", value=s['enabled'], key=idx)
        s['asset'] = col3.text_input("نماد", value=s.get('asset', ''), key=f"asset_{idx}")
        s['stop_loss'] = col4.number_input(
            "حد ضرر", value=s.get("stop_loss", 0.0), key=f"sl_{idx}"
        )
        s['take_profit'] = col5.number_input(
            "حد سود", value=s.get("take_profit", 0.0), key=f"tp_{idx}"
        )
        s['volume'] = col6.number_input(
            "حجم", value=s.get("volume", 1.0), key=f"vol_{idx}"
        )
    if st.button("ذخیره تغییرات"):
        for s in strategies:
            if s.get("stop_loss", 0) <= 0:
                s["stop_loss"] = None
            if s.get("take_profit", 0) <= 0:
                s["take_profit"] = None
        save_strategies(strategies)
        st.success("ذخیره شد")
