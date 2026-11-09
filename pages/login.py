import requests
import streamlit as st

st.set_page_config(
    page_title="Cosmos | 로그인",
    page_icon="✿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

SUPABASE_URL = "https://mkvlgqcrgpqsmrlmuvjx.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "sb_publishable_QhXwfPy9tfGK06BAWn24og_RE2chtR8"

st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      [data-testid="stSidebar"] { display: none; }
      .stApp { background: #f7f8fa; }
      .block-container { max-width: 470px; padding-top: 7vh; }
      .cosmos-brand { text-align:center; font-family: Georgia,serif; font-size:34px;
        font-weight:700; font-style:italic; color:#222; margin-bottom:4px; }
      .cosmos-subtitle { text-align:center; color:#777; font-size:13px; margin-bottom:28px; }
      div.stButton > button { width:100%; border-radius:7px; min-height:42px; }
      div[data-testid="stForm"] { border:0; padding:0; }
    </style>
    <div class="cosmos-brand">cosmos</div>
    <div class="cosmos-subtitle">Math to Music Studio</div>
    """,
    unsafe_allow_html=True,
)

view = st.query_params.get("view", "login")
if view not in ("login", "signup"):
    view = "login"

login_col, signup_col = st.columns(2)
with login_col:
    if st.button("로그인", type="primary" if view == "login" else "secondary"):
        st.query_params["view"] = "login"
        st.rerun()
with signup_col:
    if st.button("회원가입", type="primary" if view == "signup" else "secondary"):
        st.query_params["view"] = "signup"
        st.rerun()

st.divider()


def auth_request(endpoint: str, payload: dict):
    url = f"{SUPABASE_URL}/auth/v1/{endpoint}"
    headers = {
        "apikey": SUPABASE_PUBLISHABLE_KEY,
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=20)
    except requests.RequestException as exc:
        return None, f"서버에 연결하지 못했습니다: {exc}"

    try:
        data = response.json()
    except ValueError:
        data = {}

    if not response.ok:
        message = data.get("msg") or data.get("message") or data.get("error_description") or "인증 요청에 실패했습니다."
        return None, message
    return data, None


def complete_login(data: dict):
    session = {
        "access_token": data.get("access_token"),
        "refresh_token": data.get("refresh_token"),
        "token_type": data.get("token_type", "bearer"),
        "expires_in": data.get("expires_in"),
        "user": data.get("user", {}),
    }
    st.session_state["cosmos_supabase_session"] = session
    st.session_state["cosmos_user"] = data.get("user", {})
    st.success("인증되었습니다. Cosmos 그래프 화면으로 이동합니다.")
    st.switch_page("main.py")


if view == "login":
    st.subheader("로그인")
    with st.form("cosmos_login_form"):
        email = st.text_input("이메일", placeholder="example@email.com")
        password = st.text_input("비밀번호", type="password", placeholder="비밀번호 입력")
        submitted = st.form_submit_button("로그인", type="primary", use_container_width=True)

    if submitted:
        if not email.strip() or not password:
            st.error("이메일과 비밀번호를 모두 입력해 주세요.")
        else:
            with st.spinner("로그인 중입니다..."):
                data, error = auth_request(
                    "token?grant_type=password",
                    {"email": email.strip(), "password": password},
                )
            if error:
                st.error(f"로그인에 실패했습니다: {error}")
            elif data and data.get("access_token") and data.get("refresh_token"):
                complete_login(data)
            else:
                st.error("로그인 응답에 세션 정보가 없습니다. Supabase 설정을 확인해 주세요.")

else:
    st.subheader("회원가입")
    with st.form("cosmos_signup_form"):
        display_name = st.text_input("닉네임", placeholder="Cosmos에서 사용할 이름")
        email = st.text_input("이메일", placeholder="example@email.com")
        password = st.text_input("비밀번호", type="password", placeholder="8자 이상")
        password_confirm = st.text_input("비밀번호 확인", type="password", placeholder="비밀번호 다시 입력")
        submitted = st.form_submit_button("회원가입", type="primary", use_container_width=True)

    if submitted:
        if not email.strip() or not password or not password_confirm:
            st.error("이메일과 비밀번호를 모두 입력해 주세요.")
        elif len(password) < 8:
            st.error("비밀번호는 8자 이상으로 입력해 주세요.")
        elif password != password_confirm:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            with st.spinner("계정을 생성하고 있습니다..."):
                data, error = auth_request(
                    "signup",
                    {
                        "email": email.strip(),
                        "password": password,
                        "data": {"display_name": display_name.strip() or email.strip().split("@")[0]},
                    },
                )
            if error:
                st.error(f"회원가입에 실패했습니다: {error}")
            elif data and data.get("access_token") and data.get("refresh_token"):
                complete_login(data)
            elif data:
                st.success("회원가입 요청이 완료되었습니다. 이메일 확인이 활성화되어 있다면 인증 메일을 확인한 뒤 로그인해 주세요.")
            else:
                st.error("회원가입 응답을 확인할 수 없습니다.")

st.divider()
if st.button("그래프 계산기로 돌아가기", use_container_width=True):
    st.switch_page("main.py")
