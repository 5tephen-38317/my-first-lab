import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos — Math to Music Studio",
    page_icon="🎵",
    layout="wide",
)

HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Cosmos</title>

<style>
*{
    box-sizing:border-box;
}

body{
    margin:0;
    background:#080b14;
    color:#eef2ff;
    font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}

.wrap{
    max-width:1400px;
    margin:auto;
    padding:24px;
}

.hero{
    padding:22px 24px;
    border:1px solid #222a40;
    border-radius:22px;
    background:linear-gradient(135deg,#10172a,#0a0d17);
    margin-bottom:18px;
}

.logo{
    font-size:34px;
    font-weight:900;
    letter-spacing:-1px;
}

.sub{
    color:#98a2bd;
    margin-top:6px;
}

.grid{
    display:grid;
    grid-template-columns:1.25fr .75fr;
    gap:18px;
}

.card{
    background:#0e1320;
    border:1px solid #222a40;
    border-radius:18px;
    padding:18px;
}

.card h2{
    margin:0 0 12px;
    font-size:18px;
}

.controls{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
    margin-top:12px;
}

input,select,button{
    font:inherit;
}

input,select{
    width:100%;
    padding:11px 12px;
    border-radius:10px;
    border:1px solid #303a55;
    background:#0a0e19;
    color:#fff;
    outline:none;
}

input:focus,select:focus{
    border-color:#7c8cff;
}

button{
    border:0;
    border-radius:10px;
    padding:11px 14px;
    background:#202a43;
    color:#fff;
    cursor:pointer;
    font-weight:700;
}

button:hover{
    filter:brightness(1.18);
}

.primary{
    background:#6d5dfc;
}

.danger{
    background:#a83b55;
}

.full{
    grid-column:1/-1;
}

.row{
    display:flex;
    gap:8px;
    flex-wrap:wrap;
}

.small{
    font-size:12px;
    color:#8792ad;
}

.stats{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:8px;
    margin-top:10px;
}

.stat{
    padding:10px;
    border-radius:10px;
    background:#0a0e19;
    border:1px solid #202940;
}

.stat b{
    display:block;
    font-size:15px;
    margin-top:4px;
}

.layers{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.layer{
    padding:11px;
    border:1px solid #242e48;
    border-radius:11px;
    background:#0a0e19;
}

.layer label{
    display:flex;
    gap:8px;
    align-items:center;
    font-size:13px;
}

.layer input[type=range]{
    padding:0;
    margin-top:7px;
}

.timeline{
    height:18px;
    background:#080b12;
    border-radius:10px;
    overflow:hidden;
    border:1px solid #252d43;
    margin-top:10px;
}

#playbar{
    height:100%;
    width:0%;
    background:linear-gradient(90deg,#6d5dfc,#45d5ff);
}

.pad{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:6px;
    margin-top:10px;
}

.pad button{
    padding:9px 4px;
}

.status{
    padding:10px;
    border-radius:10px;
    background:#0a0e19;
    border:1px solid #202940;
    color:#aeb8d0;
    margin-top:10px;
}

.sketchWrap{
    position:relative;
}

#sketch{
    cursor:crosshair;
}

.badge{
    display:inline-block;
    padding:5px 9px;
    border-radius:999px;
    background:#191f34;
    color:#b9c2ff;
    font-size:12px;
    margin-right:5px;
}

.eq{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
    color:#7ee7ff;
    word-break:break-all;
}

.graphWrap{
    position:relative;
    width:100%;
    max-width:1000px;
    margin:0 auto;
}

.graphWrap canvas{
    display:block;
    width:100%;
    height:auto;
}

#playhead{
    position:absolute;
    left:0;
    top:0;
    pointer-events:none;
}

@media(max-width:900px){
    .grid{
        grid-template-columns:1fr;
    }

    .stats{
        grid-template-columns:1fr 1fr;
    }

    .layers{
        grid-template-columns:1fr;
    }
}
</style>
</head>

<body>

