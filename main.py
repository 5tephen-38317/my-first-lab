import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos | 그래핑 계산기",
    page_icon="✿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Cosmos 그래프 + 오디오 추적 단일 화면
# Streamlit 기본 여백을 제거해 계산기 화면을 넓게 표시합니다.
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: #ffffff !important;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe { border: 0 !important; }
</style>
""", unsafe_allow_html=True)

# CLOUD SYNC SETUP (required for cross-device accounts):
# 1) Create a Supabase project and copy Project URL + anon/public key.
# 2) Replace SUPABASE_URL and SUPABASE_ANON_KEY in the HTML JavaScript below.
# 3) Run this SQL in Supabase SQL Editor:
# create table public.cosmos_workspaces (
#   user_id uuid primary key references auth.users(id) on delete cascade,
#   payload jsonb not null default '{}'::jsonb,
#   updated_at timestamptz not null default now()
# );
# alter table public.cosmos_workspaces enable row level security;
# create policy "Users can read own workspace" on public.cosmos_workspaces
#   for select to authenticated using (auth.uid() = user_id);
# create policy "Users can insert own workspace" on public.cosmos_workspaces
#   for insert to authenticated with check (auth.uid() = user_id);
# create policy "Users can update own workspace" on public.cosmos_workspaces
#   for update to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);

HTML = r"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmos | 그래핑 계산기</title>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Math.js CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            overflow: hidden;
            user-select: none;
            -webkit-user-select: none;
        }

        /* Cosmos Keypad Button Styling */
        .key-btn {
            background-color: #f1f3f4;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-family: 'Inter', system-ui, sans-serif;
            font-size: 13px;
            font-weight: 500;
            color: #202124;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.08s ease;
            box-shadow: 0 1px 1px rgba(0,0,0,0.05);
        }
        .key-btn:hover {
            background-color: #e8eaed;
            border-color: #bdc1c6;
        }
        .key-btn:active {
            background-color: #d2d6da;
            transform: translateY(1px);
        }
        .key-btn-dark {
            background-color: #dadce0;
            color: #3c4043;
            font-weight: 600;
        }
