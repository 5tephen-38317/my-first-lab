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
    --accent:#7a5af8;
    --line:#e6e7ec;
}
*{box-sizing:border-box;}
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:var(--bg);
    color:var(--text);
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
    font-weight:bold;
}
.workspace{
    display:grid;
    grid-template-columns:300px 1fr;
    flex:1;
    overflow:hidden;
}
.expressionPane{
    background:#fff;
    border-right:1px solid var(--line);
    padding:12px;
    overflow-y:auto;
}
.graphWorkspace{
    display:flex;
    flex-direction:column;
    background:#fff;
}
.graphCanvasArea{
    flex:1;
    position:relative;
}
canvas{
    width:100%;
    height:100%;
    display:block;
}
</style>
</head>
<body>

<div class="workspaceShell">
    <div class="appToolbar">
        <div>Cosmos - Graph to Music (Desmos Clone)</div>
    </div>
    <div class="workspace">
        <div class="expressionPane">
            <h3>함수 입력</h3>
            <p style="font-size: 12px; color: #666;">원하는 수학 함수를 입력하세요 (예: Math.sin(x)).</p>
            <input type="text" id="funcInput" value="Math.sin(x)" style="width: 100%; padding: 8px; margin-top: 8px;">
        </div>
        <div class="graphWorkspace">
            <div class="graphCanvasArea">
                <canvas id="graphCanvas"></canvas>
            </div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('graphCanvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    drawGraph();
}

function drawGraph() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.strokeStyle = '#7a5af8';
    ctx.lineWidth = 2;

    const width = canvas.width;
    const height = canvas.height;
    const scale = 50;

    for (let px = 0; px < width; px++) {
        let x = (px - width / 2) / scale;
        let y;
        try {
            y = eval(document.getElementById('funcInput').value);
        } catch (e) {
            y = 0;
        }
        let py = height / 2 - y * scale;

        if (px === 0) {
            ctx.moveTo(px, py);
        } else {
            ctx.lineTo(px, py);
        }
    }
    ctx.stroke();
}

window.addEventListener('resize', resizeCanvas);
document.getElementById('funcInput').addEventListener('input', drawGraph);
window.onload = resizeCanvas;
</script>

</body>
</html>
"""

components.html(HTML, height=700, scrolling=True)