<div class="wrap">

    <div class="hero">
        <div class="logo">☄️ Cosmos</div>

        <div class="sub">
            Mathematical structures → musical structures · Interactive Math to Music Studio
        </div>

        <div style="margin-top:12px">
            <span class="badge">GRAPH</span>
            <span class="badge">MELODY</span>
            <span class="badge">DRUMS</span>
            <span class="badge">BASS</span>
            <span class="badge">CHORDS</span>
            <span class="badge">SKETCH → FUNCTION</span>
        </div>
    </div>


    <div class="grid">

        <section class="card">

            <h2>📈 Graph Lab</h2>

            <div class="graphWrap">
                <canvas id="graph" width="1000" height="560"></canvas>
                <canvas id="playhead" width="1000" height="560"></canvas>
            </div>

            <div class="controls">

                <div>
                    <div class="small">함수</div>
                    <input
                        id="expr"
                        value="sin(x)"
                        spellcheck="false"
                    >
                </div>

                <div>
                    <div class="small">x 범위</div>
                    <input
                        id="xr"
                        value="-12, 12"
                    >
                </div>

            </div>

            <div class="row" style="margin-top:10px">

                <button class="primary" onclick="drawGraph()">
                    그래프 그리기
                </button>

                <button onclick="resetView()">
                    기본 범위
                </button>

                <button onclick="addText('7')">7</button>
                <button onclick="addText('x')">x</button>
                <button onclick="addText('+')">+</button>
                <button onclick="backspace()">⌫</button>
                <button onclick="addText('sin(')">sin(</button>
                <button onclick="addText('cos(')">cos(</button>

            </div>

            <div class="stats">

                <div class="stat">
                    최솟값
                    <b id="minv">-</b>
                </div>

                <div class="stat">
                    최댓값
                    <b id="maxv">-</b>
                </div>

                <div class="stat">
                    평균
                    <b id="avgv">-</b>
                </div>

                <div class="stat">
                    원점
                    <b id="origin">표시</b>
                </div>

            </div>

        </section>


        <section class="card">

            <h2>🎛️ Music Studio</h2>

            <div class="controls">

                <div>
                    <div class="small">곡 길이</div>

                    <select id="duration">
                        <option value="30">30초</option>
                        <option value="60">1분</option>
                        <option value="120">2분</option>
                        <option value="180" selected>3분</option>
                        <option value="300">5분</option>
                    </select>
                </div>


                <div>
                    <div class="small">BPM</div>

                    <select id="bpm">
                        <option>80</option>
                        <option selected>100</option>
                        <option>120</option>
                        <option>140</option>
                        <option>160</option>
                    </select>
                </div>


                <div>
                    <div class="small">스타일</div>

                    <select id="genre">
                        <option>Pop</option>
                        <option>K-pop inspired</option>
                        <option>J-pop inspired</option>
                        <option>Lo-fi</option>
                        <option>EDM</option>
                    </select>
                </div>


                <div>
                    <div class="small">음계</div>

                    <select id="scale">
                        <option>C Major</option>
                        <option>A Minor</option>
                        <option>Pentatonic</option>
                        <option>Chromatic</option>
                    </select>
                </div>

            </div>


            <h2 style="margin-top:18px">
                🎚️ 레이어
            </h2>


            <div class="layers">

                <div class="layer">
                    <label>
                        <input id="melodyOn" type="checkbox" checked>
                        그래프 멜로디
                    </label>

                    <input
                        id="melVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".42"
                    >
                </div>


                <div class="layer">
                    <label>
                        <input id="drumOn" type="checkbox" checked>
                        드럼
                    </label>

                    <input
                        id="drumVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".28"
                    >
                </div>


                <div class="layer">
                    <label>
                        <input id="bassOn" type="checkbox" checked>
                        베이스
                    </label>

                    <input
                        id="bassVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".25"
                    >
                </div>


                <div class="layer">
                    <label>
                        <input id="chordOn" type="checkbox" checked>
                        코드
                    </label>

                    <input
                        id="chordVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".18"
                    >
                </div>


                <div class="layer">
                    <label>
                        <input id="arpOn" type="checkbox">
                        아르페지오
                    </label>

                    <input
                        id="arpVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".15"
                    >
                </div>


                <div class="layer">
                    <label>
                        <input id="percOn" type="checkbox" checked>
                        퍼커션
                    </label>

                    <input
                        id="percVol"
                        type="range"
                        min="0"
                        max="1"
                        step=".01"
                        value=".12"
                    >
                </div>

            </div>


            <div class="timeline">
                <div id="playbar"></div>
            </div>


            <div class="row" style="margin-top:12px">

                <button
                    class="primary"
                    onclick="startMusic()"
                >
                    ▶ 음악 생성·재생
                </button>

                <button
                    class="danger"
                    onclick="stopMusic()"
                >
                    ■ 정지
                </button>

            </div>


            <div class="status" id="musicStatus">
                그래프를 그린 뒤 음악을 생성해 보세요.
            </div>

        </section>


        <section class="card full">

            <h2>✏️ Sketch → Function</h2>

            <div class="small">
                마우스로 곡선을 그리면 좌표를 수집하고
                3차 다항식으로 근사합니다.
                근사된 식은 아래에 표시되며 그래프에 적용할 수 있습니다.
            </div>


            <div
                class="sketchWrap"
                style="margin-top:10px"
            >
                <canvas
                    id="sketch"
                    width="1200"
                    height="360"
                ></canvas>
            </div>


            <div
                class="row"
                style="margin-top:10px"
            >

                <button
                    class="primary"
                    onclick="fitSketch()"
                >
                    그린 곡선을 함수로 근사
                </button>

                <button onclick="clearSketch()">
                    지우기
                </button>

                <button onclick="applyFit()">
                    근사 함수를 그래프에 적용
                </button>

            </div>


            <div class="status">
                근사식:
                <span
                    class="eq"
                    id="fitEq"
                >
                    아직 없음
                </span>
            </div>

        </section>

    </div>
</div>


<script>

const G = document.getElementById('graph');
const gc = G.getContext('2d');

const S = document.getElementById('sketch');
const sc = S.getContext('2d');

let xMin = -12;
let xMax = 12;

let yMin = -5;
let yMax = 5;

/*
   실제 함수의 데이터 범위.
   화면용 yMin/yMax와 분리한다.
*/
let dataYMin = -1;
let dataYMax = 1;

let samples = [];
let fitExpression = '';

let audioCtx = null;
let master = null;

let playing = false;
let timer = null;

let nextNote = 0;
let songStart = 0;
let step = 0;

const TAU = Math.PI * 2;


/* =========================
   입력
========================= */

function addText(t){

    const e = document.getElementById('expr');

    e.focus();

    e.setRangeText(
        t,
        e.selectionStart,
        e.selectionEnd,
        'end'
    );
}


function backspace(){

    const e = document.getElementById('expr');

    e.focus();

    let a = e.selectionStart;
    let b = e.selectionEnd;

    if(a === b && a > 0){
        a--;
    }

    e.setRangeText('',a,b,'end');
}


function resetView(){

    xMin = -12;
    xMax = 12;

    yMin = -5;
    yMax = 5;

    drawGraph();
}


/* =========================
   좌표
========================= */

function px(x){

    return (
        (x - xMin) /
        (xMax - xMin) *
        G.width
    );
}


function py(y){

    return (
        G.height -
        (y - yMin) /
        (yMax - yMin) *
        G.height
    );
}


/* =========================
   함수 계산
========================= */

function evalExpr(s,x){

    try{

        let q = s
            .toLowerCase()
            .replaceAll('π','Math.PI')
            .replaceAll('^','**');

        q = q.replace(/\bsin\b/g,'Math.sin');
        q = q.replace(/\bcos\b/g,'Math.cos');
        q = q.replace(/\btan\b/g,'Math.tan');
        q = q.replace(/\bsqrt\b/g,'Math.sqrt');
        q = q.replace(/\blog\b/g,'Math.log10');
        q = q.replace(/\bln\b/g,'Math.log');
        q = q.replace(/\babs\b/g,'Math.abs');
        q = q.replace(/\bexp\b/g,'Math.exp');

        q = q.replace(/(\d)\s*x/g,'$1*x');
        q = q.replace(/x\s*(?=\d)/g,'x*');
        q = q.replace(/\)(?=x|\d)/g,')*');

        return Function(
            'x',
            '"use strict";return (' + q + ')'
        )(x);

    }catch(e){

        return NaN;
    }
}


/* =========================
   그래프 배경
========================= */

function drawGrid(){

    gc.clearRect(
        0,
        0,
        G.width,
        G.height
    );

    gc.fillStyle = '#070a12';

    gc.fillRect(
        0,
        0,
        G.width,
        G.height
    );


    gc.strokeStyle = '#151d31';
    gc.lineWidth = 1;


    for(
        let i = Math.ceil(xMin);
        i <= Math.floor(xMax);
        i++
    ){

        const X = px(i);

        gc.beginPath();
        gc.moveTo(X,0);
        gc.lineTo(X,G.height);
        gc.stroke();
    }


    for(
        let i = Math.ceil(yMin);
        i <= Math.floor(yMax);
        i++
    ){

        const Y = py(i);

        gc.beginPath();
        gc.moveTo(0,Y);
        gc.lineTo(G.width,Y);
        gc.stroke();
    }


    gc.strokeStyle = '#59647f';
    gc.lineWidth = 2;


    if(xMin <= 0 && xMax >= 0){

        const X = px(0);

        gc.beginPath();
        gc.moveTo(X,0);
        gc.lineTo(X,G.height);
        gc.stroke();
    }


    if(yMin <= 0 && yMax >= 0){

        const Y = py(0);

        gc.beginPath();
        gc.moveTo(0,Y);
        gc.lineTo(G.width,Y);
        gc.stroke();
    }


    gc.fillStyle = '#8792ad';
    gc.font = '14px system-ui';


    for(
        let i = Math.ceil(xMin);
        i <= Math.floor(xMax);
        i += 2
    ){

        gc.fillText(
            i,
            px(i) + 4,
            Math.min(
                G.height - 6,
                py(0) + 18
            )
        );
    }


    for(
        let i = Math.ceil(yMin);
        i <= Math.floor(yMax);
        i += 2
    ){

        gc.fillText(
            i,
            px(0) + 6,
            py(i) - 6
        );
    }


    if(
        xMin <= 0 &&
        xMax >= 0 &&
        yMin <= 0 &&
        yMax >= 0
    ){

        gc.fillStyle = '#ffffff';

        gc.fillText(
            '(0, 0)',
            px(0) + 8,
            py(0) - 10
        );
    }
}


/* =========================
   그래프
========================= */

function drawGraph(){

    const r =
        document
        .getElementById('xr')
        .value
        .split(',')
        .map(Number);


    if(
        r.length === 2 &&
        Number.isFinite(r[0]) &&
        Number.isFinite(r[1]) &&
        r[0] < r[1]
    ){

        xMin = r[0];
        xMax = r[1];
    }


    samples = [];

    drawGrid();


    const expr =
        document
        .getElementById('expr')
        .value;


    let ys = [];


    for(
        let i = 0;
        i < 1000;
        i++
    ){

        const x =
            xMin +
            (xMax - xMin) *
            i / 999;


        const y =
            evalExpr(
                expr,
                x
            );


        if(
            Number.isFinite(y) &&
            Math.abs(y) < 1e5
        ){

            samples.push({
                x:x,
                y:y
            });

            ys.push(y);
        }
    }


    if(ys.length === 0){

        document.getElementById('minv').textContent = '-';
        document.getElementById('maxv').textContent = '-';
        document.getElementById('avgv').textContent = '-';

        return;
    }


    const mn = Math.min(...ys);
    const mx = Math.max(...ys);

    /* 실제 함수 범위 저장 */
    dataYMin = mn;
    dataYMax = mx;


    const span =
        Math.max(
            1,
            mx - mn
        );


    yMin =
        mn -
        span * 0.15;

    yMax =
        mx +
        span * 0.15;


    drawGrid();


    gc.strokeStyle = '#73d7ff';
    gc.lineWidth = 4;

    gc.beginPath();


    let first = true;


    for(const p of samples){

        const X = px(p.x);
        const Y = py(p.y);


        if(
            Y < -1000 ||
            Y > G.height + 1000
        ){

            first = true;

            continue;
        }


        if(first){

            gc.moveTo(X,Y);

            first = false;

        }else{

            gc.lineTo(X,Y);
        }
    }


    gc.stroke();


    document.getElementById('minv').textContent =
        mn.toFixed(2);

    document.getElementById('maxv').textContent =
        mx.toFixed(2);

    document.getElementById('avgv').textContent =
        (
            ys.reduce(
                (a,b) => a+b,
                0
            ) / ys.length
        ).toFixed(2);


    clearPlayhead();
}


/* =========================
   재생 점
========================= */

function drawPlayhead(progress){

    if(!samples.length){
        return;
    }


    const overlay =
        document.getElementById('playhead');

    const ctx =
        overlay.getContext('2d');


    ctx.clearRect(
        0,
        0,
        overlay.width,
        overlay.height
    );


    const idx =
        Math.min(
            samples.length - 1,
            Math.floor(
                progress *
                (samples.length - 1)
            )
        );


    const p =
        samples[idx];


    const X = px(p.x);
    const Y = py(p.y);


    ctx.beginPath();

    ctx.arc(
        X,
        Y,
        13,
        0,
        Math.PI * 2
    );

    ctx.strokeStyle =
        'rgba(115,215,255,.35)';

    ctx.lineWidth = 2;

    ctx.stroke();


    ctx.beginPath();

    ctx.arc(
        X,
        Y,
        9,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = '#ffffff';

    ctx.fill();


    ctx.beginPath();

    ctx.arc(
        X,
        Y,
        5,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = '#73d7ff';

    ctx.fill();
}


function clearPlayhead(){

    const overlay =
        document.getElementById('playhead');

    if(!overlay){
        return;
    }

    const ctx =
        overlay.getContext('2d');

    ctx.clearRect(
        0,
        0,
        overlay.width,
        overlay.height
    );
}


/* =========================
   음악 시작
========================= */

function startMusic(){

    if(!samples.length){
        drawGraph();
    }


    if(!samples.length){

        document.getElementById(
            'musicStatus'
        ).textContent =
            '먼저 올바른 함수를 입력하고 그래프를 그려 주세요.';

        return;
    }


    stopMusic(false);


    audioCtx =
        new (
            window.AudioContext ||
            window.webkitAudioContext
        )();


    master =
        audioCtx.createGain();


    master.gain.value = 0.22;

    master.connect(
        audioCtx.destination
    );


    const duration =
        Number(
            document.getElementById(
                'duration'
            ).value
        );


    playing = true;

    step = 0;

    songStart =
        audioCtx.currentTime;

    nextNote =
        songStart;


    document.getElementById(
        'musicStatus'
    ).textContent =
        '▶ 그래프의 형태를 따라 음정이 변화하는 중입니다.';


    timer =
        setInterval(
            scheduler,
            50
        );
}


/* =========================
   스케줄러
========================= */

function scheduler(){

    if(!playing || !audioCtx){
        return;
    }


    const bpm =
        Number(
            document.getElementById(
                'bpm'
            ).value
        );


    const beat =
        60 / bpm;


    /*
       기존 beat/2보다 촘촘하게 만든다.

       그래프를 음악으로 변환할 때
       더 많은 지점을 사용해야
       함수의 곡선이 음정 변화에
       더 정확하게 반영된다.
    */
    const stepDuration =
        beat / 4;


    const now =
        audioCtx.currentTime;


    while(
        nextNote <
        now + 0.20
    ){

        scheduleStep(
            nextNote,
            step
        );


        nextNote += stepDuration;

        step++;


        if(step > 100000){
            break;
        }
    }


    const duration =
        Number(
            document.getElementById(
                'duration'
            ).value
        );


    const elapsed =
        Math.max(
            0,
            now - songStart
        );


    const pct =
        Math.min(
            100,
            elapsed /
            duration *
            100
        );


    document.getElementById(
        'playbar'
    ).style.width =
        pct + '%';


    drawPlayhead(
        Math.min(
            1,
            elapsed / duration
        )
    );


    if(elapsed >= duration){

        stopMusic(false);
    }
}


/* =========================
   MIDI → 주파수
========================= */

function noteFreq(midi){

    return 440 *
        Math.pow(
            2,
            (midi - 69) / 12
        );
}


/* =========================
   그래프 y값 → 음정
========================= */

/*
   핵심 함수.

   함수의 실제 y범위를 3옥타브
   정도의 음역으로 선형 변환한다.

   낮은 y
       ↓
   낮은 음

   높은 y
       ↓
   높은 음

   특정 함수(sin, x, x² 등)를
   따로 처리하지 않는다.
*/

function graphYToFrequency(y){

    let minY = dataYMin;
    let maxY = dataYMax;


    if(!Number.isFinite(minY) ||
       !Number.isFinite(maxY)){

        return noteFreq(60);
    }


    /*
       상수함수 방지
    */

    if(Math.abs(maxY - minY) < 1e-9){

        return noteFreq(60);
    }


    let normalized =
        (y - minY) /
        (maxY - minY);


    normalized =
        Math.max(
            0,
            Math.min(
                1,
                normalized
            )
        );


    /*
       약 3옥타브 범위.

       y 최저 → C3
       y 최고 → C6
    */

    const minMidi = 48;
    const maxMidi = 84;


    const midi =
        minMidi +
        normalized *
        (maxMidi - minMidi);


    /*
       반올림하지 않는다.

       이것이 중요하다.

       기존 코드는 Math.round() 때문에
       그래프의 연속적인 변화가
       피아노 음계의 계단형 변화로
       바뀌었다.

       이제는 MIDI 값을 실수로 유지하여
       주파수가 연속적으로 변한다.
    */

    return noteFreq(midi);
}


/* =========================
   그래프 멜로디
========================= */

function playGraphTone(
    time,
    index,
    duration
){

    if(
        !audioCtx ||
        !master ||
        !samples.length
    ){

        return;
    }


    const p =
        samples[
            index %
            samples.length
        ];


    const next =
        samples[
            Math.min(
                samples.length - 1,
                index + 1
            )
        ];


    const frequency =
        graphYToFrequency(
            p.y
        );


    const nextFrequency =
        graphYToFrequency(
            next.y
        );


    const osc =
        audioCtx.createOscillator();


    const gain =
        audioCtx.createGain();


    /*
       triangle wave는
       그래프의 음정 변화를
       비교적 명확하게 들려준다.
    */

    osc.type = 'triangle';


    /*
       현재 그래프 위치의 y값에서 시작
    */

    osc.frequency.setValueAtTime(
        frequency,
        time
    );


    /*
       다음 그래프 위치의 y값까지
       음정을 부드럽게 이동.

       따라서 sin(x)의 경우
       음도 실제로 올라갔다 내려간다.
    */

    osc.frequency.linearRampToValueAtTime(
        nextFrequency,
        time + duration * 0.95
    );


    const volume =
        Number(
            document.getElementById(
                'melVol'
            ).value
        );


    gain.gain.setValueAtTime(
        0,
        time
    );


    gain.gain.linearRampToValueAtTime(
        volume,
        time + Math.min(
            0.025,
            duration * 0.08
        )
    );


    gain.gain.setValueAtTime(
        volume,
        time + duration * 0.78
    );


    gain.gain.linearRampToValueAtTime(
        0.001,
        time + duration
    );


    osc.connect(gain);
    gain.connect(master);


    osc.start(time);

    osc.stop(
        time + duration + 0.03
    );
}


/* =========================
   실제 스텝
========================= */

function scheduleStep(
    time,
    index
){

    if(!samples.length){
        return;
    }


    const bpm =
        Number(
            document.getElementById(
                'bpm'
            ).value
        );


    const beat =
        60 / bpm;


    const stepDuration =
        beat / 4;


    const p =
        samples[
            index %
            samples.length
        ];


    /*
       그래프 멜로디
       ↓
       함수 y값을 직접 사용
    */

    if(
        document.getElementById(
            'melodyOn'
        ).checked
    ){

        playGraphTone(
            time,
            index,
            stepDuration
        );
    }


    /*
       아래 레이어들은 기존 음악적 배경으로 유지한다.
       메인 멜로디와 달리 그래프를 정확히 따라갈
       필요가 없으므로 기존 구조를 유지한다.
    */

    const normalized =
        Math.max(
            0,
            Math.min(
                1,
                (p.y - dataYMin) /
                Math.max(
                    1e-9,
                    dataYMax - dataYMin
                )
            )
        );


    const beatIndex =
        index % 8;


    /* 베이스 */

    if(
        document.getElementById(
            'bassOn'
        ).checked &&
        beatIndex % 4 === 0
    ){

        playTone(
            noteFreq(
                36 +
                Math.round(
                    normalized * 12
                )
            ),
            time,
            beat * 0.75,
            Number(
                document.getElementById(
                    'bassVol'
                ).value
            ),
            'sine'
        );
    }


    /* 코드 */

    if(
        document.getElementById(
            'chordOn'
        ).checked &&
        beatIndex % 4 === 0
    ){

        const root =
            48 +
            Math.round(
                normalized * 12
            );


        playTone(
            noteFreq(root),
            time,
            beat * 0.9,
            Number(
                document.getElementById(
                    'chordVol'
                ).value
            ),
            'sine'
        );


        playTone(
            noteFreq(root + 4),
            time,
            beat * 0.9,
            Number(
                document.getElementById(
                    'chordVol'
                ).value
            ) * 0.65,
            'sine'
        );


        playTone(
            noteFreq(root + 7),
            time,
            beat * 0.9,
            Number(
                document.getElementById(
                    'chordVol'
                ).value
            ) * 0.55,
            'sine'
        );
    }


    /* 아르페지오 */

    if(
        document.getElementById(
            'arpOn'
        ).checked
    ){

        const root =
            60 +
            Math.round(
                normalized * 12
            );


        playTone(
            noteFreq(
                root +
                (beatIndex % 4) * 4
            ),
            time,
            beat * 0.35,
            Number(
                document.getElementById(
                    'arpVol'
                ).value
            ),
            'triangle'
        );
    }


    /* 드럼 */

    if(
        document.getElementById(
            'drumOn'
        ).checked
    ){

        if(beatIndex % 4 === 0){

            playKick(
                time,
                Number(
                    document.getElementById(
                        'drumVol'
                    ).value
                )
            );

        }else if(beatIndex % 4 === 2){

            playSnare(
                time,
                Number(
                    document.getElementById(
                        'drumVol'
                    ).value
                )
            );
        }
    }


    /* 퍼커션 */

    if(
        document.getElementById(
            'percOn'
        ).checked &&
        beatIndex % 2 === 1
    ){

        playHat(
            time,
            Number(
                document.getElementById(
                    'percVol'
                ).value
            )
        );
    }
}


/* =========================
   일반 Tone
========================= */

function playTone(
    frequency,
    time,
    duration,
    volume,
    type='sine'
){

    if(!audioCtx || !master){
        return;
    }


    const osc =
        audioCtx.createOscillator();

    const gain =
        audioCtx.createGain();


    osc.type = type;


    osc.frequency.setValueAtTime(
        frequency,
        time
    );


    gain.gain.setValueAtTime(
        0,
        time
    );


    gain.gain.linearRampToValueAtTime(
        volume,
        time + 0.01
    );


    gain.gain.exponentialRampToValueAtTime(
        0.001,
        time + duration
    );


    osc.connect(gain);
    gain.connect(master);


    osc.start(time);

    osc.stop(
        time + duration + 0.03
    );
}


/* =========================
   드럼
========================= */

function playKick(
    time,
    volume
){

    if(!audioCtx || !master){
        return;
    }


    const osc =
        audioCtx.createOscillator();

    const gain =
        audioCtx.createGain();


    osc.type = 'sine';


    osc.frequency.setValueAtTime(
        120,
        time
    );


    osc.frequency.exponentialRampToValueAtTime(
        45,
        time + 0.12
    );


    gain.gain.setValueAtTime(
        volume,
        time
    );


    gain.gain.exponentialRampToValueAtTime(
        0.001,
        time + 0.16
    );


    osc.connect(gain);
    gain.connect(master);


    osc.start(time);
    osc.stop(time + 0.18);
}


function playNoise(
    time,
    duration,
    volume
){

    if(!audioCtx || !master){
        return;
    }


    const buffer =
        audioCtx.createBuffer(
            1,
            audioCtx.sampleRate * duration,
            audioCtx.sampleRate
        );


    const data =
        buffer.getChannelData(0);


    for(
        let i = 0;
        i < data.length;
        i++
    ){

        data[i] =
            Math.random() * 2 - 1;
    }


    const source =
        audioCtx.createBufferSource();


    const filter =
        audioCtx.createBiquadFilter();


    const gain =
        audioCtx.createGain();


    source.buffer = buffer;

    filter.type = 'highpass';
    filter.frequency.value = 700;


    gain.gain.setValueAtTime(
        volume,
        time
    );


    gain.gain.exponentialRampToValueAtTime(
        0.001,
        time + duration
    );


    source
        .connect(filter)
        .connect(gain)
        .connect(master);


    source.start(time);
}


function playSnare(
    time,
    volume
){

    playNoise(
        time,
        0.16,
        volume
    );
}


function playHat(
    time,
    volume
){

    playNoise(
        time,
        0.055,
        volume * 0.55
    );
}


/* =========================
   정지
========================= */

function stopMusic(
    showStatus = true
){

    playing = false;


    if(timer){

        clearInterval(timer);

        timer = null;
    }


    if(audioCtx){

        try{
            audioCtx.close();
        }catch(e){}
    }


    audioCtx = null;
    master = null;


    document.getElementById(
        'playbar'
    ).style.width = '0%';


    clearPlayhead();


    if(showStatus){

        document.getElementById(
            'musicStatus'
        ).textContent =
            '음악 재생이 정지되었습니다.';
    }
}


/* =========================
   Sketch → Function
========================= */

let drawing = false;
let sketchPoints = [];


function sketchPosition(e){

    const rect =
        S.getBoundingClientRect();


    return {
        x:
            (e.clientX - rect.left) *
            S.width /
            rect.width,

        y:
            (e.clientY - rect.top) *
            S.height /
            rect.height
    };
}


function drawSketchPoint(p){

    sc.lineTo(
        p.x,
        p.y
    );

    sc.stroke();
}


S.addEventListener(
    'pointerdown',
    e => {

        drawing = true;

        sketchPoints = [];


        const p =
            sketchPosition(e);


        sketchPoints.push(p);


        sc.beginPath();

        sc.moveTo(
            p.x,
            p.y
        );

        sc.strokeStyle =
            '#73d7ff';

        sc.lineWidth = 4;

        sc.lineCap = 'round';
    }
);


S.addEventListener(
    'pointermove',
    e => {

        if(!drawing){
            return;
        }


        const p =
            sketchPosition(e);


        sketchPoints.push(p);

        drawSketchPoint(p);
    }
);


window.addEventListener(
    'pointerup',
    () => {

        drawing = false;

        sc.closePath();
    }
);


function clearSketch(){

    sc.clearRect(
        0,
        0,
        S.width,
        S.height
    );


    sketchPoints = [];

    fitExpression = '';


    document.getElementById(
        'fitEq'
    ).textContent =
        '아직 없음';
}


/* =========================
   3차 근사
========================= */

function solve(A,b){

    const n = b.length;

    const M =
        A.map(
            (r,i) =>
                r.slice().concat([b[i]])
        );


    for(
        let i = 0;
        i < n;
        i++
    ){

        let p = i;


        for(
            let j = i + 1;
            j < n;
            j++
        ){

            if(
                Math.abs(M[j][i]) >
                Math.abs(M[p][i])
            ){

                p = j;
            }
        }


        [
            M[i],
            M[p]
        ] =
        [
            M[p],
            M[i]
        ];


        if(
            Math.abs(
                M[i][i]
            ) < 1e-10
        ){

            return null;
        }


        for(
            let j = i + 1;
            j < n;
            j++
        ){

            const q =
                M[j][i] /
                M[i][i];


            for(
                let k = i;
                k <= n;
                k++
            ){

                M[j][k] -=
                    q *
                    M[i][k];
            }
        }
    }


    const x =
        new Array(n).fill(0);


    for(
        let i = n - 1;
        i >= 0;
        i--
    ){

        let s =
            M[i][n];


        for(
            let j = i + 1;
            j < n;
            j++
        ){

            s -=
                M[i][j] *
                x[j];
        }


        x[i] =
            s /
            M[i][i];
    }


    return x;
}


function fitSketch(){

    if(sketchPoints.length < 8){

        document.getElementById(
            'fitEq'
        ).textContent =
            '조금 더 길게 그려 주세요.';

        return;
    }


    const pts =
        sketchPoints.filter(
            (_,i) =>
                i %
                Math.max(
                    1,
                    Math.floor(
                        sketchPoints.length /
                        120
                    )
                ) === 0
        );


    const xs =
        pts.map(
            p =>
                (p.x / S.width) *
                20 - 10
        );


    const ys =
        pts.map(
            p =>
                4 -
                (p.y / S.height) *
                8
        );


    const A =
        Array.from(
            {length:4},
            () => Array(4).fill(0)
        );


    const b =
        Array(4).fill(0);


    for(
        let i = 0;
        i < xs.length;
        i++
    ){

        const x = xs[i];
        const y = ys[i];


        const v =
            [
                1,
                x,
                x*x,
                x*x*x
            ];


        for(
            let r = 0;
            r < 4;
            r++
        ){

            b[r] +=
                v[r] * y;


            for(
                let c = 0;
                c < 4;
                c++
            ){

                A[r][c] +=
                    v[r] * v[c];
            }
        }
    }


    const coef =
        solve(A,b);


    if(!coef){

        document.getElementById(
            'fitEq'
        ).textContent =
            '근사에 실패했습니다.';

        return;
    }


    const [a0,a1,a2,a3] =
        coef;


    function fmt(v){

        return Number(
            v.toFixed(4)
        );
    }


    fitExpression =
        `${fmt(a3)}*x^3+${fmt(a2)}*x^2+${fmt(a1)}*x+${fmt(a0)}`;


    document.getElementById(
        'fitEq'
    ).textContent =
        fitExpression;
}


function applyFit(){

    if(!fitExpression){
        return;
    }


    document.getElementById(
        'expr'
    ).value =
        fitExpression;


    drawGraph();
}


/* =========================
   초기 실행
========================= */

drawGraph();

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=1500,
    scrolling=True
)
