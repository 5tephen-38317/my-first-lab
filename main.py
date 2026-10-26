import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos - Graph to Music",
    page_icon="✿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cosmos - Graph to Music</title>
<style>
:root{
    --bg:#f6f7fb;
    --surface:#ffffff;
    --text:#17181d;
    --muted:#6f7480;
    --line:#e6e7ec;
    --accent:#7a5af8;
    --accent-dark:#6242e5;
    --accent-soft:#f0edff;
}
*{box-sizing:border-box;}
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:var(--bg);
    color:var(--text);
    overflow:hidden;
}
.workspaceShell{
    display:flex;
    flex-direction:column;
    height:100vh;
}
.appToolbar{
    height:54px;
    background:#292929;
    color:#fff;
    display:flex;
    align-items:center;
    padding:0 16px;
    gap:16px;
}
.toolbarBrand{
    font-weight:800;
    font-size:16px;
    letter-spacing:1px;
    color:#fff;
}
.fileTitle{
    background:transparent;
    color:#fff;
    border:0;
    border-left:1px solid #666;
    padding-left:12px;
    font-size:15px;
    outline:none;
}
.workspace{
    display:grid;
    grid-template-columns:320px 1fr;
    flex:1;
    height:calc(100vh - 54px);
    overflow:hidden;
}
.expressionPane{
    background:#fff;
    border-right:1px solid var(--line);
    display:flex;
    flex-direction:column;
    overflow:hidden;
}
.expressionHeader{
    padding:12px;
    border-bottom:1px solid var(--line);
    font-weight:bold;
    font-size:13px;
}
.expressionList{
    flex:1;
    overflow-y:auto;
    padding:12px;
}
.expressionItem{
    display:flex;
    align-items:center;
    gap:8px;
    padding:8px;
    border:1px solid var(--line);
    border-radius:8px;
    background:#fbfbfd;
    margin-bottom:8px;
}
.colorDot{
    width:8px;
    height:28px;
    background:var(--accent);
    border-radius:4px;
}
.expressionInput{
    flex:1;
    border:1px solid #ccc;
    border-radius:6px;
    padding:6px 10px;
    font-size:14px;
    outline:none;
}
.expressionInput:focus{
    border-color:var(--accent);
}
.graphWorkspace{
    display:flex;
    flex-direction:column;
    background:#fff;
    position:relative;
}
.graphCanvasArea{
    flex:1;
    position:relative;
    background:#fcfcfe;
}
canvas{
    width:100%;
    height:100%;
    display:block;
    touch-action:none;
}
.audioToolbar{
    height:50px;
    background:#f7f7f9;
    border-top:1px solid var(--line);
    display:flex;
    align-items:center;
    padding:0 16px;
    gap:12px;
}
button{
    background:var(--accent);
    color:#fff;
    border:0;
    border-radius:6px;
    padding:8px 14px;
    font-size:12px;
    font-weight:bold;
    cursor:pointer;
}
button:hover{
    background:var(--accent-dark);
}
.keypad{
    position:absolute;
    bottom:12px;
    right:12px;
    background:#fff;
    border:1px solid var(--line);
    border-radius:8px;
    padding:8px;
    box-shadow:0 4px 16px rgba(0,0,0,0.1);
    display:grid;
    grid-template-columns:repeat(5, 1fr);
    gap:4px;
    z-index:10;
}
.keypad button{
    background:#f0f0f5;
    color:#333;
    padding:8px;
    font-size:12px;
    min-width:36px;
}
.keypad button:hover{
    background:#e0e0ea;
}
</style>
</head>
<body>

