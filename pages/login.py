
import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Cosmos | 로그인",
    page_icon="✿",
    layout="centered"
)

SUPABASE_URL = "https://mkvlgqcrgpqsmrlmuvjx.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_QhXwfPy9tfGK06BAWn24og_RE2chtR8"


@st.cache_resource
def get_supabase():
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


client = get_supabase()
st.session_state["cosmos_supabase"] = client

st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}
[data-testid="stSidebar"] {
    display: none;
}
.block-container {
    max-width: 440px;
    padding-top: 8vh;
}
.stApp {
    background: #f5f6f8;
}
div[data-testid="stForm"] {
    background: white;
    padding: 25px;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)


# 이미 로그인되어 있다면 그래프 페이지로 이동
if (
    st.session_state.get("cosmos_authenticated")
    and st.session_state.get("cosmos_session")
):
    st.switch_page("main.py")


st.markdown(
    "<h1 style='text-align:center;'>✿ Cosmos</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#777;'>Math to Music Studio</p>",
    unsafe_allow_html=True
)

mode = st.radio(
    "계정 메뉴",
    ["로그인", "회원가입"],
    horizontal=True,
    label_visibility="collapsed"
)


# -------------------------
# 로그인
# -------------------------
if mode == "로그인":

    with st.form("login_form"):
        st.subheader("로그인")

        email = st.text_input(
            "이메일",
            placeholder="name@example.com"
        )

        password = st.text_input(
            "비밀번호",
            type="password"
        )

        submitted = st.form_submit_button(
            "로그인",
            use_container_width=True,
            type="primary"
        )

    if submitted:

        if not email.strip() or not password:
            st.error("이메일과 비밀번호를 입력해 주세요.")

        else:
            try:
                result = client.auth.sign_in_with_password({
                    "email": email.strip().lower(),
                    "password": password
                })

                if result.user and result.session:

                    st.session_state["cosmos_user"] = result.user
                    st.session_state["cosmos_session"] = result.session
                    st.session_state["cosmos_authenticated"] = True

                    st.switch_page("main.py")

                else:
                    st.error("로그인 세션을 확인하지 못했습니다.")

            except Exception as e:
                st.error("로그인에 실패했습니다.")
                st.caption(str(e))


# -------------------------
# 회원가입
# -------------------------
else:

    with st.form("signup_form"):

        st.subheader("회원가입")

        name = st.text_input("이름")

        email = st.text_input(
            "이메일",
            placeholder="name@example.com"
        )

        password = st.text_input(
            "비밀번호 (8자 이상)",
            type="password"
        )

        confirm = st.text_input(
            "비밀번호 확인",
            type="password"
        )

        submitted = st.form_submit_button(
            "회원가입",
            use_container_width=True,
            type="primary"
        )

    if submitted:

        if not name.strip() or not email.strip():
            st.error("이름과 이메일을 입력해 주세요.")

        elif len(password) < 8:
            st.error("비밀번호는 8자 이상이어야 합니다.")

        elif password != confirm:
            st.error("비밀번호가 일치하지 않습니다.")

        else:
            try:
                result = client.auth.sign_up({
                    "email": email.strip().lower(),
                    "password": password,
                    "options": {
                        "data": {
                            "display_name": name.strip()
                        }
                    }
                })

                if result.user and result.session:

                    st.session_state["cosmos_user"] = result.user
                    st.session_state["cosmos_session"] = result.session
                    st.session_state["cosmos_authenticated"] = True

                    st.switch_page("main.py")

                else:
                    st.success(
                        "회원가입이 완료되었습니다. "
                        "이메일 인증 후 로그인해 주세요."
                    )

            except Exception as e:
                st.error("회원가입에 실패했습니다.")
                st.caption(str(e))


st.markdown(
    "<p style='text-align:center;color:#999;font-size:12px;'>"
    "Cosmos Math to Music Studio"
    "</p>",
    unsafe_allow_html=True
)
