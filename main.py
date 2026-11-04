
import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Cosmos | 그래핑 계산기",
    page_icon="✿",
    layout="wide"
)

# 로그인 여부 확인
if not st.session_state.get("cosmos_authenticated"):
    st.switch_page("pages/로그인.py")
    st.stop()

session = st.session_state.get("cosmos_session")
user = st.session_state.get("cosmos_user")
client = st.session_state.get("cosmos_supabase")

if session is None or user is None:
    st.session_state["cosmos_authenticated"] = False
    st.switch_page("pages/로그인.py")
    st.stop()

# 로그아웃
left, right = st.columns([8, 1])

with left:
    st.caption(f"로그인 계정: {user.email}")

with right:
    if st.button("로그아웃"):
        try:
            client.auth.sign_out()
        except Exception:
            pass

        for key in [
            "cosmos_authenticated",
            "cosmos_session",
            "cosmos_user"
        ]:
            st.session_state.pop(key, None)

        st.switch_page("pages/로그인.py")

