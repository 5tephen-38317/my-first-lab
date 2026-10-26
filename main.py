<!DOCTYPE html>
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
    </style>
</head>
<body class="bg-slate-100 h-screen w-screen flex flex-col font-sans text-slate-800">

    <!-- 1. TOP NAVBAR -->
    <header class="bg-[#1c2836] text-white h-12 px-3 flex items-center justify-between z-30 shrink-0 select-none">
        <!-- Left Title and Save -->
        <div class="flex items-center space-x-2">
            <button onclick="showToast('폴더 목록을 불러왔습니다.')" class="p-1.5 hover:bg-slate-700/60 rounded text-slate-300 hover:text-white transition">
                <i class="fa-regular fa-folder text-base"></i>
            </button>
            <input id="graph-title-input" type="text" value="Cosmos 그래프" 
                   class="bg-transparent text-slate-100 text-sm font-medium px-2 py-1 rounded hover:bg-slate-700/40 focus:bg-slate-800 focus:outline-none border border-transparent focus:border-slate-600 transition w-36 sm:w-48">
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
            <button onclick="openModal('login-modal')" class="hidden sm:inline-block text-xs font-medium px-3 py-1.5 rounded hover:bg-slate-700/60 transition">
                로그인
            </button>
            <button onclick="openModal('signup-modal')" class="bg-[#2b72ee] hover:bg-blue-600 text-white text-xs font-semibold px-3 py-1.5 rounded transition shadow-sm">
                회원가입
            </button>
            <div class="h-4 w-[1px] bg-slate-600 mx-1"></div>
            <button onclick="openModal('share-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="공유">
                <i class="fa-solid fa-share-nodes text-sm"></i>
            </button>
            <button onclick="openModal('help-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="도움말">
                <i class="fa-regular fa-circle-question text-sm"></i>
            </button>
            <button onclick="toggleAngleMode()" id="btn-lang-toggle" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition text-xs font-semibold" title="각도 단위 전환 (라디안/각도)">
                Rad
            </button>
            <button onclick="openModal('settings-modal')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="설정">
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
```html
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
                            <textarea oninput="updateNote('${item.id}', this.value)" class="w-full text-sm border border-amber-200 rounded p-2 bg-amber-50 focus:outline-none focus:border-amber-400" rows="3">${item.text}</textarea>
                            <button onclick="removeExpression('${item.id}')" class="text-slate-300 hover:text-slate-600 p-1 rounded"><i class="fa-solid fa-xmark text-sm"></i></button>
                        </div>
                    `;
                }

                el.addEventListener('click', () => {
                    if (state.activeItemId !== item.id) {
                        state.activeItemId = item.id;
                        renderExpressionList();
                    }
                });

                expressionsList.appendChild(el);
            });
        }
