import json
import urllib.error
import urllib.request

import streamlit as st

st.set_page_config(
    page_title="Cosmos | 회원가입",
    page_icon="✿",
    layout="centered"
)

SUPABASE_URL = "https://mkvlgqcrgpqsmrlmuvjx.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_QhXwfPy9tfGK06BAWn24og_RE2chtR8"

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: #f7f8fa;
    }
    .block-container {
        max-width: 520px;
        padding-top: 3rem;
    }
    h1 {
        letter-spacing: -1px;
    }
</style>
""", unsafe_allow_html=True)

st.title("cosmos")
st.subheader("회원가입")
st.caption("계정을 만들면 그래프와 음악 작업을 계정에 연결할 수 있습니다.")

if st.session_state.get("cosmos_supabase_session"):
    st.success("이미 회원가입 또는 로그인이 완료된 세션이 있습니다.")
    if st.button("Cosmos 그래핑 계산기로 돌아가기", use_container_width=True):
        st.switch_page("main.py")

with st.form("cosmos_signup_form", clear_on_submit=False):
    display_name = st.text_input("이름", placeholder="사용할 이름")
    email = st.text_input("이메일", placeholder="name@example.com")
    password = st.text_input("비밀번호", type="password", placeholder="8자 이상")
    password_confirm = st.text_input("비밀번호 확인", type="password")
    submitted = st.form_submit_button("회원가입", use_container_width=True, type="primary")

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
        body = {
            "email": email_value,
            "password": password,
            "data": {"display_name": name}
        }
        request = urllib.request.Request(
            endpoint,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "apikey": SUPABASE_ANON_KEY,
                "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                result = json.loads(response.read().decode("utf-8"))

            if result.get("access_token") and result.get("refresh_token"):
                st.session_state["cosmos_supabase_session"] = {
                    "access_token": result["access_token"],
                    "refresh_token": result["refresh_token"],
                }
                st.success("회원가입이 완료되었습니다. Cosmos로 이동합니다.")
                st.switch_page("main.py")
            else:
                st.warning(
                    "계정은 생성됐지만 즉시 로그인 세션은 발급되지 않았습니다. "
                    "Supabase의 Authentication → Providers → Email에서 "
                    "Confirm email 설정을 확인해 주세요."
                )
        except urllib.error.HTTPError as exc:
            try:
                detail = json.loads(exc.read().decode("utf-8"))
                message = (
                    detail.get("msg")
                    or detail.get("message")
                    or detail.get("error_description")
                    or str(detail)
                )
            except Exception:
                message = str(exc)
            st.error(f"회원가입 실패: {message}")
        except Exception as exc:
            st.error(f"서버에 연결하지 못했습니다: {exc}")

st.divider()
if st.button("메인 그래핑 계산기로 돌아가기", use_container_width=True):
    st.switch_page("main.py")
