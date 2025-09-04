import streamlit as st
from ..strategy import load_strategies, save_strategies, add_strategy


def render():
    st.header("ساخت استراتژی")
    with st.form("new_strategy"):
        name = st.text_input("نام استراتژی")
        market = st.selectbox("بازار", ["crypto", "commodity"])
        asset = st.text_input("نماد دارایی")
        script = st.text_area("دستور متنی")
        submitted = st.form_submit_button("ذخیره")
        if submitted:
            add_strategy(name, script, market, asset, True)
            st.success("استراتژی اضافه شد")

    st.subheader("مدیریت استراتژی‌ها")
    strategies = load_strategies()
    for idx, s in enumerate(strategies):
        col1, col2, col3 = st.columns(3)
        col1.write(f"{s['name']} - {s['market']} - {s.get('asset','')}")
        s['enabled'] = col2.checkbox("فعال", value=s['enabled'], key=idx)
        s['asset'] = col3.text_input("نماد", value=s.get('asset', ''), key=f"asset_{idx}")
    if st.button("ذخیره تغییرات"):
        save_strategies(strategies)
        st.success("ذخیره شد")
