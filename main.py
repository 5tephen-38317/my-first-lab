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

HTML = r"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmos | 그래핑 계산기</title>
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
        .key-btn-dark:hover {
            background-color: #bdc1c6;
        }
        .key-btn-blue {
            background-color: #2b72ee;
            color: white;
            border-color: #1a62e0;
            font-weight: 600;
        }
        .key-btn-blue:hover {
            background-color: #1a62e0;
        }

        /* Cosmos Audio Trace Panel Button Styling */
        .audio-btn {
            background-color: #ffffff;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 500;
            color: #3c4043;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.1s;
        }
        .audio-btn:hover {
            background-color: #f8f9fa;
            border-color: #bdc1c6;
        }
        .audio-btn:active {
            background-color: #e8eaed;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #f8f9fa;
        }
        ::-webkit-scrollbar-thumb {
            background: #dadce0;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #bdc1c6;
        }

        .color-popover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border: 1px solid #dadce0;
        }
    
        /* Desmos-inspired light calculator skin */
        body { background:#fff !important; color:#222 !important; }
        header { background:#222 !important; }
        #expressions-list, .expression-list { background:#fff !important; }
        input, select, textarea { color:#222; }
        .key-btn { background:#f1f1f1; border-color:#d1d1d1; color:#222; box-shadow:none; border-radius:3px; }
        .key-btn:hover { background:#e5e5e5; border-color:#bcbcbc; }
        .key-btn-blue { background:#3274d9; border-color:#2866c4; color:#fff; }
        .audio-btn { background:#fff; border-color:#d0d0d0; color:#333; }
        .audio-btn:hover { background:#f3f3f3; }
        .color-popover { background:#fff; }
    </style>
</head>
<body class="bg-white h-screen w-screen flex flex-col font-sans text-slate-800">

    <!-- 1. TOP NAVBAR -->
    <header class="bg-[#222222] text-white h-12 px-3 flex items-center justify-between z-30 shrink-0 select-none">
        <!-- Left Title and Save -->
        <div class="flex items-center space-x-2">
            <button onclick="showToast('폴더 목록을 불러왔습니다.')" class="p-1.5 hover:bg-[#3b3b3b] rounded text-slate-300 hover:text-white transition">
                <i class="fa-regular fa-folder text-base"></i>
            </button>
            <input id="graph-title-input" type="text" value="Cosmos 그래프" 
                   class="bg-transparent text-slate-100 text-sm font-medium px-2 py-1 rounded hover:bg-[#3b3b3b] focus:bg-[#303030] focus:outline-none border border-transparent focus:border-slate-600 transition w-36 sm:w-48">
            <button onclick="saveGraphState()" class="bg-[#2b72ee] hover:bg-blue-600 text-white text-xs font-semibold px-3 py-1.5 rounded transition shadow-sm">
                저장
            </button>
        </div>

        <!-- Center Logo -->
        <div class="absolute left-1/2 transform -translate-x-1/2 flex items-center cursor-pointer" onclick="resetView()">
            <span class="text-xl font-bold tracking-tight text-white font-serif italic">cosmos</span>
        </div>

        <!-- Right User Actions -->
        <div class="flex items-center space-x-1 sm:space-x-2">
            <span id="account-label" class="hidden text-xs text-slate-200 px-2"></span>
            <button id="login-nav-btn" onclick="openModal('login-modal')" class="text-xs font-medium px-3 py-1.5 rounded hover:bg-[#3b3b3b] transition">
                로그인
            </button>
            <button id="signup-nav-btn" onclick="openModal('signup-modal')" class="bg-[#2b72ee] hover:bg-blue-600 text-white text-xs font-semibold px-3 py-1.5 rounded transition shadow-sm">
                회원가입
            </button>
            <button id="logout-nav-btn" onclick="logoutAccount()" class="hidden text-xs font-medium px-3 py-1.5 rounded border border-slate-600 hover:bg-[#3b3b3b] transition">
                로그아웃
            </button>
            <div class="h-4 w-[1px] bg-slate-600 mx-1"></div>
            <button onclick="openModal('share-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-[#3b3b3b] rounded transition" title="공유">
                <i class="fa-solid fa-share-nodes text-sm"></i>
            </button>
            <button onclick="openModal('help-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-[#3b3b3b] rounded transition" title="도움말">
                <i class="fa-regular fa-circle-question text-sm"></i>
            </button>
            <button onclick="toggleAngleMode()" id="btn-lang-toggle" class="p-1.5 text-slate-300 hover:text-white hover:bg-[#3b3b3b] rounded transition text-xs font-semibold" title="각도 단위 전환 (라디안/각도)">
                Rad
            </button>
            <button onclick="openModal('settings-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-[#3b3b3b] rounded transition" title="설정">
                <i class="fa-solid fa-wrench text-sm"></i>
            </button>
        </div>
    </header>

    <!-- MAIN WORKSPACE -->
    <div class="flex-1 flex relative overflow-hidden">

        <!-- 2. LEFT SIDEBAR (EXPRESSIONS PANEL) -->
        <aside id="sidebar-panel" class="w-[340px] sm:w-[380px] bg-white border-r border-slate-300 flex flex-col z-20 transition-all duration-200 shrink-0">
            
            <!-- Sidebar Toolbar Header -->
            <div class="h-10 border-b border-slate-200 px-3 flex items-center justify-between bg-slate-50 shrink-0 relative">
                <div class="flex items-center space-x-1">
                    <!-- Add Item Menu Dropdown -->
                    <button id="btn-add-menu" onclick="toggleAddMenu()" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="항목 추가">
                        <i class="fa-solid fa-plus text-base"></i>
                    </button>
                    <!-- History Undo/Redo -->
                    <button onclick="undo()" id="btn-undo" class="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200/70 rounded transition" title="되돌리기">
                        <i class="fa-solid fa-rotate-left text-xs"></i>
                    </button>
                    <button onclick="redo()" id="btn-redo" class="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200/70 rounded transition" title="다시 실행">
                        <i class="fa-solid fa-rotate-right text-xs"></i>
                    </button>
                </div>

                <div class="flex items-center space-x-1">
                    <button onclick="showToast('편집 모드가 활성화되었습니다.')" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="수식 목록 편집">
                        <i class="fa-solid fa-gear text-sm"></i>
                    </button>
                    <button id="btn-collapse-sidebar" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="패널 숨기기">
                        <i class="fa-solid fa-angles-left text-sm"></i>
                    </button>
                </div>

                <!-- Add Menu Popover -->
                <div id="add-menu-popover" class="hidden absolute top-9 left-2 bg-white border border-slate-300 rounded-lg shadow-xl z-50 py-1 w-40 text-sm">
                    <button onclick="addExpression(''); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">
                        <i class="fa-solid fa-calculator text-blue-600 text-xs"></i>
                        <span>수식 (Expression)</span>
                    </button>
                    <button onclick="addTableItem(); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">
                        <i class="fa-solid fa-table text-emerald-600 text-xs"></i>
                        <span>표 (Table)</span>
                    </button>
                    <button onclick="addNoteItem(); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">
                        <i class="fa-regular fa-note-sticky text-amber-600 text-xs"></i>
                        <span>주석 (Note)</span>
                    </button>
                </div>
            </div>

            <!-- Expressions Scrollable List -->
            <div id="expressions-list" class="flex-1 overflow-y-auto divide-y divide-slate-100">
                <!-- Dynamically populated math items -->
            </div>
        </aside>

        <!-- Sidebar Re-open Floating Button -->
        <button id="btn-expand-sidebar" class="hidden absolute top-3 left-3 z-30 bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 p-2 rounded-lg shadow-md transition">
            <i class="fa-solid fa-angles-right text-sm"></i>
        </button>

        <!-- 3. GRAPH CANVAS ENGINE -->
        <main class="flex-1 relative bg-white overflow-hidden flex flex-col">
            <canvas id="graph-canvas" class="w-full h-full block cursor-crosshair"></canvas>

            <!-- Top Right Graph Controls -->
            <div class="absolute top-3 right-3 flex flex-col bg-white border border-slate-300 rounded-lg shadow-md overflow-hidden z-10 text-slate-700">
                <button onclick="openModal('settings-modal')" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="그래프 설정">
                    <i class="fa-solid fa-wrench text-xs"></i>
                </button>
                <button onclick="zoomIn()" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="확대">
                    <i class="fa-solid fa-plus text-xs"></i>
                </button>
                <button onclick="zoomOut()" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="축소">
                    <i class="fa-solid fa-minus text-xs"></i>
                </button>
                <button onclick="resetView()" class="p-2.5 hover:bg-slate-100 transition" title="기본 보기로 돌아가기">
                    <i class="fa-solid fa-house text-xs"></i>
                </button>
            </div>

            <!-- Hover / Pinned Point Label Overlay -->
            <div id="point-tooltip" class="pointer-events-none absolute hidden bg-slate-900/90 text-white text-xs px-2.5 py-1 rounded shadow-lg z-20 font-mono -translate-x-1/2 -translate-y-full mb-2">
                <span id="tooltip-coords">(0, 0)</span>
            </div>
        </main>
    </div>

    <!-- 4. BOTTOM KEYPAD & AUDIO TRACE CONTROLS PANEL -->
    <div id="bottom-panel" class="bg-[#e8eaed] border-t border-slate-300 z-30 flex flex-col shrink-0 select-none shadow-2xl transition-all duration-200">
        
        <!-- Tab Header Selector: Math Keyboard vs Audio Trace -->
        <div class="h-8 bg-[#dadce0] px-3 flex items-center justify-between text-xs text-slate-600 border-b border-slate-300">
            <div class="flex items-center space-x-2">
                <button id="tab-btn-keypad" onclick="switchBottomTab('keypad')" class="px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition">
                    가상 키보드
                </button>
                <button id="tab-btn-audio" onclick="switchBottomTab('audio')" class="px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition flex items-center space-x-1">
                    <i class="fa-solid fa-volume-high text-xs text-blue-600"></i>
                    <span>오디오 추적 (Audio Trace)</span>
                </button>
            </div>
            <button id="btn-hide-bottom-panel" class="hover:text-slate-900 transition p-1">
                <i class="fa-solid fa-chevron-down text-xs"></i>
            </button>
        </div>

        <!-- TAB 1: VIRTUAL MATH KEYBOARD -->
        <div id="keypad-tab-content" class="p-2 max-w-5xl mx-auto w-full grid grid-cols-12 gap-1.5 h-44 sm:h-48 text-sm">
            <!-- Col 1-4: Variables & Math Symbols -->
            <div class="col-span-4 grid grid-cols-4 gap-1">
                <button class="key-btn" onclick="insertKey('x')"><i>x</i></button>
                <button class="key-btn" onclick="insertKey('y')"><i>y</i></button>
                <button class="key-btn" onclick="insertKey('^2')"><i>a</i>²</button>
                <button class="key-btn" onclick="insertKey('^')"><i>a</i><sup><i>b</i></sup></button>

                <button class="key-btn" onclick="insertKey('(')">(</button>
                <button class="key-btn" onclick="insertKey(')')">)</button>
                <button class="key-btn" onclick="insertKey('<')">&lt;</button>
                <button class="key-btn" onclick="insertKey('>')">&gt;</button>

                <button class="key-btn" onclick="insertKey('|')">|<i>a</i>|</button>
                <button class="key-btn" onclick="insertKey(',')">,</button>
                <button class="key-btn" onclick="insertKey('<=')">≤</button>
                <button class="key-btn" onclick="insertKey('>=')">≥</button>

                <button class="key-btn key-btn-dark" onclick="insertKey('a')"><i>a</i></button>
                <button class="key-btn key-btn-dark" onclick="insertKey('b')"><i>b</i></button>
                <button class="key-btn" onclick="insertKey('sqrt(')">√</button>
                <button class="key-btn" onclick="insertKey('pi')">π</button>
            </div>

            <!-- Col 5-8: Standard Numpad -->
            <div class="col-span-4 grid grid-cols-4 gap-1">
                <button class="key-btn font-bold bg-white" onclick="insertKey('7')">7</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('8')">8</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('9')">9</button>
                <button class="key-btn key-btn-dark text-base" onclick="insertKey('/')">÷</button>

                <button class="key-btn font-bold bg-white" onclick="insertKey('4')">4</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('5')">5</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('6')">6</button>
                <button class="key-btn key-btn-dark text-base" onclick="insertKey('*')">×</button>

                <button class="key-btn font-bold bg-white" onclick="insertKey('1')">1</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('2')">2</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('3')">3</button>
                <button class="key-btn key-btn-dark text-base" onclick="insertKey('-')">-</button>

                <button class="key-btn font-bold bg-white" onclick="insertKey('0')">0</button>
                <button class="key-btn font-bold bg-white" onclick="insertKey('.')">.</button>
                <button class="key-btn key-btn-dark text-base" onclick="insertKey('=')">=</button>
                <button class="key-btn key-btn-dark text-base" onclick="insertKey('+')">+</button>
            </div>

            <!-- Col 9-12: Functions & Actions -->
            <div class="col-span-4 grid grid-cols-3 gap-1">
                <button class="key-btn key-btn-dark" onclick="insertKey('sin(')">sin</button>
                <button class="key-btn key-btn-dark" onclick="moveCursor(-1)"><i class="fa-solid fa-arrow-left text-xs"></i></button>
                <button class="key-btn key-btn-dark" onclick="moveCursor(1)"><i class="fa-solid fa-arrow-right text-xs"></i></button>

                <button class="key-btn" onclick="insertKey('cos(')">cos</button>
                <button class="key-btn" onclick="insertKey('tan(')">tan</button>
                <button class="key-btn key-btn-dark" onclick="handleBackspace()"><i class="fa-solid fa-delete-left text-sm"></i></button>

                <button class="key-btn" onclick="insertKey('log(')">log</button>
                <button class="key-btn" onclick="insertKey('ln(')">ln</button>
                <button class="key-btn key-btn-blue row-span-2" onclick="handleEnter()">↵</button>

                <button class="key-btn" onclick="insertKey('e')"><i>e</i></button>
                <button class="key-btn" onclick="insertKey('abs(')">abs</button>
            </div>
        </div>

        <!-- TAB 2: COSMOS AUDIO TRACE PANEL -->
        <div id="audio-tab-content" class="hidden p-3 w-full flex-col space-y-3 max-h-72 overflow-y-auto">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
                
                <!-- Section 1: Audio Playback Controls -->
                <div class="flex flex-col space-y-2 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">
                    <button id="btn-audio-play" onclick="toggleAudioPlayback()" class="w-full bg-[#2b72ee] hover:bg-blue-600 text-white font-semibold py-2 px-3 rounded flex items-center justify-center space-x-2 shadow transition">
                        <i id="audio-play-icon" class="fa-solid fa-play text-xs"></i>
                        <span id="audio-play-text">그래프 듣기</span>
                    </button>
                    
                    <div class="grid grid-cols-2 gap-2 text-[11px]">
                        <label class="flex flex-col gap-1 text-slate-600">볼륨 <span id="audio-vol-text" class="font-semibold text-slate-800">50%</span>
                            <input id="audio-volume-range" type="range" min="0" max="1" step="0.01" value="0.5" class="w-full accent-blue-600" aria-label="오디오 볼륨">
                        </label>
                        <label class="flex flex-col gap-1 text-slate-600">재생 속도 <span id="audio-speed-text" class="font-semibold text-slate-800">1.00×</span>
                            <input id="audio-speed-range" type="range" min="0.25" max="3" step="0.05" value="1" class="w-full accent-blue-600" aria-label="오디오 재생 속도">
                        </label>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-[11px]">
                        <label class="flex flex-col gap-1 text-slate-600">추적 대상
                            <select id="audio-track-mode" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800">
                                <option value="active">선택한 함수</option><option value="visible">표시 중인 함수 전체</option>
                            </select>
                        </label>
                        <label class="flex flex-col gap-1 text-slate-600">음색
                            <select id="audio-waveform" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800">
                                <option value="sine">부드러운 사인파</option><option value="triangle">삼각파</option><option value="sawtooth">톱니파</option><option value="square">사각파</option>
                            </select>
                        </label>
                    </div>
                    <div class="rounded-lg border border-slate-200 bg-slate-50 p-3 space-y-2">
                        <div class="flex items-center justify-between"><strong class="text-sm text-slate-800">음악 만들기</strong><span class="text-[10px] text-slate-500">그래프 + 반주</span></div>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-[11px]">
                            <label class="flex flex-col gap-1 text-slate-600">BPM <span id="music-bpm-value" class="font-semibold">100</span><input id="music-bpm" type="range" min="50" max="180" value="100" step="1" class="w-full accent-blue-600"></label>
                            <label class="flex flex-col gap-1 text-slate-600">스타일<select id="music-genre" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800"><option value="pop">Pop</option><option value="kpop">K-pop</option><option value="jpop">J-pop</option><option value="lofi">Lo-fi</option><option value="edm">EDM</option><option value="classic">Classic</option><option value="phonk">Phonk</option><option value="funk">Funk</option></select></label>
                            <label class="flex flex-col gap-1 text-slate-600">조성<select id="music-key" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800"><option value="0">C 메이저 / A 마이너</option><option value="2">D 메이저</option><option value="4">E 메이저</option><option value="5">F 메이저</option><option value="7">G 메이저</option><option value="9">A 메이저</option></select></label>
                            <label class="flex flex-col gap-1 text-slate-600">음계<select id="music-scale" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800"><option value="major">메이저</option><option value="minor">마이너</option><option value="pentatonic">펜타토닉</option><option value="chromatic">반음계</option></select></label>
                        </div>
                        <div class="grid grid-cols-2 md:grid-cols-5 gap-2 text-xs text-slate-700">
                            <label><input type="checkbox" id="part-melody" checked> 멜로디</label><label><input type="checkbox" id="part-bass" checked> 베이스</label><label><input type="checkbox" id="part-chords" checked> 코드</label><label><input type="checkbox" id="part-arp"> 아르페지오</label><label><input type="checkbox" id="part-drums" checked> 드럼/타악기</label>
                        </div>
                        <div id="audio-layer-volumes" class="space-y-1 text-[11px]"></div>
                        <div class="flex flex-wrap gap-2 items-center"><input id="music-song-name" type="text" placeholder="곡 이름" class="border border-slate-300 rounded px-2 py-1 text-xs w-28"><button onclick="saveMusicPreset()" class="audio-btn px-2 py-1.5">곡 저장</button><select id="music-library-select" class="border border-slate-300 rounded px-2 py-1 text-xs bg-white"><option value="">저장한 곡 불러오기</option></select><button onclick="loadMusicPreset()" class="audio-btn px-2 py-1.5">불러오기</button></div>
                        <div class="flex flex-wrap gap-2"><button onclick="playGraphMusic()" class="audio-btn px-3 py-1.5"><i class="fa-solid fa-music mr-1"></i>음악 재생</button><button onclick="stopGraphMusic()" class="audio-btn px-3 py-1.5"><i class="fa-solid fa-stop mr-1"></i>음악 정지</button><span id="music-status" class="self-center text-[11px] text-slate-500">그래프 추적과 음악을 함께 재생할 수 있어요.</span></div>
                    </div>
                    <div class="grid grid-cols-3 gap-2 text-[11px]">
                        <label class="flex flex-col gap-1 text-slate-600">시작 x
                            <input id="audio-x-start" type="number" value="-10" step="0.5" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 text-slate-800">
                        </label>
                        <label class="flex flex-col gap-1 text-slate-600">끝 x
                            <input id="audio-x-end" type="number" value="10" step="0.5" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 text-slate-800">
                        </label>
                        <label class="flex flex-col gap-1 text-slate-600">재생 시간
                            <select id="audio-duration" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 bg-white text-slate-800">
                                <option value="15">15초</option><option value="30" selected>30초</option><option value="60">1분</option><option value="120">2분</option><option value="180">3분</option>
                            </select>
                        </label>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="restartAudioTrace()" class="audio-btn px-2 py-1.5 flex-1"><i class="fa-solid fa-rotate-left mr-1"></i>처음부터</button>
                        <button onclick="stopAudioTrace()" class="audio-btn px-2 py-1.5 flex-1"><i class="fa-solid fa-stop mr-1"></i>정지</button>
                    </div>
                    <label class="block text-[11px] text-slate-600">재생 위치 <span id="audio-progress-text" class="font-semibold text-slate-800">x = -10.00</span>
                        <input id="audio-progress" type="range" min="0" max="1000" step="1" value="0" class="w-full accent-blue-600">
                    </label>
                    <div id="audio-note-readout" class="rounded bg-slate-50 border border-slate-200 px-2 py-1.5 text-[11px] text-slate-600">음높이: 대기 중 · 추적 점: 대기 중</div>
                    <button id="btn-audio-trace-status" class="w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center">
                        오디오 추적 꺼짐
                    </button>
                </div>

                <!-- Section 2: Point & Curve Navigation -->
                <div class="flex flex-col space-y-2 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">
                    <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider text-center">내비게이션</span>
                    
                    <div class="grid grid-cols-3 gap-1 items-center text-center text-xs">
                        <button onclick="navigatePoint(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-chevron-left"></i></button>
                        <span class="font-medium text-slate-700">점</span>
                        <button onclick="navigatePoint(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-chevron-right"></i></button>

                        <button onclick="navigateInterest(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-angles-left"></i></button>
                        <span class="font-medium text-slate-700">관심지점</span>
                        <button onclick="navigateInterest(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-angles-right"></i></button>

                        <button onclick="navigateCurve(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-caret-up"></i></button>
                        <span class="font-medium text-slate-700">곡선</span>
                        <button onclick="navigateCurve(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-caret-down"></i></button>
                    </div>
                </div>

                <!-- Section 3: Screen Reader Speech Accessibility -->
                <div class="flex flex-col space-y-1.5 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">스크린 리더</span>
                        <i class="fa-solid fa-circle-info text-slate-400 text-xs" title="웹 음성합성 API 지원"></i>
                    </div>

                    <button onclick="speakDescription('point')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">
                        점 설명
                    </button>
                    <button onclick="speakDescription('curve')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">
                        곡선 설명
                    </button>
                    <button onclick="speakDescription('axis')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">
                        축 설명
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Toggle Bottom Panel Floating Button -->
    <button id="btn-toggle-bottom" class="fixed bottom-2 left-2 z-40 bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 px-2.5 py-1.5 rounded-lg shadow-md flex items-center space-x-1.5 text-xs font-medium transition">
        <i class="fa-solid fa-keyboard"></i>
        <i class="fa-solid fa-caret-down text-[10px]"></i>
    </button>

    <!-- Color / Style Picker Popover Modal -->
    <div id="color-popover" class="hidden absolute z-50 bg-white rounded-lg p-2.5 color-popover flex flex-col space-y-2">
        <div class="flex items-center space-x-2">
            <button onclick="setColorForSelected('#c74440')" class="w-6 h-6 rounded-full bg-[#c74440] hover:scale-110 transition"></button>
            <button onclick="setColorForSelected('#2d70b3')" class="w-6 h-6 rounded-full bg-[#2d70b3] hover:scale-110 transition"></button>
            <button onclick="setColorForSelected('#388c46')" class="w-6 h-6 rounded-full bg-[#388c46] hover:scale-110 transition"></button>
            <button onclick="setColorForSelected('#6042a6')" class="w-6 h-6 rounded-full bg-[#6042a6] hover:scale-110 transition"></button>
            <button onclick="setColorForSelected('#000000')" class="w-6 h-6 rounded-full bg-black hover:scale-110 transition"></button>
        </div>
        <div class="h-[1px] bg-slate-200 w-full"></div>
        <div class="flex items-center justify-between text-xs text-slate-600">
            <button onclick="setStyleForSelected('solid')" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium">실선</button>
            <button onclick="setStyleForSelected('dashed')" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium">점선</button>
        </div>
    </div>

    <!-- MODAL DIALOGS -->
    <div id="modal-backdrop" class="hidden fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
        
        <!-- Login Modal -->
        <div id="login-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-sm w-full p-6 flex flex-col space-y-4" role="dialog" aria-modal="true" aria-labelledby="login-heading">
            <div class="flex justify-between items-center">
                <h3 id="login-heading" class="text-lg font-bold text-slate-800">Cosmos 로그인</h3>
                <button onclick="closeModal()" aria-label="닫기" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <p class="text-xs text-slate-500">이 브라우저에서 가입한 계정으로 로그인합니다.</p>
            <form onsubmit="loginAccount(event)" class="flex flex-col space-y-3">
                <label class="text-xs font-semibold text-slate-600">이메일</label>
                <input id="login-email" type="email" autocomplete="username" required placeholder="name@example.com" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <label class="text-xs font-semibold text-slate-600">비밀번호</label>
                <input id="login-password" type="password" autocomplete="current-password" required placeholder="비밀번호" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <p id="login-error" class="hidden text-xs text-red-600" role="alert"></p>
                <button type="submit" class="w-full bg-[#2b72ee] text-white py-2 rounded font-semibold text-sm hover:bg-blue-600 transition">로그인</button>
            </form>
            <button onclick="openModal('signup-modal')" class="text-xs text-blue-600 hover:underline">아직 계정이 없나요? 회원가입</button>
        </div>

        <!-- Signup Modal -->
        <div id="signup-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-sm w-full p-6 flex flex-col space-y-4" role="dialog" aria-modal="true" aria-labelledby="signup-heading">
            <div class="flex justify-between items-center">
                <h3 id="signup-heading" class="text-lg font-bold text-slate-800">Cosmos 계정 만들기</h3>
                <button onclick="closeModal()" aria-label="닫기" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <p class="text-xs text-slate-500">데모 계정은 현재 사용 중인 브라우저에만 저장됩니다.</p>
            <form onsubmit="signupAccount(event)" class="flex flex-col space-y-3">
                <label class="text-xs font-semibold text-slate-600">이름</label>
                <input id="signup-name" type="text" autocomplete="name" required maxlength="40" placeholder="이름" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <label class="text-xs font-semibold text-slate-600">이메일</label>
                <input id="signup-email" type="email" autocomplete="email" required placeholder="name@example.com" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <label class="text-xs font-semibold text-slate-600">비밀번호 (8자 이상)</label>
                <input id="signup-password" type="password" autocomplete="new-password" minlength="8" required placeholder="8자 이상 입력" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <label class="text-xs font-semibold text-slate-600">비밀번호 확인</label>
                <input id="signup-confirm" type="password" autocomplete="new-password" minlength="8" required placeholder="비밀번호 다시 입력" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">
                <p id="signup-error" class="hidden text-xs text-red-600" role="alert"></p>
                <button type="submit" class="w-full bg-[#2b72ee] text-white py-2 rounded font-semibold text-sm hover:bg-blue-600 transition">회원가입</button>
            </form>
            <button onclick="openModal('login-modal')" class="text-xs text-blue-600 hover:underline">이미 계정이 있나요? 로그인</button>
        </div>

        <!-- Share Modal -->
        <div id="share-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-4">
            <div class="flex justify-between items-center">
                <h3 class="text-lg font-bold text-slate-800">그래프 공유</h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <p class="text-xs text-slate-500">그래프 주소를 복사하거나 링크를 공유하세요.</p>
            <div class="flex items-center space-x-2">
                <input id="share-url-input" readonly value="" placeholder="배포 후 공유 주소가 여기에 표시됩니다" class="flex-1 border border-slate-300 rounded px-3 py-2 text-xs bg-slate-50 font-mono">
                <button onclick="copyShareUrl()" class="bg-slate-800 text-white px-3 py-2 rounded text-xs font-semibold hover:bg-slate-700 transition">복사</button>
            </div>
        </div>

        <!-- Settings Modal -->
        <div id="settings-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-4">
            <div class="flex justify-between items-center">
                <h3 class="text-lg font-bold text-slate-800">그래프 설정</h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <div class="space-y-3 text-sm">
                <div class="flex justify-between items-center">
                    <span class="text-slate-700 font-medium">각도 단위</span>
                    <div class="flex border border-slate-300 rounded overflow-hidden">
                        <button id="set-rad-btn" onclick="setAngleUnit('rad')" class="px-3 py-1 bg-blue-600 text-white font-semibold text-xs">라디안 (Radians)</button>
                        <button id="set-deg-btn" onclick="setAngleUnit('deg')" class="px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs">각도 (Degrees)</button>
                    </div>
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-slate-700 font-medium">그리드 표시</span>
                    <input type="checkbox" id="chk-grid" checked onchange="toggleGrid(this.checked)" class="w-4 h-4 text-blue-600">
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-slate-700 font-medium">축 번호 표시</span>
                    <input type="checkbox" id="chk-numbers" checked onchange="toggleNumbers(this.checked)" class="w-4 h-4 text-blue-600">
                </div>
            </div>
        </div>

        <!-- Help Modal -->
        <div id="help-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-3">
            <div class="flex justify-between items-center">
                <h3 class="text-lg font-bold text-slate-800">도움말 및 수식 안내</h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="text-xs text-slate-600 space-y-2 leading-relaxed">
                <p>• <b>함수 입력예시:</b> <code class="bg-slate-100 px-1 py-0.5 rounded">y = sin(x)</code>, <code class="bg-slate-100 px-1 py-0.5 rounded">y = x^2 - 4</code>, <code class="bg-slate-100 px-1 py-0.5 rounded">y = 2*x + 1</code></p>
                <p>• <b>변수 슬라이더:</b> 수식에 <code class="bg-slate-100 px-1 py-0.5 rounded">a</code> 또는 <code class="bg-slate-100 px-1 py-0.5 rounded">b</code>를 입력하면 슬라이더 조절바가 생성됩니다.</p>
                <p>• <b>오디오 추적:</b> 오디오 추적 탭에서 [그래프 듣기]를 클릭하면 음고와 스테레오 사운드로 그래프를 청각화합니다.</p>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div id="toast-msg" class="fixed bottom-12 right-4 z-50 bg-slate-800 text-white text-xs px-3 py-2 rounded-lg shadow-xl opacity-0 transition-opacity duration-300 pointer-events-none">
        알림 메시지
    </div>

    <!-- JAVASCRIPT APPLICATION LOGIC ENGINE -->
    <script>
        /**
         * Core Application State
         */
        const state = {
            scale: 60, // Screen pixels per math coordinate unit
            offsetX: 0,
            offsetY: 0,
            isDragging: false,
            dragStart: { x: 0, y: 0 },
            
            showGrid: true,
            showNumbers: true,
            angleUnit: 'rad', // 'rad' or 'deg'

            items: [], // Array of expressions / notes / tables
            variables: { a: 1, b: 2 }, // Active slider variables
            activeItemId: null,
            colorPopoverItemId: null,
            
            history: [],
            historyIdx: -1,

            // Audio Engine & Trace State
            audio: {
                ctx: null,
                masterGain: null,
                tracks: [],
                isPlaying: false,
                vol: 0.5,
                speed: 1,
                duration: 15,
                timer: null,
                startedAt: 0,
                elapsedBeforePause: 0,
                currX: -10,
                xStart: -10,
                xEnd: 10,
                waveform: 'sine',
                mode: 'active',
                lastFrameAt: 0,
                musicPlaying: false,
                lastMusicStep: -1,
                musicVolumes: { melody: 0.45, bass: 0.35, chords: 0.22, arp: 0.2, drums: 0.25 },
                musicNodes: []
            },

            // Interactive Snap Points
            snapPoints: [],
            pinnedPoints: [],
            activeHoverPoint: null,
            navPointIdx: 0
        };

        const PALETTE = ['#c74440', '#2d70b3', '#388c46', '#6042a6', '#000000'];
        let colorIndex = 0;
        function getNextColor() {
            return PALETTE[colorIndex++ % PALETTE.length];
        }

        /**
         * DOM Elements Initialization
         */
        const canvas = document.getElementById('graph-canvas');
        const ctx = canvas.getContext('2d');
        const expressionsList = document.getElementById('expressions-list');
        const bottomPanel = document.getElementById('bottom-panel');
        const btnToggleBottom = document.getElementById('btn-toggle-bottom');
        const btnHideBottomPanel = document.getElementById('btn-hide-bottom-panel');
        const sidebarPanel = document.getElementById('sidebar-panel');
        const btnCollapseSidebar = document.getElementById('btn-collapse-sidebar');
        const btnExpandSidebar = document.getElementById('btn-expand-sidebar');
        const tooltip = document.getElementById('point-tooltip');
        const tooltipCoords = document.getElementById('tooltip-coords');
        const colorPopover = document.getElementById('color-popover');

        /**
         * Canvas Auto-Resizer Engine
         */
        function resizeCanvas() {
            const rect = canvas.parentElement.getBoundingClientRect();
            const dpr = window.devicePixelRatio || 1;
            canvas.width = Math.max(1, Math.round(rect.width * dpr));
            canvas.height = Math.max(1, Math.round(rect.height * dpr));
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            render();
        }
        window.addEventListener('resize', resizeCanvas);

        /**
         * Coordinate Transformations
         */
        function mathToScreen(x, y) {
            const width = canvas.width / window.devicePixelRatio;
            const height = canvas.height / window.devicePixelRatio;
            const centerX = width / 2 + state.offsetX;
            const centerY = height / 2 + state.offsetY;
            return {
                x: centerX + x * state.scale,
                y: centerY - y * state.scale
            };
        }

        function screenToMath(px, py) {
            const width = canvas.width / window.devicePixelRatio;
            const height = canvas.height / window.devicePixelRatio;
            const centerX = width / 2 + state.offsetX;
            const centerY = height / 2 + state.offsetY;
            return {
                x: (px - centerX) / state.scale,
                y: (centerY - py) / state.scale
            };
        }

        /**
         * Rendering Engine: Grid, Functions, Snap Points, Tables
         */
        function render() {
            const width = canvas.width / window.devicePixelRatio;
            const height = canvas.height / window.devicePixelRatio;

            ctx.fillStyle = '#ffffff';
            ctx.fillRect(0, 0, width, height);

            if (state.showGrid) {
                drawGrid(width, height);
            }

            state.snapPoints = []; // Reset snap points for current frame

            // Render Function Curves & Tables
            state.items.forEach(item => {
                if (item.visible) {
                    if (item.type === 'expression' && item.compiled) {
                        drawFunction(item, width, height);
                    } else if (item.type === 'table') {
                        drawTablePoints(item);
                    }
                }
            });

            // Draw Computed Snap Points (Gray Dots)
            drawSnapPoints();

            // Draw Pinned Coordinate Labels
            drawPinnedPoints();

            // Audio trace playhead guide and active point
            if (state.activeHoverPoint && state.activeHoverPoint.audioTrace) {
                const width = canvas.width / (window.devicePixelRatio || 1);
                const height = canvas.height / (window.devicePixelRatio || 1);
                const guide = mathToScreen(state.activeHoverPoint.x, 0).x;
                ctx.save();
                ctx.strokeStyle = state.activeHoverPoint.color || '#2b72ee';
                ctx.globalAlpha = 0.25;
                ctx.setLineDash([4, 4]);
                ctx.beginPath(); ctx.moveTo(guide, 0); ctx.lineTo(guide, height); ctx.stroke();
                ctx.setLineDash([]); ctx.restore();
            }
            if (state.activeHoverPoint) drawActiveHoverMarker();
        }

        /**
         * Cosmos coordinate grid renderer
         */
        function drawGrid(width, height) {
            const centerX = width / 2 + state.offsetX;
            const centerY = height / 2 + state.offsetY;

            let unitStep = 1;
            const targetPixelStep = 80;
            const rawUnits = targetPixelStep / state.scale;
            const magnitude = Math.pow(10, Math.floor(Math.log10(rawUnits)));
            const residual = rawUnits / magnitude;

            if (residual >= 5) unitStep = 5 * magnitude;
            else if (residual >= 2) unitStep = 2 * magnitude;
            else unitStep = 1 * magnitude;

            const stepPixels = unitStep * state.scale;

            // Minor Grid Lines
            ctx.lineWidth = 0.5;
            ctx.strokeStyle = '#e2e8f0';
            ctx.beginPath();
            const subStep = stepPixels / 5;
            for (let x = (centerX % subStep) - subStep; x < width; x += subStep) {
                ctx.moveTo(x, 0); ctx.lineTo(x, height);
            }
            for (let y = (centerY % subStep) - subStep; y < height; y += subStep) {
                ctx.moveTo(0, y); ctx.lineTo(width, y);
            }
            ctx.stroke();

            // Major Grid Lines
            ctx.lineWidth = 1;
            ctx.strokeStyle = '#cbd5e1';
            ctx.beginPath();
            for (let x = (centerX % stepPixels) - stepPixels; x < width; x += stepPixels) {
                ctx.moveTo(x, 0); ctx.lineTo(x, height);
            }
            for (let y = (centerY % stepPixels) - stepPixels; y < height; y += stepPixels) {
                ctx.moveTo(0, y); ctx.lineTo(width, y);
            }
            ctx.stroke();

            // Main Axes Lines
            ctx.lineWidth = 1.5;
            ctx.strokeStyle = '#334155';
            ctx.beginPath();
            ctx.moveTo(centerX, 0); ctx.lineTo(centerX, height);
            ctx.moveTo(0, centerY); ctx.lineTo(width, centerY);
            ctx.stroke();

            // Axis Number Labels
            if (state.showNumbers) {
                ctx.fillStyle = '#64748b';
                ctx.font = '12px Inter, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'top';

                const firstMathX = Math.ceil(-centerX / stepPixels) * unitStep;
                const lastMathX = Math.floor((width - centerX) / stepPixels) * unitStep;

                for (let mathX = firstMathX; mathX <= lastMathX; mathX += unitStep) {
                    if (Math.abs(mathX) < 1e-9) continue;
                    const screen = mathToScreen(mathX, 0);
                    const labelY = Math.min(Math.max(centerY + 6, 6), height - 20);
                    ctx.fillText(Number(mathX.toFixed(4)).toString(), screen.x, labelY);
                }

                ctx.textAlign = 'right';
                ctx.textBaseline = 'middle';
                const firstMathY = Math.ceil((centerY - height) / stepPixels) * unitStep;
                const lastMathY = Math.floor(centerY / stepPixels) * unitStep;

                for (let mathY = firstMathY; mathY <= lastMathY; mathY += unitStep) {
                    if (Math.abs(mathY) < 1e-9) continue;
                    const screen = mathToScreen(0, mathY);
                    const labelX = Math.min(Math.max(centerX - 8, 28), width - 8);
                    ctx.fillText(Number(mathY.toFixed(4)).toString(), labelX, screen.y);
                }
            }
        }

        /**
         * Mathematical Curve & Snap Point Evaluation
         */
        function drawFunction(item, width, height) {
            ctx.strokeStyle = item.color;
            ctx.lineWidth = 2.5;

            if (item.lineStyle === 'dashed') ctx.setLineDash([8, 6]);
            else ctx.setLineDash([]);

            ctx.beginPath();
            let isDrawing = false;
            const stepPx = 2;

            let prevY = null;
            let prevMathX = null;
            let prevSlope = null;

            const scope = { ...state.variables };

            for (let px = 0; px <= width; px += stepPx) {
                const mathX = screenToMath(px, 0).x;
                scope.x = mathX;

                try {
                    let yVal = item.compiled.evaluate(scope);
                    if (typeof yVal === 'object' && yVal.re !== undefined) yVal = yVal.re;

                    if (typeof yVal === 'number' && !isNaN(yVal) && isFinite(yVal)) {
                        const screen = mathToScreen(mathX, yVal);
                        
                        if (!isDrawing) {
                            ctx.moveTo(screen.x, screen.y);
                            isDrawing = true;
                        } else {
                            ctx.lineTo(screen.x, screen.y);
                        }

                        // Snap Points: X-Intercept
                        if (prevY !== null) {
                            const slope = (yVal - prevY) / (mathX - prevMathX);
                            
                            if ((prevY < 0 && yVal >= 0) || (prevY > 0 && yVal <= 0)) {
                                state.snapPoints.push({ x: mathX, y: yVal, color: item.color, type: 'intercept' });
                            }
                            // Min/Max Extrema
                            if (prevSlope !== null && ((prevSlope > 0 && slope < 0) || (prevSlope < 0 && slope > 0))) {
                                state.snapPoints.push({ x: prevMathX, y: prevY, color: item.color, type: 'extrema' });
                            }
                            prevSlope = slope;
                        }

                        // Y-Intercept
                        if (prevMathX !== null && prevMathX < 0 && mathX >= 0) {
                            scope.x = 0;
                            const yZero = item.compiled.evaluate(scope);
                            state.snapPoints.push({ x: 0, y: yZero, color: item.color, type: 'y-intercept' });
                        }

                        prevY = yVal;
                        prevMathX = mathX;
                    } else {
                        isDrawing = false;
                    }
                } catch (e) {
                    isDrawing = false;
                }
            }
            ctx.stroke();
            ctx.setLineDash([]);
        }

        /**
         * Render Table Coordinates & Scatter Points
         */
        function drawTablePoints(item) {
            item.rows.forEach(row => {
                if (row.x !== '' && row.y !== '') {
                    const mathX = parseFloat(row.x);
                    const mathY = parseFloat(row.y);
                    if (!isNaN(mathX) && !isNaN(mathY)) {
                        const screen = mathToScreen(mathX, mathY);
                        ctx.fillStyle = item.color;
                        ctx.beginPath();
                        ctx.arc(screen.x, screen.y, 5, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.strokeStyle = '#ffffff';
                        ctx.lineWidth = 1.5;
                        ctx.stroke();
                    }
                }
            });
        }

        /**
         * Draw Snap Dots & Pinned Coordinates
         */
        function drawSnapPoints() {
            state.snapPoints.forEach(pt => {
                const screen = mathToScreen(pt.x, pt.y);
                ctx.fillStyle = '#94a3b8';
                ctx.beginPath();
                ctx.arc(screen.x, screen.y, 4, 0, Math.PI * 2);
                ctx.fill();
            });
        }

        function drawPinnedPoints() {
            state.pinnedPoints.forEach(pt => {
                const screen = mathToScreen(pt.x, pt.y);
                ctx.fillStyle = pt.color || '#334155';
                ctx.beginPath();
                ctx.arc(screen.x, screen.y, 5, 0, Math.PI * 2);
                ctx.fill();

                // Draw Coordinate Box
                const text = `(${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`;
                ctx.font = '12px Inter, sans-serif';
                const textWidth = ctx.measureText(text).width;

                ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
                ctx.strokeStyle = '#cbd5e1';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.roundRect(screen.x - textWidth / 2 - 6, screen.y - 28, textWidth + 12, 20, 4);
                ctx.fill();
                ctx.stroke();

                ctx.fillStyle = '#1e293b';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(text, screen.x, screen.y - 18);
            });
        }

        function drawActiveHoverMarker() {
            const pt = state.activeHoverPoint;
            if (!pt || !Number.isFinite(pt.x) || !Number.isFinite(pt.y)) return;
            const screen = mathToScreen(pt.x, pt.y);
            const width = canvas.width / (window.devicePixelRatio || 1);
            const height = canvas.height / (window.devicePixelRatio || 1);
            if (screen.x < -20 || screen.x > width + 20 || screen.y < -20 || screen.y > height + 20) return;
            ctx.save();
            ctx.shadowColor = pt.color || '#2b72ee';
            ctx.shadowBlur = pt.audioTrace ? 18 : 8;
            ctx.fillStyle = pt.color || '#2b72ee';
            ctx.beginPath();
            ctx.arc(screen.x, screen.y, pt.audioTrace ? 7 : 6, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.stroke();
            if (pt.audioTrace) {
                ctx.strokeStyle = pt.color || '#2b72ee';
                ctx.globalAlpha = 0.45;
                ctx.lineWidth = 1.5;
                ctx.beginPath(); ctx.arc(screen.x, screen.y, 13, 0, Math.PI * 2); ctx.stroke();
            }
            ctx.restore();
        }

        /**
         * Expressions & Sidebar List Manager
         */
        function addExpression(rawText = '') {
            saveHistory();
            const item = {
                id: 'item_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
                type: 'expression',
                rawText: rawText,
                compiled: null,
                color: getNextColor(),
                lineStyle: 'solid',
                visible: true,
                error: false,
                hasSlider: false,
                varName: null
            };
            state.items.push(item);
            state.activeItemId = item.id;
            renderExpressionList();
            if (rawText) updateExpression(item.id, rawText);
        }

        function addTableItem() {
            saveHistory();
            const item = {
                id: 'item_' + Date.now(),
                type: 'table',
                color: getNextColor(),
                visible: true,
                rows: [
                    { x: '-2', y: '4' },
                    { x: '-1', y: '1' },
                    { x: '0', y: '0' },
                    { x: '1', y: '1' },
                    { x: '2', y: '4' }
                ]
            };
            state.items.push(item);
            renderExpressionList();
            render();
        }

        function addNoteItem() {
            saveHistory();
            const item = {
                id: 'item_' + Date.now(),
                type: 'note',
                text: '주석을 입력하세요...'
            };
            state.items.push(item);
            renderExpressionList();
        }

        function updateExpression(id, text) {
            const item = state.items.find(it => it.id === id);
            if (!item) return;

            item.rawText = text;
            if (!text.trim()) {
                item.compiled = null;
                item.error = false;
                item.hasSlider = false;
                render();
                return;
            }

            try {
                let expr = text;
                if (expr.includes('=')) {
                    expr = expr.split('=')[1].trim();
                }

                // Check for slider variables (e.g., 'a' or 'b')
                if (text.includes('a') && !state.variables.hasOwnProperty('a')) state.variables.a = 1;
                if (text.includes('b') && !state.variables.hasOwnProperty('b')) state.variables.b = 2;

                item.compiled = math.compile(expr);
                item.compiled.evaluate({ x: 1, ...state.variables });
                item.error = false;
            } catch (err) {
                item.compiled = null;
                item.error = true;
            }

            render();
        }

        function removeExpression(id) {
            saveHistory();
            state.items = state.items.filter(it => it.id !== id);
            if (state.activeItemId === id) {
                state.activeItemId = state.items.length > 0 ? state.items[0].id : null;
            }
            renderExpressionList();
            render();
        }

        function toggleVisibility(id) {
            const item = state.items.find(it => it.id === id);
            if (item) {
                item.visible = !item.visible;
                renderExpressionList();
                render();
            }
        }

        function updateVariableSlider(varName, value) {
            state.variables[varName] = parseFloat(value);
            document.getElementById(`slider-val-${varName}`).textContent = value;
            render();
        }

        function updateTableCell(itemId, rowIdx, col, val) {
            const item = state.items.find(it => it.id === itemId);
            if (item && item.rows[rowIdx]) {
                item.rows[rowIdx][col] = val;
                render();
            }
        }

        /**
         * Render Expression List in Sidebar
         */
        function renderExpressionList() {
            expressionsList.innerHTML = '';

            state.items.forEach((item, index) => {
                const el = document.createElement('div');
                el.className = `p-3 space-y-2 border-b border-slate-100 transition ${state.activeItemId === item.id ? 'bg-blue-50/50' : 'hover:bg-slate-50'}`;
                
                if (item.type === 'expression') {
                    el.innerHTML = `
                        <div class="flex items-center space-x-2">
                            <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>
                            
                            <button onclick="toggleVisibility('${item.id}')" 
                                    oncontextmenu="openColorPopover(event, '${item.id}')"
                                    class="w-6 h-6 rounded-full flex items-center justify-center shrink-0 transition" 
                                    style="background-color: ${item.visible ? item.color : 'transparent'}; border: 2px solid ${item.color}">
                                ${item.visible ? '<i class="fa-solid fa-check text-white text-[10px]"></i>' : ''}
                            </button>

                            <input id="input-${item.id}" type="text" value="${item.rawText}" placeholder="수식 입력 (예: y = sin(x))" 
                                   onfocus="setActiveItem('${item.id}')"
                                   oninput="updateExpression('${item.id}', this.value)"
                                   class="flex-1 text-base font-serif italic bg-transparent focus:outline-none ${item.error ? 'text-rose-600' : 'text-slate-800'}">

                            <button onclick="removeExpression('${item.id}')" class="text-slate-300 hover:text-slate-600 p-1 rounded transition">
                                <i class="fa-solid fa-xmark text-sm"></i>
                            </button>
                        </div>
                    `;
                } else if (item.type === 'table') {
                    let rowsHtml = '';
                    item.rows.forEach((r, rIdx) => {
                        rowsHtml += `
                            <tr class="border-b border-slate-100">
                                <td class="p-1"><input type="text" value="${r.x}" oninput="updateTableCell('${item.id}', ${rIdx}, 'x', this.value)" class="w-full text-center bg-slate-50 border rounded text-xs py-0.5"></td>
                                <td class="p-1"><input type="text" value="${r.y}" oninput="updateTableCell('${item.id}', ${rIdx}, 'y', this.value)" class="w-full text-center bg-slate-50 border rounded text-xs py-0.5"></td>
                            </tr>
                        `;
                    });

                    el.innerHTML = `
                        <div class="flex items-center justify-between">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>
                                <span class="text-xs font-bold text-emerald-600">표 (Table)</span>
                            </div>
                            <button onclick="removeExpression('${item.id}')" class="text-slate-300 hover:text-slate-600 p-1 rounded"><i class="fa-solid fa-xmark text-sm"></i></button>
                        </div>
                        <table class="w-full text-xs text-center border">
                            <thead>
                                <tr class="bg-slate-100 font-semibold">
                                    <th class="p-1 border">x₁</th>
                                    <th class="p-1 border">y₁</th>
                                </tr>
                            </thead>
                            <tbody>${rowsHtml}</tbody>
                        </table>
                    `;
                } else if (item.type === 'note') {
                    el.innerHTML = `
                        <div class="flex items-center space-x-2">
                            <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>
                            <input type="text" value="${item.text}" oninput="item.text=this.value" class="flex-1 text-xs text-slate-600 bg-transparent focus:outline-none italic">
                            <button onclick="removeExpression('${item.id}')" class="text-slate-300 hover:text-slate-600 p-1 rounded"><i class="fa-solid fa-xmark text-sm"></i></button>
                        </div>
                    `;
                }

                expressionsList.appendChild(el);
            });

            // Dynamically Render Variable Sliders if 'a' or 'b' exist
            ['a', 'b'].forEach(v => {
                if (state.variables.hasOwnProperty(v)) {
                    const sliderDiv = document.createElement('div');
                    sliderDiv.className = 'p-3 bg-amber-50/60 border-b border-amber-200 flex flex-col space-y-1.5';
                    sliderDiv.innerHTML = `
                        <div class="flex justify-between items-center text-xs text-amber-900 font-semibold">
                            <span>슬라이더 변수 ${v} = <span id="slider-val-${v}">${state.variables[v]}</span></span>
                        </div>
                        <input type="range" min="-10" max="10" step="0.1" value="${state.variables[v]}" 
                               oninput="updateVariableSlider('${v}', this.value)" class="w-full accent-amber-600">
                    `;
                    expressionsList.appendChild(sliderDiv);
                }
            });
        }

        function setActiveItem(id) {
            state.activeItemId = id;
            // When paused, rebuild tracks on the next Play so the newly selected curve is followed.
            if (!state.audio.isPlaying) disposeAudioTracks();
        }

        /**
         * Popover Menu Handlers
         */
        function openColorPopover(e, itemId) {
            e.preventDefault();
            state.colorPopoverItemId = itemId;
            colorPopover.style.left = `${e.clientX}px`;
            colorPopover.style.top = `${e.clientY}px`;
            colorPopover.classList.remove('hidden');
        }

        function setColorForSelected(color) {
            if (state.colorPopoverItemId) {
                const item = state.items.find(it => it.id === state.colorPopoverItemId);
                if (item) {
                    item.color = color;
                    renderExpressionList();
                    render();
                }
            }
            colorPopover.classList.add('hidden');
        }

        function setStyleForSelected(style) {
            if (state.colorPopoverItemId) {
                const item = state.items.find(it => it.id === state.colorPopoverItemId);
                if (item) {
                    item.lineStyle = style;
                    render();
                }
            }
            colorPopover.classList.add('hidden');
        }

        function toggleAddMenu() {
            document.getElementById('add-menu-popover').classList.toggle('hidden');
        }
        function hideAddMenu() {
            document.getElementById('add-menu-popover').classList.add('hidden');
        }

        /**
         * Virtual On-Screen Keypad Functions
         */
        function insertKey(key) {
            if (!state.activeItemId) return;
            const input = document.getElementById(`input-${state.activeItemId}`);
            if (!input) return;

            const start = input.selectionStart;
            const end = input.selectionEnd;
            const val = input.value;

            input.value = val.substring(0, start) + key + val.substring(end);
            input.focus();
            input.setSelectionRange(start + key.length, start + key.length);

            updateExpression(state.activeItemId, input.value);
        }

        function handleBackspace() {
            if (!state.activeItemId) return;
            const input = document.getElementById(`input-${state.activeItemId}`);
            if (!input) return;

            const start = input.selectionStart;
            const end = input.selectionEnd;
            const val = input.value;

            if (start === end && start > 0) {
                input.value = val.substring(0, start - 1) + val.substring(start);
                input.setSelectionRange(start - 1, start - 1);
            } else if (start !== end) {
                input.value = val.substring(0, start) + val.substring(end);
                input.setSelectionRange(start, start);
            }
            input.focus();
            updateExpression(state.activeItemId, input.value);
        }

        function moveCursor(dir) {
            if (!state.activeItemId) return;
            const input = document.getElementById(`input-${state.activeItemId}`);
            if (!input) return;

            const pos = input.selectionStart + dir;
            input.focus();
            input.setSelectionRange(pos, pos);
        }

        function handleEnter() {
            addExpression();
        }

        /**
         * Cosmos Audio Trace Engine
         * Each visible curve can have its own oscillator. X controls time/pan;
         * Y controls pitch, while a moving marker follows the sampled graph point.
         */
        function initAudioEngine() {
            if (!state.audio.ctx) {
                const AudioContextCtor = window.AudioContext || window.webkitAudioContext;
                if (!AudioContextCtor) {
                    showToast('이 브라우저는 Web Audio API를 지원하지 않습니다.');
                    return false;
                }
                state.audio.ctx = new AudioContextCtor();
                state.audio.masterGain = state.audio.ctx.createGain();
                state.audio.masterGain.gain.value = state.audio.vol;
                state.audio.masterGain.connect(state.audio.ctx.destination);
            }
            if (state.audio.ctx.state === 'suspended') state.audio.ctx.resume();
            return true;
        }

        function getAudioTargets() {
            const valid = state.items.filter(it => it.type === 'expression' && it.visible && it.compiled && !it.error);
            if (state.audio.mode === 'visible') return valid;
            const active = valid.find(it => it.id === state.activeItemId);
            return active ? [active] : (valid.length ? [valid[0]] : []);
        }

        function disposeAudioTracks() {
            state.audio.tracks.forEach(track => {
                try { track.osc.stop(); } catch (_) {}
                try { track.osc.disconnect(); track.gain.disconnect(); if (track.panner) track.panner.disconnect(); } catch (_) {}
            });
            state.audio.tracks = [];
        }

        function buildAudioTracks() {
            disposeAudioTracks();
            const targets = getAudioTargets();
            if (!targets.length) return false;
            const ctx = state.audio.ctx;
            targets.forEach((item, index) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                const panner = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
                osc.type = state.audio.waveform;
                osc.frequency.value = 440;
                gain.gain.value = 0;
                if (panner) {
                    osc.connect(panner);
                    panner.connect(gain);
                } else {
                    osc.connect(gain);
                }
                gain.connect(state.audio.masterGain);
                osc.start();
                state.audio.tracks.push({ item, osc, gain, panner, index, count: targets.length });
            });
            return true;
        }

        function readAudioSettings() {
            const startInput = document.getElementById('audio-x-start');
            const endInput = document.getElementById('audio-x-end');
            const start = Number(startInput.value);
            const end = Number(endInput.value);
            if (!Number.isFinite(start) || !Number.isFinite(end) || end <= start) {
                showToast('끝 x는 시작 x보다 커야 합니다.');
                return false;
            }
            state.audio.xStart = start;
            state.audio.xEnd = end;
            state.audio.duration = (Number(document.getElementById('audio-duration').value) || 15) / Math.max(0.25, state.audio.speed);
            state.audio.mode = document.getElementById('audio-track-mode').value;
            state.audio.waveform = document.getElementById('audio-waveform').value;
            return true;
        }

        function toggleAudioPlayback() {
            if (state.audio.isPlaying) {
                pauseAudioTrace();
                return;
            }
            if (!initAudioEngine() || !readAudioSettings()) return;
            if (!state.audio.tracks.length && !buildAudioTracks()) {
                showToast('추적할 함수가 없습니다. 수식을 입력하고 표시 상태를 확인하세요.');
                return;
            }
            // A completed run starts over; a paused run resumes from its last progress.
            if (state.audio.elapsedBeforePause >= state.audio.duration) {
                state.audio.elapsedBeforePause = 0;
                disposeAudioTracks();
                if (!buildAudioTracks()) {
                    showToast('추적할 함수가 없습니다.');
                    return;
                }
            }
            state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;
            state.audio.isPlaying = true;
            const status = document.getElementById('btn-audio-trace-status');
            status.textContent = state.audio.mode === 'visible' ? `전체 그래프 추적 중 · ${state.audio.tracks.length}개 레이어` : '선택한 그래프 추적 중';
            status.className = 'w-full bg-blue-100 text-blue-700 text-xs py-1 rounded font-semibold text-center';
            document.getElementById('audio-play-text').textContent = '일시정지';
            document.getElementById('audio-play-icon').className = 'fa-solid fa-pause text-xs';
            state.audio.masterGain.gain.setTargetAtTime(state.audio.vol, state.audio.ctx.currentTime, 0.03);
            cancelAnimationFrame(state.audio.timer);
            state.audio.timer = requestAnimationFrame(audioTraceFrame);
        }

        function pauseAudioTrace() {
            if (!state.audio.isPlaying) return;
            state.audio.isPlaying = false;
            state.audio.elapsedBeforePause = Math.min(state.audio.duration, (performance.now() - state.audio.startedAt) / 1000);
            cancelAnimationFrame(state.audio.timer);
            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02);
            document.getElementById('audio-play-text').textContent = '계속 재생';
            document.getElementById('audio-play-icon').className = 'fa-solid fa-play text-xs';
            const status = document.getElementById('btn-audio-trace-status');
            status.textContent = '오디오 추적 일시정지됨';
            status.className = 'w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center';
        }

        function stopAudioTrace() {
            state.audio.musicPlaying = false;
            state.audio.isPlaying = false;
            cancelAnimationFrame(state.audio.timer);
            state.audio.elapsedBeforePause = 0;
            state.audio.currX = state.audio.xStart;
            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02);
            state.audio.tracks.forEach(t => t.gain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02));
            document.getElementById('audio-play-text').textContent = '그래프 듣기';
            document.getElementById('audio-play-icon').className = 'fa-solid fa-play text-xs';
            document.getElementById('btn-audio-trace-status').textContent = '오디오 추적 꺼짐';
            document.getElementById('btn-audio-trace-status').className = 'w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center';
            document.getElementById('audio-progress').value = 0;
            document.getElementById('audio-progress-text').textContent = `x = ${state.audio.xStart.toFixed(2)}`;
            document.getElementById('audio-note-readout').textContent = '음높이: 대기 중 · 추적 점: 대기 중';
            if (state.activeHoverPoint && state.activeHoverPoint.audioTrace) state.activeHoverPoint = null;
            disposeAudioTracks();
            render();
        }

        function restartAudioTrace() {
            stopAudioTrace();
            if (readAudioSettings()) {
                state.audio.currX = state.audio.xStart;
                document.getElementById('audio-progress').value = 0;
            }
            toggleAudioPlayback();
        }

        function midiToFrequency(midi) { return 440 * Math.pow(2, (midi - 69) / 12); }
        function frequencyToNote(freq) {
            if (!Number.isFinite(freq) || freq <= 0) return '—';
            const names = ['도', '도♯', '레', '레♯', '미', '파', '파♯', '솔', '솔♯', '라', '라♯', '시'];
            const midi = Math.round(69 + 12 * Math.log2(freq / 440));
            return `${names[((midi % 12) + 12) % 12]}${Math.floor(midi / 12) - 1}`;
        }

        function evaluateAudioY(item, x) {
            try {
                const value = item.compiled.evaluate({ x, ...state.variables });
                const y = typeof value === 'number' ? value : (value && typeof value.re === 'number' ? value.re : NaN);
                return Number.isFinite(y) ? y : NaN;
            } catch (_) { return NaN; }
        }

        function musicScaleNotes() {
            const type = document.getElementById('music-scale').value;
            if (type === 'minor') return [0,2,3,5,7,8,10];
            if (type === 'pentatonic') return [0,2,4,7,9];
            if (type === 'chromatic') return Array.from({length:12}, (_,i)=>i);
            return [0,2,4,5,7,9,11];
        }
        function playSynthNote(freq, duration, type='triangle', volume=0.15, when=null) {
            if (!state.audio.ctx || !state.audio.masterGain) return;
            const ctx = state.audio.ctx, t = when == null ? ctx.currentTime : when;
            const osc = ctx.createOscillator(), gain = ctx.createGain();
            osc.type = type; osc.frequency.setValueAtTime(Math.max(30, Math.min(2000, freq)), t);
            gain.gain.setValueAtTime(0.0001, t); gain.gain.exponentialRampToValueAtTime(Math.max(0.001, volume), t + 0.015);
            gain.gain.exponentialRampToValueAtTime(0.0001, t + Math.max(0.06, duration));
            osc.connect(gain); gain.connect(state.audio.masterGain); osc.start(t); osc.stop(t + duration + 0.04);
            state.audio.musicNodes.push({osc, gain});
            if (state.audio.musicNodes.length > 160) state.audio.musicNodes.splice(0, 40);
        }
        function playKick(when) {
            const ctx=state.audio.ctx, osc=ctx.createOscillator(), gain=ctx.createGain();
            osc.type='sine'; osc.frequency.setValueAtTime(120,when); osc.frequency.exponentialRampToValueAtTime(42,when+0.12);
            gain.gain.setValueAtTime(0.22,when); gain.gain.exponentialRampToValueAtTime(0.001,when+0.14);
            osc.connect(gain); gain.connect(state.audio.masterGain); osc.start(when); osc.stop(when+0.15);
        }
        function playHat(when) {
            const ctx=state.audio.ctx, length=Math.floor(ctx.sampleRate*0.045), buffer=ctx.createBuffer(1,length,ctx.sampleRate), data=buffer.getChannelData(0);
            for(let i=0;i<length;i++) data[i]=(Math.random()*2-1)*(1-i/length);
            const src=ctx.createBufferSource(), filter=ctx.createBiquadFilter(), gain=ctx.createGain();
            src.buffer=buffer; filter.type='highpass'; filter.frequency.value=6500; gain.gain.setValueAtTime(0.07,when); gain.gain.exponentialRampToValueAtTime(0.001,when+0.045);
            src.connect(filter); filter.connect(gain); gain.connect(state.audio.masterGain); src.start(when);
        }
        function runMusicStep(step, x) {
            const ctx=state.audio.ctx, bpm=Number(document.getElementById('music-bpm').value), beat=60/bpm, when=ctx.currentTime+0.015;
            const genre=document.getElementById('music-genre').value, root=Number(document.getElementById('music-key').value), scale=musicScaleNotes();
            const target=getAudioTargets()[0]; let graphY=target ? evaluateAudioY(target,x) : 0; if(!Number.isFinite(graphY)) graphY=0;
            const graphMidi=Math.max(45,Math.min(84,Math.round(60+graphY*2)));
            const note=(n,oct=0)=>440*Math.pow(2,(n+root+oct-69)/12);
            const vol=state.audio.musicVolumes;
            if(document.getElementById('part-melody').checked){
                const degree=Math.abs(Math.round(graphY*2+step))%scale.length; const midi=graphMidi+(scale[degree]||0)-scale[0];
                playSynthNote(note(midi),beat*0.72,genre==='edm'?'sawtooth':'triangle',vol.melody,when);
            }
            if(document.getElementById('part-bass').checked && step%2===0) playSynthNote(note(36+root%12),beat*1.65,'sawtooth',vol.bass,when);
            if(document.getElementById('part-chords').checked && step%4===0){
                const chord=[0, scale[2]||4, scale[4]||7]; chord.forEach(n=>playSynthNote(note(48+n),beat*3.2,'sine',vol.chords/2.2,when));
            }
            if(document.getElementById('part-arp').checked){const degree=scale[step%scale.length];playSynthNote(note(60+degree),beat*0.42,'triangle',vol.arp,when);}
            if(document.getElementById('part-drums').checked){
                if(step%4===0 || (genre==='phonk' && step%4===2)) playKick(when);
                if(step%4===2) playSynthNote(180,beat*0.1,'triangle',vol.drums*0.45,when);
                if(step%2===0 || genre==='edm') playHat(when);
            }
        }
        function playGraphMusic() {
            if(!initAudioEngine()) return;
            state.audio.musicPlaying=true; state.audio.lastMusicStep=-1;
            document.getElementById('music-status').textContent='음악 재생 중 · 그래프 값이 멜로디에 반영됩니다.';
            state.audio.masterGain.gain.setTargetAtTime(state.audio.vol, state.audio.ctx.currentTime, 0.03);
            if(!state.audio.isPlaying) toggleAudioPlayback();
        }
        function stopGraphMusic() {
            state.audio.musicPlaying=false; state.audio.musicNodes.forEach(n=>{try{n.osc.stop()}catch(_){} try{n.gain.disconnect()}catch(_){}}); state.audio.musicNodes=[];
            document.getElementById('music-status').textContent='음악 정지됨';
            if(state.audio.isPlaying) pauseAudioTrace();
        }
        function readMusicPreset() {
            return { bpm:document.getElementById('music-bpm').value, genre:document.getElementById('music-genre').value, key:document.getElementById('music-key').value, scale:document.getElementById('music-scale').value, parts:['melody','bass','chords','arp','drums'].reduce((o,k)=>{o[k]=document.getElementById('part-'+k).checked;return o;},{}), waveform:document.getElementById('audio-waveform').value };
        }
        function refreshMusicLibrary() {
            const select=document.getElementById('music-library-select'); if(!select) return;
            const current=select.value; let songs=[]; try{songs=JSON.parse(localStorage.getItem('cosmosMusicLibrary')||'[]')}catch(_){}
            select.innerHTML='<option value="">저장한 곡 불러오기</option>';
            songs.forEach((song,i)=>{const option=document.createElement('option');option.value=String(i);option.textContent=song.name;select.appendChild(option);});
            if(current && songs[Number(current)]) select.value=current;
        }
        function saveMusicPreset() {
            const name=document.getElementById('music-song-name').value.trim() || '내 곡 '+new Date().toLocaleString('ko-KR');
            let songs=[];try{songs=JSON.parse(localStorage.getItem('cosmosMusicLibrary')||'[]')}catch(_){}
            songs.push({name,settings:readMusicPreset()});
            try{localStorage.setItem('cosmosMusicLibrary',JSON.stringify(songs));refreshMusicLibrary();document.getElementById('music-status').textContent='「'+name+'」 저장 완료';}
            catch(_){document.getElementById('music-status').textContent='브라우저 저장 공간에 접근할 수 없습니다.';}
        }
        function loadMusicPreset() {
            const select=document.getElementById('music-library-select'); if(!select.value) return;
            let songs=[];try{songs=JSON.parse(localStorage.getItem('cosmosMusicLibrary')||'[]')}catch(_){}
            const song=songs[Number(select.value)]; if(!song) return; const a=song.settings;
            document.getElementById('music-bpm').value=a.bpm; document.getElementById('music-bpm-value').textContent=a.bpm;
            document.getElementById('music-genre').value=a.genre; document.getElementById('music-key').value=a.key; document.getElementById('music-scale').value=a.scale;
            Object.entries(a.parts||{}).forEach(([k,v])=>{const el=document.getElementById('part-'+k);if(el)el.checked=v;});
            if(a.waveform) document.getElementById('audio-waveform').value=a.waveform;
            document.getElementById('music-status').textContent='「'+song.name+'」 불러옴';
        }
        function renderAudioLayerVolumes() {
            const host=document.getElementById('audio-layer-volumes'); if(!host) return;
            const targets=state.items.filter(it=>it.type==='expression');
            host.innerHTML='<div class="font-semibold text-slate-600">레이어별 볼륨</div>';
            if(!targets.length){host.insertAdjacentHTML('beforeend','<div class="text-slate-400">함수를 추가하면 레이어별 볼륨이 표시됩니다.</div>');return;}
            targets.forEach((item,i)=>{
                const key='layer-vol-'+item.id;
                if(state.audio.musicVolumes[key]===undefined) state.audio.musicVolumes[key]=0.6;
                const row=document.createElement('label'); row.className='flex items-center gap-2 text-slate-600';
                row.innerHTML=`<span class="w-28 truncate">${item.name||item.expr||('레이어 '+(i+1))}</span><input class="flex-1 accent-blue-600" type="range" min="0" max="1" step="0.05" value="${state.audio.musicVolumes[key]}" aria-label="레이어 볼륨"><span class="w-8 text-right">${Math.round(state.audio.musicVolumes[key]*100)}%</span>`;
                const slider=row.querySelector('input'); slider.addEventListener('input',()=>{state.audio.musicVolumes[key]=Number(slider.value);row.lastElementChild.textContent=Math.round(slider.value*100)+'%';}); host.appendChild(row);
            });
        }
        document.getElementById('music-bpm').addEventListener('input', e=>document.getElementById('music-bpm-value').textContent=e.target.value);

        function audioTraceFrame(now) {
            if (!state.audio.isPlaying) return;
            const elapsed = Math.max(0, (now - state.audio.startedAt) / 1000);
            const progress = Math.min(1, elapsed / state.audio.duration);
            const x = state.audio.xStart + (state.audio.xEnd - state.audio.xStart) * progress;
            state.audio.currX = x;
            const progressSlider = document.getElementById('audio-progress');
            progressSlider.value = String(Math.round(progress * 1000));
            document.getElementById('audio-progress-text').textContent = `x = ${x.toFixed(2)} · ${elapsed.toFixed(1)}s / ${state.audio.duration}s`;

            let firstValid = null;
            const nowAudio = state.audio.ctx.currentTime;
            if (state.audio.musicPlaying) {
                const bpm=Number(document.getElementById('music-bpm').value);
                const step=Math.floor(elapsed/(60/bpm/2));
                if(step!==state.audio.lastMusicStep){state.audio.lastMusicStep=step;runMusicStep(step,x);}
            }
            state.audio.tracks.forEach(track => {
                const y = evaluateAudioY(track.item, x);
                if (!Number.isFinite(y) || Math.abs(y) > 1e6) {
                    track.gain.gain.setTargetAtTime(0, nowAudio, 0.025);
                    return;
                }
                if (!firstValid) firstValid = { x, y, color: track.item.color, audioTrace: true };
                // Map graph height to a bounded, musical MIDI range (36–84).
                const midi = Math.max(36, Math.min(84, 60 + y * 3));
                const freq = midiToFrequency(midi);
                track.osc.frequency.setTargetAtTime(freq, nowAudio, 0.025);
                // Each visible graph gets a slightly different stereo position.
                const graphPan = track.count <= 1 ? Math.max(-1, Math.min(1, (x - state.audio.xStart) / (state.audio.xEnd - state.audio.xStart) * 2 - 1)) : -0.85 + 1.7 * track.index / Math.max(1, track.count - 1);
                if (track.panner) track.panner.pan.setTargetAtTime(graphPan, nowAudio, 0.04);
                const yGain = Math.max(0.18, Math.min(1, 0.35 + (y + 4) / 16));
                const individualVolume = state.audio.musicVolumes['layer-vol-' + track.item.id] === undefined ? 1 : state.audio.musicVolumes['layer-vol-' + track.item.id];
                const layerGain = yGain * individualVolume / Math.sqrt(track.count);
                track.gain.gain.setTargetAtTime(layerGain, nowAudio, 0.035);
                if (track.item.id === state.activeItemId || !firstValid) firstValid = { x, y, color: track.item.color, audioTrace: true, freq };
            });

            if (firstValid) {
                state.activeHoverPoint = firstValid;
                const freq = firstValid.freq || midiToFrequency(Math.max(36, Math.min(84, 60 + firstValid.y * 3)));
                document.getElementById('audio-note-readout').textContent = `y = ${firstValid.y.toFixed(3)} · ${freq.toFixed(1)} Hz (${frequencyToNote(freq)}) · ${state.audio.tracks.length}개 트랙`;
            } else {
                state.activeHoverPoint = null;
                document.getElementById('audio-note-readout').textContent = `x = ${x.toFixed(2)} · 이 위치에서는 함수값이 정의되지 않아 소리를 잠시 멈춥니다.`;
                state.audio.tracks.forEach(t => t.gain.gain.setTargetAtTime(0, nowAudio, 0.02));
            }
            render();

            if (progress >= 1) {
                state.audio.elapsedBeforePause = state.audio.duration;
                pauseAudioTrace();
                document.getElementById('audio-play-text').textContent = '처음부터 재생';
                return;
            }
            state.audio.timer = requestAnimationFrame(audioTraceFrame);
        }

        function changeAudioVolume() {
            // Kept as a compatibility hook for older buttons.
            state.audio.vol = state.audio.vol >= 0.99 ? 0.2 : (state.audio.vol <= 0.21 ? 0.5 : 1);
            const slider = document.getElementById('audio-volume-range');
            if (slider) slider.value = state.audio.vol;
            document.getElementById('audio-vol-text').textContent = `${Math.round(state.audio.vol * 100)}%`;
            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(state.audio.isPlaying ? state.audio.vol : 0, state.audio.ctx.currentTime, 0.02);
        }

        function changeAudioSpeed() {
            state.audio.speed = state.audio.speed >= 2.95 ? 0.5 : (state.audio.speed <= 0.51 ? 1 : 3);
            const slider = document.getElementById('audio-speed-range');
            if (slider) slider.value = state.audio.speed;
            document.getElementById('audio-speed-text').textContent = `${state.audio.speed.toFixed(2)}×`;
        }

        function seekAudioTrace() {
            if (!readAudioSettings()) return;
            const ratio = Number(document.getElementById('audio-progress').value) / 1000;
            state.audio.elapsedBeforePause = ratio * state.audio.duration;
            state.audio.currX = state.audio.xStart + ratio * (state.audio.xEnd - state.audio.xStart);
            const previewTargets = state.audio.tracks.length ? state.audio.tracks.map(t => t.item) : getAudioTargets();
            for (const item of previewTargets) {
                const y = evaluateAudioY(item, state.audio.currX);
                if (Number.isFinite(y)) {
                    state.activeHoverPoint = { x: state.audio.currX, y, color: item.color, audioTrace: true };
                    break;
                }
            }
            document.getElementById('audio-progress-text').textContent = `x = ${state.audio.currX.toFixed(2)} · ${state.audio.elapsedBeforePause.toFixed(1)}s / ${state.audio.duration.toFixed(1)}s`;
            if (state.audio.isPlaying) state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;
            render();
        }

        document.getElementById('audio-volume-range').addEventListener('input', event => {
            state.audio.vol = Number(event.target.value);
            document.getElementById('audio-vol-text').textContent = `${Math.round(state.audio.vol * 100)}%`;
            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(state.audio.isPlaying ? state.audio.vol : 0, state.audio.ctx.currentTime, 0.02);
        });
        document.getElementById('audio-speed-range').addEventListener('input', event => {
            const newSpeed = Number(event.target.value);
            if (state.audio.isPlaying) {
                state.audio.elapsedBeforePause = Math.max(0, (performance.now() - state.audio.startedAt) / 1000);
                state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;
            }
            state.audio.speed = newSpeed;
            state.audio.duration = (Number(document.getElementById('audio-duration').value) || 15) / state.audio.speed;
            document.getElementById('audio-speed-text').textContent = `${newSpeed.toFixed(2)}×`;
        });
        document.getElementById('audio-progress').addEventListener('input', seekAudioTrace);
        ['audio-track-mode', 'audio-waveform'].forEach(id => {
            document.getElementById(id).addEventListener('change', () => {
                if (state.audio.isPlaying) pauseAudioTrace();
                readAudioSettings();
                disposeAudioTracks();
            });
        });
        ['audio-x-start', 'audio-x-end', 'audio-duration'].forEach(id => {
            document.getElementById(id).addEventListener('change', () => {
                if (state.audio.isPlaying) pauseAudioTrace();
                readAudioSettings();
                state.audio.elapsedBeforePause = 0;
                state.audio.currX = state.audio.xStart;
                document.getElementById('audio-progress').value = 0;
            });
        });

        function navigatePoint(dir) {
            if (state.snapPoints.length === 0) return;
            state.navPointIdx = (state.navPointIdx + dir + state.snapPoints.length) % state.snapPoints.length;
            const pt = state.snapPoints[state.navPointIdx];
            state.activeHoverPoint = pt;
            tooltipCoords.textContent = `(${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`;
            render();
            showToast(`점 이동: (${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`);
        }

        function navigateInterest(dir) { navigatePoint(dir); }
        function navigateCurve(dir) { navigatePoint(dir); }

        function speakDescription(type) {
            if (!('speechSynthesis' in window)) {
                showToast('브라우저가 음성 합성을 지원하지 않습니다.');
                return;
            }
            let msg = '';
            if (type === 'point' && state.activeHoverPoint) {
                msg = `현재 추적 점의 X좌표는 ${state.activeHoverPoint.x.toFixed(2)}, Y좌표는 ${state.activeHoverPoint.y.toFixed(2)}입니다.`;
            } else if (type === 'curve') {
                const active = state.items.find(it => it.id === state.activeItemId && it.type === 'expression');
                msg = active ? `현재 선택된 함수는 ${active.rawText || '수식이 입력되지 않은 함수'}입니다.` : '먼저 왼쪽 수식 목록에서 함수를 선택해 주세요.';
            } else {
                msg = '좌표평면의 수평 X축과 수직 Y축, 그리고 원점의 위치를 표시하고 있습니다.';
            }
            const utterance = new SpeechSynthesisUtterance(msg);
            utterance.lang = 'ko-KR';
            window.speechSynthesis.speak(utterance);
            showToast('음성 설명 재생 중...');
        }

        function switchBottomTab(tab) {
            const keypadContent = document.getElementById('keypad-tab-content');
            const audioContent = document.getElementById('audio-tab-content');
            const tabKeypad = document.getElementById('tab-btn-keypad');
            const tabAudio = document.getElementById('tab-btn-audio');

            if (tab === 'keypad') {
                keypadContent.classList.remove('hidden');
                audioContent.classList.add('hidden');
                tabKeypad.className = 'px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition';
                tabAudio.className = 'px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition flex items-center space-x-1';
            } else {
                keypadContent.classList.add('hidden');
                audioContent.classList.remove('hidden');
                audioContent.classList.add('flex');
                tabAudio.className = 'px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition flex items-center space-x-1';
                tabKeypad.className = 'px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition';
            }
        }

        /**
         * Canvas Mouse Interactions (Pan, Zoom, Snap Pinning)
         */
        canvas.addEventListener('mousedown', (e) => {
            state.isDragging = true;
            state.dragStart = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('mouseup', () => {
            state.isDragging = false;
        });

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;

            if (state.isDragging) {
                state.offsetX += e.clientX - state.dragStart.x;
                state.offsetY += e.clientY - state.dragStart.y;
                state.dragStart = { x: e.clientX, y: e.clientY };
                render();
            } else {
                // Detect Snap Point Hovering
                let hovered = null;
                for (let pt of state.snapPoints) {
                    const screen = mathToScreen(pt.x, pt.y);
                    if (Math.hypot(mouseX - screen.x, mouseY - screen.y) < 12) {
                        hovered = pt;
                        break;
                    }
                }

                if (hovered) {
                    state.activeHoverPoint = hovered;
                    tooltipCoords.textContent = `(${hovered.x.toFixed(2)}, ${hovered.y.toFixed(2)})`;
                    tooltip.style.left = `${e.clientX}px`;
                    tooltip.style.top = `${e.clientY}px`;
                    tooltip.classList.remove('hidden');
                } else {
                    state.activeHoverPoint = null;
                    tooltip.classList.add('hidden');
                }
                render();
            }
        });

        canvas.addEventListener('click', (e) => {
            if (state.activeHoverPoint) {
                // Pin point label on canvas
                state.pinnedPoints.push(state.activeHoverPoint);
                render();
            }
        });

        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            const factor = e.deltaY < 0 ? 1.1 : 0.9;
            state.scale *= factor;
            render();
        }, { passive: false });

        /**
         * View Zoom & Reset Actions
         */
        function zoomIn() { state.scale *= 1.25; render(); }
        function zoomOut() { state.scale /= 1.25; render(); }
        function resetView() {
            state.scale = 60;
            state.offsetX = 0;
            state.offsetY = 0;
            state.pinnedPoints = [];
            render();
            showToast('그래프 보기가 초기화되었습니다.');
        }

        /**
         * History & State Management
         */
        function saveHistory() {
            state.history = state.history.slice(0, state.historyIdx + 1);
            state.history.push(JSON.stringify(state.items));
            state.historyIdx++;
        }

        function undo() {
            if (state.historyIdx > 0) {
                state.historyIdx--;
                state.items = JSON.parse(state.history[state.historyIdx]);
                renderExpressionList();
                render();
            }
        }

        function redo() {
            if (state.historyIdx < state.history.length - 1) {
                state.historyIdx++;
                state.items = JSON.parse(state.history[state.historyIdx]);
                renderExpressionList();
                render();
            }
        }

        function saveGraphState() {
            localStorage.setItem('cosmos_saved_graph', JSON.stringify(state.items));
            showToast('그래프가 브라우저에 저장되었습니다!');
        }

        /**
         * Modal Windows Management
         */
        function openModal(id) {
            document.getElementById('modal-backdrop').classList.remove('hidden');
            ['login-modal', 'signup-modal', 'share-modal', 'settings-modal', 'help-modal'].forEach(m => {
                document.getElementById(m).classList.add('hidden');
            });
            if (id === 'share-modal') {
                const shareInput = document.getElementById('share-url-input');
                shareInput.value = (window.location.protocol === 'http:' || window.location.protocol === 'https:')
                    ? window.location.href : '';
            }
            document.getElementById(id).classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('modal-backdrop').classList.add('hidden');
        }

        // Demo authentication: accounts are local to this browser, not a secure server account system.
        const COSMOS_USERS_KEY = 'cosmos_demo_users_v1';
        const COSMOS_SESSION_KEY = 'cosmos_demo_session_v1';

        function readCosmosUsers() {
            try { return JSON.parse(localStorage.getItem(COSMOS_USERS_KEY) || '{}'); }
            catch (err) { return {}; }
        }

        async function hashCosmosPassword(password) {
            if (!window.crypto || !crypto.subtle) throw new Error('현재 브라우저에서 안전한 비밀번호 해시 기능을 사용할 수 없습니다.');
            const bytes = new TextEncoder().encode(password);
            const digest = await crypto.subtle.digest('SHA-256', bytes);
            return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
        }

        function showAuthError(id, message) {
            const el = document.getElementById(id);
            el.textContent = message;
            el.classList.remove('hidden');
        }

        function clearAuthError(id) {
            const el = document.getElementById(id);
            el.textContent = '';
            el.classList.add('hidden');
        }

        async function signupAccount(event) {
            event.preventDefault();
            clearAuthError('signup-error');
            const name = document.getElementById('signup-name').value.trim();
            const email = document.getElementById('signup-email').value.trim().toLowerCase();
            const password = document.getElementById('signup-password').value;
            const confirm = document.getElementById('signup-confirm').value;
            if (!name || !email) return showAuthError('signup-error', '이름과 이메일을 입력해 주세요.');
            if (password.length < 8) return showAuthError('signup-error', '비밀번호는 8자 이상이어야 합니다.');
            if (password !== confirm) return showAuthError('signup-error', '비밀번호 확인이 일치하지 않습니다.');
            const users = readCosmosUsers();
            if (users[email]) return showAuthError('signup-error', '이미 가입된 이메일입니다. 로그인해 주세요.');
            try {
                users[email] = { name, email, passwordHash: await hashCosmosPassword(password), createdAt: new Date().toISOString() };
                localStorage.setItem(COSMOS_USERS_KEY, JSON.stringify(users));
                localStorage.setItem(COSMOS_SESSION_KEY, JSON.stringify({ name, email }));
                updateAccountUI();
                closeModal();
                document.getElementById('signup-password').value = '';
                document.getElementById('signup-confirm').value = '';
                showToast('회원가입이 완료되었습니다.');
            } catch (err) {
                showAuthError('signup-error', err.message || '계정 저장에 실패했습니다. 브라우저 저장 설정을 확인해 주세요.');
            }
        }

        async function loginAccount(event) {
            event.preventDefault();
            clearAuthError('login-error');
            const email = document.getElementById('login-email').value.trim().toLowerCase();
            const password = document.getElementById('login-password').value;
            const users = readCosmosUsers();
            if (!users[email]) return showAuthError('login-error', '가입된 계정을 찾을 수 없습니다. 이메일을 확인하거나 회원가입해 주세요.');
            try {
                const hash = await hashCosmosPassword(password);
                if (hash !== users[email].passwordHash) return showAuthError('login-error', '이메일 또는 비밀번호가 올바르지 않습니다.');
                localStorage.setItem(COSMOS_SESSION_KEY, JSON.stringify({ name: users[email].name, email }));
                updateAccountUI();
                closeModal();
                document.getElementById('login-password').value = '';
                showToast(`${users[email].name}님, 로그인되었습니다.`);
            } catch (err) {
                showAuthError('login-error', err.message || '로그인 처리 중 오류가 발생했습니다.');
            }
        }

        function updateAccountUI() {
            let session = null;
            try { session = JSON.parse(localStorage.getItem(COSMOS_SESSION_KEY) || 'null'); } catch (err) {}
            const label = document.getElementById('account-label');
            const loginBtn = document.getElementById('login-nav-btn');
            const signupBtn = document.getElementById('signup-nav-btn');
            const logoutBtn = document.getElementById('logout-nav-btn');
            if (session && session.email) {
                label.textContent = session.name || session.email;
                label.classList.remove('hidden');
                loginBtn.classList.add('hidden');
                signupBtn.classList.add('hidden');
                logoutBtn.classList.remove('hidden');
            } else {
                label.classList.add('hidden');
                loginBtn.classList.remove('hidden');
                signupBtn.classList.remove('hidden');
                logoutBtn.classList.add('hidden');
            }
        }

        function logoutAccount() {
            localStorage.removeItem(COSMOS_SESSION_KEY);
            updateAccountUI();
            showToast('로그아웃되었습니다.');
        }

        function showToast(msg) {
            const toast = document.getElementById('toast-msg');
            toast.textContent = msg;
            toast.classList.remove('opacity-0');
            setTimeout(() => toast.classList.add('opacity-0'), 2500);
        }

        function copyShareUrl() {
            const input = document.getElementById('share-url-input');
            const currentUrl = window.location.href;
            if (window.location.protocol === 'http:' || window.location.protocol === 'https:') {
                input.value = currentUrl;
                input.select();
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(currentUrl).then(() => showToast('Cosmos 주소를 복사했습니다.')).catch(() => {
                        document.execCommand('copy'); showToast('주소 복사를 시도했습니다.');
                    });
                } else {
                    document.execCommand('copy'); showToast('주소 복사를 시도했습니다.');
                }
            } else {
                showToast('로컬 파일로 실행 중입니다. 공유하려면 HTML 파일 자체를 전달하세요.');
            }
        }

        function toggleAngleMode() {
            state.angleUnit = state.angleUnit === 'rad' ? 'deg' : 'rad';
            document.getElementById('btn-lang-toggle').textContent = state.angleUnit === 'rad' ? 'Rad' : 'Deg';
            showToast(`각도 단위: ${state.angleUnit.toUpperCase()}`);
        }

        function setAngleUnit(unit) {
            state.angleUnit = unit;
            document.getElementById('set-rad-btn').className = unit === 'rad' ? 'px-3 py-1 bg-blue-600 text-white font-semibold text-xs' : 'px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs';
            document.getElementById('set-deg-btn').className = unit === 'deg' ? 'px-3 py-1 bg-blue-600 text-white font-semibold text-xs' : 'px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs';
        }

        function toggleGrid(checked) { state.showGrid = checked; render(); }
        function toggleNumbers(checked) { state.showNumbers = checked; render(); }

        /**
         * UI Sidebar and Keypad Toggles
         */
        btnToggleBottom.addEventListener('click', () => {
            bottomPanel.classList.toggle('hidden');
        });
        btnHideBottomPanel.addEventListener('click', () => {
            bottomPanel.classList.add('hidden');
        });

        btnCollapseSidebar.addEventListener('click', () => {
            sidebarPanel.classList.add('-ml-[380px]');
            btnExpandSidebar.classList.remove('hidden');
            setTimeout(resizeCanvas, 200);
        });
        btnExpandSidebar.addEventListener('click', () => {
            sidebarPanel.classList.remove('-ml-[380px]');
            btnExpandSidebar.classList.add('hidden');
            setTimeout(resizeCanvas, 200);
        });

        /**
         * Page Entry Point
         */
        window.onload = function() {
            resizeCanvas();
            updateAccountUI();
            // Initial Sine Graph matching screenshot
            addExpression('y = sin(x)');
            renderAudioLayerVolumes();
            refreshMusicLibrary();
        };
    </script>
</body>
</html>"""

components.html(HTML, height=1050, scrolling=False)