<div class="workspaceShell">
    <div class="appToolbar">
        <div class="toolbarBrand">Cosmos</div>
        <input type="text" class="fileTitle" value="제목 없는 그래프">
    </div>
    
    <div class="workspace">
        <div class="expressionPane">
            <div class="expressionHeader">수식 목록</div>
            <div class="expressionList">
                <div class="expressionItem">
                    <div class="colorDot"></div>
                    <input type="text" id="expr1" class="expressionInput" value="Math.sin(x)">
                </div>
                <div class="expressionItem">
                    <div class="colorDot" style="background:#2d9cdb;"></div>
                    <input type="text" id="expr2" class="expressionInput" value="0.5 * x">
                </div>
            </div>
        </div>
        
        <div class="graphWorkspace">
            <div class="graphCanvasArea">
                <canvas id="graphCanvas"></canvas>
                
                <!-- 데스모스 스타일 가상 키패드 -->
                <div class="keypad">
                    <button onclick="insertText('x')">x</button>
                    <button onclick="insertText('y')">y</button>
                    <button onclick="insertText('+')">+</button>
                    <button onclick="insertText('-')">-</button>
                    <button onclick="insertText('*')">×</button>
                    <button onclick="insertText('/')">÷</button>
                    <button onclick="insertText('Math.sin(x)')">sin</button>
                    <button onclick="insertText('Math.cos(x)')">cos</button>
                    <button onclick="insertText('Math.pow(x, 2)')">x²</button>
                    <button onclick="insertText('Math.sqrt(x)')">√</button>
                </div>
            </div>
            
            <div class="audioToolbar">
                <button onclick="toggleAudio()">🎵 그래프 음악 재생 (Audio Trace)</button>
                <span id="audioStatus" style="font-size:12px; color:#666;">정지됨</span>
            </div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('graphCanvas');
const ctx = canvas.getContext('2d');

let scale = 40;
let offsetX = 0;
let offsetY = 0;
let isDragging = false;
let startX, startY;

function resizeCanvas() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    drawGrid();
}

function drawGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    const width = canvas.width;
    const height = canvas.height;
    const centerX = width / 2 + offsetX;
    const centerY = height / 2 + offsetY;

    // 격자 그리기
    ctx.strokeStyle = '#eeeef2';
    ctx.lineWidth = 1;

    for (let x = centerX % scale; x < width; x += scale) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = centerY % scale; y < height; y += scale) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // 축 그리기
    ctx.strokeStyle = '#d0d2d8';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, centerY); ctx.lineTo(width, centerY); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(centerX, 0); ctx.lineTo(centerX, height); ctx.stroke();

    // 함수 그래프 그리기
    drawFunction(document.getElementById('expr1').value, '#7a5af8');
    drawFunction(document.getElementById('expr2').value, '#2d9cdb');
}

function drawFunction(expr, color) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 2.5;
    ctx.beginPath();

    const width = canvas.width;
    const height = canvas.height;
    const centerX = width / 2 + offsetX;
    const centerY = height / 2 + offsetY;

    let first = true;
    for (let px = 0; px < width; px++) {
        let x = (px - centerX) / scale;
        let y;
        try {
            y = eval(expr);
        } catch (e) {
            y = 0;
        }
        let py = centerY - y * scale;

        if (first) {
            ctx.moveTo(px, py);
            first = false;
        } else {
            ctx.lineTo(px, py);
        }
    }
    ctx.stroke();
}

// 마우스 드래그로 화면 이동 (Pan)
canvas.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
});

window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    offsetX += e.clientX - startX;
    offsetY += e.clientY - startY;
    startX = e.clientX;
    startY = e.clientY;
    drawGrid();
});

window.addEventListener('mouseup', () => { isDragging = false; });

// 마우스 휠로 확대/축소 (Zoom)
canvas.addEventListener('wheel', (e) => {
    e.preventDefault();
    if (e.deltaY < 0) {
        scale *= 1.1;
    } else {
        scale /= 1.1;
    }
    drawGrid();
}, { passive: false });

document.getElementById('expr1').addEventListener('input', drawGrid);
document.getElementById('expr2').addEventListener('input', drawGrid);

function insertText(val) {
    const activeInput = document.activeElement;
    if (activeInput && activeInput.classList.contains('expressionInput')) {
        const start = activeInput.selectionStart;
        const end = activeInput.selectionEnd;
        const text = activeInput.value;
        activeInput.value = text.substring(0, start) + val + text.substring(end);
        activeInput.selectionStart = activeInput.selectionEnd = start + val.length;
        activeInput.focus();
        drawGrid();
    }
}

let isPlaying = false;
function toggleAudio() {
    isPlaying = !isPlaying;
    document.getElementById('audioStatus').innerText = isPlaying ? "🎵 재생 중..." : "정지됨";
    if (isPlaying) {
        // 간단한 웹 오디오 API 사운드 연동 시뮬레이션
        setTimeout(() => {
            if(isPlaying) toggleAudio();
        }, 5000);
    }
}

window.addEventListener('resize', resizeCanvas);
window.onload = resizeCanvas;
</script>

</body>
</html>
"""

components.html(HTML, height=750, scrolling=True)
