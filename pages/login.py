import json
import urllib.error
import urllib.request

import streamlit as st

st.set_page_config(
    page_title="Cosmos | 계정",
    page_icon="✿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SUPABASE_URL = "https://mkvlgqcrgpqsmrlmuvjx.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_QhXwfPy9tfGK06BAWn24og_RE2chtR8"

st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stAppViewContainer"], [data-testid="stMain"] { background: #f7f8fa; }
    .block-container { max-width: 100% !important; padding: 0 0 3rem 0 !important; }
    .cosmos-topbar { height: 48px; width: 100%; background: #222; color: white;
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 12px; box-sizing: border-box; position: relative; }
    .cosmos-topbar-left { width: 30%; min-width: 80px; }
    .cosmos-topbar-brand { position: absolute; left: 50%; transform: translateX(-50%);
        color: white; font-family: Georgia, serif; font-size: 20px; font-weight: 700;
        font-style: italic; letter-spacing: -.5px; }
    .cosmos-topbar-right { margin-left: auto; display: flex; align-items: center; gap: 6px; }
    .top-login, .top-signup { display: inline-flex; align-items: center; justify-content: center;
        height: 32px; padding: 0 12px; border-radius: 4px; text-decoration: none !important;
        font-size: 12px; font-weight: 600; white-space: nowrap; box-sizing: border-box; }
    .top-login { color: #fff !important; background: transparent; }
    .top-login:hover, .top-login.active { color: #fff !important; background: #3b3b3b; }
    .top-signup { color: #fff !important; background: #2b72ee; box-shadow: 0 1px 2px rgba(0,0,0,.12); }
    .top-signup:hover, .top-signup.active { color: #fff !important; background: #1a62e0; }
    .auth-title { font-size: 24px; font-weight: 700; color: #202124; margin: 0 0 6px; }
    .auth-caption { color: #6b7280; font-size: 13px; margin-bottom: 22px; }
    div[data-testid="stTextInput"] label { font-size: 12px; font-weight: 600; color: #4b5563; }
    div[data-testid="stFormSubmitButton"] button { background: #2b72ee; color: white;
        border: 1px solid #2b72ee; border-radius: 5px; min-height: 40px; font-weight: 700; }
    div[data-testid="stFormSubmitButton"] button:hover { background: #1a62e0; color: white; border-color: #1a62e0; }
    @media (max-width: 600px) { .cosmos-topbar-left { width: 15%; } }
</style>
""", unsafe_allow_html=True)

view = st.query_params.get("view", "login")
if view not in ("login", "signup"):
    view = "login"
login_class = "top-login active" if view == "login" else "top-login"
signup_class = "top-signup active" if view == "signup" else "top-signup"

st.markdown(
    '<div class="cosmos-topbar">'
    '<div class="cosmos-topbar-left"></div>'
    '<div class="cosmos-topbar-brand">cosmos</div>'
    '<div class="cosmos-topbar-right">'
    f'<a class="{login_class}" href="?view=login">로그인</a>'
    f'<a class="{signup_class}" href="?view=signup">회원가입</a>'
    '</div></div>',
    unsafe_allow_html=True,
)

left_col, auth_col, right_col = st.columns([1, 1.15, 1])
with auth_col:
    st.markdown('<div style="height:48px"></div>', unsafe_allow_html=True)

    if view == "login":
        st.markdown('<div class="auth-title">로그인</div>', unsafe_allow_html=True)
        st.markdown('<div class="auth-caption">Cosmos 계정으로 로그인하여 그래프와 음악 작업을 불러오세요.</div>', unsafe_allow_html=True)
        with st.form("cosmos_login_form", clear_on_submit=False):
            email = st.text_input("이메일", placeholder="name@example.com", key="login_email")
            password = st.text_input("비밀번호", type="password", placeholder="비밀번호", key="login_password")
            submitted = st.form_submit_button("로그인", use_container_width=True)
        if submitted:
            email_value = email.strip().lower()
            if not email_value or not password:
                st.error("이메일과 비밀번호를 모두 입력해 주세요.")
            else:
                endpoint = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
                body = {"email": email_value, "password": password}
                request = urllib.request.Request(endpoint, data=json.dumps(body).encode("utf-8"), headers={
                    "Content-Type": "application/json", "apikey": SUPABASE_ANON_KEY,
                    "Authorization": f"Bearer {SUPABASE_ANON_KEY}"}, method="POST")
                try:
                    with urllib.request.urlopen(request, timeout=20) as response:
                        result = json.loads(response.read().decode("utf-8"))
                    if result.get("access_token") and result.get("refresh_token"):
                        st.session_state["cosmos_supabase_session"] = {
                            "access_token": result["access_token"], "refresh_token": result["refresh_token"]}
                        st.success("로그인이 완료되었습니다. Cosmos로 이동합니다.")
                        st.switch_page("main.py")
                    else:
                        st.error("로그인 세션을 발급받지 못했습니다. 다시 시도해 주세요.")
                except urllib.error.HTTPError as exc:
                    try:
                        detail = json.loads(exc.read().decode("utf-8"))
                        message = detail.get("msg") or detail.get("message") or detail.get("error_description") or str(detail)
                    except Exception:
                        message = str(exc)
                    st.error(f"로그인 실패: {message}")
                except Exception as exc:
                    st.error(f"서버에 연결하지 못했습니다: {exc}")
    else:
        st.markdown('<div class="auth-title">회원가입</div>', unsafe_allow_html=True)
        st.markdown('<div class="auth-caption">계정을 만들면 그래프와 음악 작업을 계정에 연결할 수 있습니다.</div>', unsafe_allow_html=True)
        with st.form("cosmos_signup_form", clear_on_submit=False):
            display_name = st.text_input("이름", placeholder="사용할 이름", key="signup_display_name")
            email = st.text_input("이메일", placeholder="name@example.com", key="signup_email")
            password = st.text_input("비밀번호", type="password", placeholder="8자 이상", key="signup_password")
            password_confirm = st.text_input("비밀번호 확인", type="password", key="signup_password_confirm")
            submitted = st.form_submit_button("회원가입", use_container_width=True)
        if submitted:
            name = display_name.strip()
            email_value = email.strip().lower()
            if not name or not email_value or not password:
                st.error("이름, 이메일, 비밀번호를 모두 입력해 주세요.")
            elif len(password) < 8:
                st.error("비밀번호는 8자 이상이어야 합니다.")
            elif password != password_confirm:
                st.error("비밀번호 확인이 일치하지 않습니다.")
            else:
                endpoint = f"{SUPABASE_URL}/auth/v1/signup"
                body = {"email": email_value, "password": password, "data": {"display_name": name}}
                request = urllib.request.Request(endpoint, data=json.dumps(body).encode("utf-8"), headers={
                    "Content-Type": "application/json", "apikey": SUPABASE_ANON_KEY,
                    "Authorization": f"Bearer {SUPABASE_ANON_KEY}"}, method="POST")
                try:
                    with urllib.request.urlopen(request, timeout=20) as response:
                        result = json.loads(response.read().decode("utf-8"))
                    if result.get("access_token") and result.get("refresh_token"):
                        st.session_state["cosmos_supabase_session"] = {
                            "access_token": result["access_token"], "refresh_token": result["refresh_token"]}
                        st.success("회원가입이 완료되었습니다. Cosmos로 이동합니다.")
                        st.switch_page("main.py")
                    else:
                        st.info("계정이 생성되었습니다. 이메일 인증이 설정되어 있다면 인증 후 로그인해 주세요.")
                except urllib.error.HTTPError as exc:
                    try:
                        detail = json.loads(exc.read().decode("utf-8"))
                        message = detail.get("msg") or detail.get("message") or detail.get("error_description") or str(detail)
                    except Exception:
                        message = str(exc)
                    st.error(f"회원가입 실패: {message}")
                except Exception as exc:
                    st.error(f"서버에 연결하지 못했습니다: {exc}")
    if st.button("그래핑 계산기로 돌아가기", key="back_to_cosmos", use_container_width=True):
        st.switch_page("main.py")
