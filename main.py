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
*{box-sizing:border-box}
body{margin:0;background:#080b14;color:#eef2ff;font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.wrap{max-width:1400px;margin:auto;padding:24px}
.hero{padding:22px 24px;border:1px solid #222a40;border-radius:22px;background:linear-gradient(135deg,#10172a,#0a0d17);margin-bottom:18px}
.logo{font-size:34px;font-weight:900;letter-spacing:-1px}
.sub{color:#98a2bd;margin-top:6px}
.grid{display:grid;grid-template-columns:1.25fr .75fr;gap:18px}
.card{background:#0e1320;border:1px solid #222a40;border-radius:18px;padding:18px}
.card h2{margin:0 0 12px;font-size:18px}
canvas{width:100%;height:430px;background:#070a12;border-radius:14px;border:1px solid #202940;display:block}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
input,select,button{font:inherit}
input,select{width:100%;padding:11px 12px;border-radius:10px;border:1px solid #303a55;background:#0a0e19;color:#fff;outline:none}
input:focus,select:focus{border-color:#7c8cff}
button{border:0;border-radius:10px;padding:11px 14px;background:#202a43;color:#fff;cursor:pointer;font-weight:700}
button:hover{filter:brightness(1.18)}
.primary{background:#6d5dfc}
.danger{background:#a83b55}
.full{grid-column:1/-1}
.row{display:flex;gap:8px;flex-wrap:wrap}
.small{font-size:12px;color:#8792ad}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px}
.stat{padding:10px;border-radius:10px;background:#0a0e19;border:1px solid #202940}
.stat b{display:block;font-size:15px;margin-top:4px}
.layers{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.layer{padding:11px;border:1px solid #242e48;border-radius:11px;background:#0a0e19}
.layer label{display:flex;gap:8px;align-items:center;font-size:13px}
.layer input[type=range]{padding:0;margin-top:7px}
.timeline{height:18px;background:#080b12;border-radius:10px;overflow:hidden;border:1px solid #252d43;margin-top:10px}
#playbar{height:100%;width:0%;background:linear-gradient(90deg,#6d5dfc,#45d5ff)}
.pad{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-top:10px}
.pad button{padding:9px 4px}
.status{padding:10px;border-radius:10px;background:#0a0e19;border:1px solid #202940;color:#aeb8d0;margin-top:10px}
.sketchWrap{position:relative}
#sketch{cursor:crosshair}
.badge{display:inline-block;padding:5px 9px;border-radius:999px;background:#191f34;color:#b9c2ff;font-size:12px;margin-right:5px}
.eq{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#7ee7ff;word-break:break-all}
@media(max-width:900px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:1fr 1fr}.layers{grid-template-columns:1fr}}
.graphWrap {
    position: relative;
    width: 100%;
    max-width: 1000px;
    margin: 0 auto;
}

.graphWrap canvas {
    display: block;
    width: 100%;
    height: auto;
}

#playhead {
    position: absolute;
    left: 0;
    top: 0;
    pointer-events: none;
}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <div class="logo">☄️ Cosmos</div>
    <div class="sub">Mathematical structures → musical structures · Interactive Math to Music Studio</div>
    <div style="margin-top:12px">
      <span class="badge">GRAPH</span><span class="badge">MELODY</span><span class="badge">DRUMS</span>
      <span class="badge">BASS</span><span class="badge">CHORDS</span><span class="badge">SKETCH → FUNCTION</span>
    </div>
  </div>

  <div class="grid">
    <section class="card">
      <h2>📈 Graph Lab</h2><div class="graphWrap">
<canvas id="graph" width="1000" height="560"></canvas>
<canvas id="playhead" width="1000" height="560"></canvas>
</div>
      <div class="controls">
        <div>
          <div class="small">함수</div>
          <input id="expr" value="sin(x)" spellcheck="false">
        </div>
        <div>
          <div class="small">x 범위</div>
          <input id="xr" value="-12, 12">
        </div>
      </div>
      <div class="row" style="margin-top:10px">
        <button class="primary" onclick="drawGraph()">그래프 그리기</button>
        <button onclick="resetView()">기본 범위</button>
        <button onclick="addText('7')">7</button><button onclick="addText('x')">x</button>
        <button onclick="addText('+')">+</button><button onclick="backspace()">⌫</button>
        <button onclick="addText('sin(')">sin(</button><button onclick="addText('cos(')">cos(</button>
      </div>
      <div class="stats">
        <div class="stat">최솟값<b id="minv">-</b></div>
        <div class="stat">최댓값<b id="maxv">-</b></div>
        <div class="stat">평균<b id="avgv">-</b></div>
        <div class="stat">원점<b id="origin">표시</b></div>
      </div>
    </section>

    <section class="card">
      <h2>🎛️ Music Studio</h2>
      <div class="controls">
        <div><div class="small">곡 길이</div>
          <select id="duration">
            <option value="30">30초</option><option value="60">1분</option>
            <option value="120">2분</option><option value="180" selected>3분</option>
            <option value="300">5분</option>
          </select>
        </div>
        <div><div class="small">BPM</div>
          <select id="bpm"><option>80</option><option selected>100</option><option>120</option><option>140</option><option>160</option>
          </select>
        </div>
        <div><div class="small">스타일</div>
          <select id="genre">
            <option>Pop</option><option>K-pop inspired</option><option>J-pop inspired</option>
            <option>Lo-fi</option><option>EDM</option>
          </select>
        </div>
        <div><div class="small">음계</div>
          <select id="scale"><option>C Major</option><option>A Minor</option><option>Pentatonic</option><option>Chromatic</option></select>
        </div>
      </div>

      <h2 style="margin-top:18px">🎚️ 레이어</h2>
      <div class="layers">
        <div class="layer"><label><input id="melodyOn" type="checkbox" checked> 그래프 멜로디</label><input id="melVol" type="range" min="0" max="1" step=".01" value=".42"></div>
        <div class="layer"><label><input id="drumOn" type="checkbox" checked> 드럼</label><input id="drumVol" type="range" min="0" max="1" step=".01" value=".28"></div>
        <div class="layer"><label><input id="bassOn" type="checkbox" checked> 베이스</label><input id="bassVol" type="range" min="0" max="1" step=".01" value=".25"></div>
        <div class="layer"><label><input id="chordOn" type="checkbox" checked> 코드</label><input id="chordVol" type="range" min="0" max="1" step=".01" value=".18"></div>
        <div class="layer"><label><input id="arpOn" type="checkbox"> 아르페지오</label><input id="arpVol" type="range" min="0" max="1" step=".01" value=".15"></div>
        <div class="layer"><label><input id="percOn" type="checkbox" checked> 퍼커션</label><input id="percVol" type="range" min="0" max="1" step=".01" value=".12"></div>
      </div>

      <div class="timeline"><div id="playbar"></div></div>
      <div class="row" style="margin-top:12px">
        <button class="primary" onclick="startMusic()">▶ 음악 생성·재생</button>
        <button class="danger" onclick="stopMusic()">■ 정지</button>
      </div>
      <div class="status" id="musicStatus">그래프를 그린 뒤 음악을 생성해 보세요.</div>
    </section>

    <section class="card full">
      <h2>✏️ Sketch → Function</h2>
      <div class="small">마우스로 곡선을 그리면 좌표를 수집하고 3차 다항식으로 근사합니다. 근사된 식은 아래에 표시되며 그래프에 적용할 수 있습니다.</div>
      <div class="sketchWrap" style="margin-top:10px"><canvas id="sketch" width="1200" height="360"></canvas></div>
      <div class="row" style="margin-top:10px">
        <button class="primary" onclick="fitSketch()">그린 곡선을 함수로 근사</button>
        <button onclick="clearSketch()">지우기</button>
        <button onclick="applyFit()">근사 함수를 그래프에 적용</button>
      </div>
      <div class="status">근사식: <span class="eq" id="fitEq">아직 없음</span></div>
    </section>
  </div>
</div>

<script>
const G=document.getElementById('graph'), gc=G.getContext('2d');
const S=document.getElementById('sketch'), sc=S.getContext('2d');
let xMin=-12,xMax=12,yMin=-5,yMax=5, samples=[], fitExpression='';
let audioCtx=null, master=null, playing=false, timer=null, nextNote=0, songStart=0, step=0;
const TAU=Math.PI*2;

function addText(t){const e=document.getElementById('expr'); e.focus(); e.setRangeText(t,e.selectionStart,e.selectionEnd,'end')}
function backspace(){const e=document.getElementById('expr');e.focus();let a=e.selectionStart,b=e.selectionEnd;if(a===b&&a>0)a--;e.setRangeText('',a,b,'end')}
function resetView(){xMin=-12;xMax=12;yMin=-5;yMax=5;drawGraph()}
function px(x){return (x-xMin)/(xMax-xMin)*G.width}
function py(y){return G.height-(y-yMin)/(yMax-yMin)*G.height}
function evalExpr(s,x){
  try{
    let q=s.toLowerCase().replaceAll('π','Math.PI').replaceAll('^','**');
    q=q.replace(/\bsin\b/g,'Math.sin').replace(/\bcos\b/g,'Math.cos').replace(/\btan\b/g,'Math.tan');
    q=q.replace(/\bsqrt\b/g,'Math.sqrt').replace(/\blog\b/g,'Math.log10').replace(/\bln\b/g,'Math.log');
    q=q.replace(/\babs\b/g,'Math.abs').replace(/\bexp\b/g,'Math.exp');
    q=q.replace(/(\d)\s*x/g,'$1*x');
    q=q.replace(/x\s*(?=\d)/g,'x*');
    q=q.replace(/\)(?=x|\d)/g,')*');
    return Function('x','"use strict";return ('+q+')')(x);
  }catch(e){return NaN}
}
function drawGrid(){
  gc.clearRect(0,0,G.width,G.height);gc.fillStyle='#070a12';gc.fillRect(0,0,G.width,G.height);
  gc.strokeStyle='#151d31';gc.lineWidth=1;
  for(let i=Math.ceil(xMin);i<=Math.floor(xMax);i++){let X=px(i);gc.beginPath();gc.moveTo(X,0);gc.lineTo(X,G.height);gc.stroke()}
  for(let i=Math.ceil(yMin);i<=Math.floor(yMax);i++){let Y=py(i);gc.beginPath();gc.moveTo(0,Y);gc.lineTo(G.width,Y);gc.stroke()}
  gc.strokeStyle='#59647f';gc.lineWidth=2;
  if(xMin<=0&&xMax>=0){let X=px(0);gc.beginPath();gc.moveTo(X,0);gc.lineTo(X,G.height);gc.stroke()}
  if(yMin<=0&&yMax>=0){let Y=py(0);gc.beginPath();gc.moveTo(0,Y);gc.lineTo(G.width,Y);gc.stroke()}
  gc.fillStyle='#8792ad';gc.font='14px system-ui';
  for(let i=Math.ceil(xMin);i<=Math.floor(xMax);i+=2)gc.fillText(i,px(i)+4,Math.min(G.height-6,py(0)+18));
  for(let i=Math.ceil(yMin);i<=Math.floor(yMax);i+=2)gc.fillText(i,px(0)+6,py(i)-6);
  if(xMin<=0&&xMax>=0&&yMin<=0&&yMax>=0){gc.fillStyle='#ffffff';gc.fillText('(0, 0)',px(0)+8,py(0)-10)}
}
function drawPlayhead(progress){
  if(!samples.length)return;

  const overlay=document.getElementById('playhead');
  const ctx=overlay.getContext('2d');

  ctx.clearRect(0,0,overlay.width,overlay.height);

  const idx=Math.min(
    samples.length-1,
    Math.floor(progress*(samples.length-1))
  );

  const p=samples[idx];
  const X=px(p.x);
  const Y=py(p.y);

  ctx.beginPath();
  ctx.arc(X,Y,9,0,Math.PI*2);
  ctx.fillStyle='#ffffff';
  ctx.fill();

  ctx.beginPath();
  ctx.arc(X,Y,5,0,Math.PI*2);
  ctx.fillStyle='#73d7ff';
  ctx.fill();

  ctx.beginPath();
  ctx.arc(X,Y,13,0,Math.PI*2);
  ctx.strokeStyle='rgba(115,215,255,.35)';
  ctx.lineWidth=2;
  ctx.stroke();
}
function drawGraph(){
  const r=document.getElementById('xr').value.split(',').map(Number);
  if(r.length===2&&Number.isFinite(r[0])&&Number.isFinite(r[1])&&r[0]<r[1]){xMin=r[0];xMax=r[1]}
  samples=[];drawGrid();
  let ys=[];
  for(let i=0;i<1000;i++){
    const x=xMin+(xMax-xMin)*i/999,y=evalExpr(document.getElementById('expr').value,x);
    if(Number.isFinite(y)&&Math.abs(y)<1e5){samples.push({x,y});ys.push(y)}
  }
  if(ys.length){
    const mn=Math.min(...ys),mx=Math.max(...ys),span=Math.max(1,mx-mn);
    yMin=Math.min(yMin,mn-span*.08);yMax=Math.max(yMax,mx+span*.08);
    drawGrid();
    gc.strokeStyle='#73d7ff';gc.lineWidth=4;gc.beginPath();
    let first=true;
    samples.forEach(p=>{const X=px(p.x),Y=py(p.y);if(Y<-1000||Y>G.height+1000){first=true;return}if(first){gc.moveTo(X,Y);first=false}else gc.lineTo(X,Y)});
    gc.stroke();
    document.getElementById('minv').textContent=mn.toFixed(2);
    document.getElementById('maxv').textContent=mx.toFixed(2);
    document.getElementById('avgv').textContent=(ys.reduce((a,b)=>a+b,0)/ys.length).toFixed(2);
  }
}
function hz(note){return 440*Math.pow(2,(note-69)/12)}
const scales={
 'C Major':[0,2,4,5,7,9,11,12],
 'A Minor':[0,2,3,5,7,8,10,12],
 'Pentatonic':[0,2,4,7,9,12],
 'Chromatic':[0,1,2,3,4,5,6,7,8,9,10,11,12]
};
function graphNotes(n){
  if(!samples.length)drawGraph();
  if(!samples.length)return [];
  const vals=samples.map(p=>p.y),mn=Math.min(...vals),mx=Math.max(...vals),span=Math.max(1e-9,mx-mn);
  const scale=scales[document.getElementById('scale').value], out=[];
  for(let i=0;i<n;i++){
    const t=i/(n-1), idx=Math.floor(((Math.sin(t*Math.PI*.35)*.08)+(samples[Math.floor(t*(samples.length-1))].y-mn)/span)*scale.length*1.6);
    const k=Math.max(0,Math.min(scale.length*2-1,idx));
    const octave=Math.floor(k/scale.length);
    const note=60+scale[k%scale.length]+12*octave;
    out.push(note);
  }
  return out;
}
function oscTone(freq,time,dur,type,vol){
  if(!audioCtx||!master)return;
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type=type;o.frequency.setValueAtTime(freq,time);
  g.gain.setValueAtTime(0.0001,time);g.gain.exponentialRampToValueAtTime(Math.max(.0002,vol),time+.012);
  g.gain.exponentialRampToValueAtTime(.0001,time+dur);
  o.connect(g);g.connect(master);o.start(time);o.stop(time+dur+.03);
}
function noise(time,dur,vol,filterFreq){
  if(!audioCtx||!master)return;
  const len=Math.max(1,Math.floor(audioCtx.sampleRate*dur)),buf=audioCtx.createBuffer(1,len,audioCtx.sampleRate),d=buf.getChannelData(0);
  for(let i=0;i<len;i++)d[i]=Math.random()*2-1;
  const src=audioCtx.createBufferSource(),f=audioCtx.createBiquadFilter(),g=audioCtx.createGain();
  src.buffer=buf;f.type='lowpass';f.frequency.value=filterFreq;
  g.gain.setValueAtTime(Math.max(.0001,vol),time);g.gain.exponentialRampToValueAtTime(.0001,time+dur);
  src.connect(f);f.connect(g);g.connect(master);src.start(time);src.stop(time+dur+.02);
}
function chordFor(step){
  const pattern=[0,3,5,4,0,3,4,5];
  return pattern[Math.floor(step/8)%pattern.length];
}
function scheduleStep(t,i,notes,bpm,genre){
  const beat=60/bpm;
  const root=48+[0,5,7,3][chordFor(i)];
  if(document.getElementById('drumOn').checked){
    const dv=+document.getElementById('drumVol').value;
    noise(t,.08,dv*(i%4===0?.9:.55),genre==='EDM'?2600:1900);
    if(i%2===1)noise(t+beat*.5,.10,dv*.7,3200);
    if(i%4===2)noise(t+beat*.5,.045,dv*.35,7000);
  }
  if(document.getElementById('percOn').checked&&i%2===0){
    noise(t+beat*.25,.035,+document.getElementById('percVol').value*.7,6000);
  }
  if(document.getElementById('bassOn').checked){
    const bv=+document.getElementById('bassVol').value;
    oscTone(hz(root),t,beat*.8,'triangle',bv);
    if(i%4===3)oscTone(hz(root+7),t+beat*.5,beat*.35,'triangle',bv*.7);
  }
  if(document.getElementById('chordOn').checked&&i%4===0){
    const cv=+document.getElementById('chordVol').value;
    [root+12,root+16,root+19].forEach((nn,j)=>oscTone(hz(nn),t,beat*3.4,'sine',cv/(j+1)*1.5));
  }
  if(document.getElementById('arpOn').checked){
    const av=+document.getElementById('arpVol').value;
    [root+24,root+28,root+31,root+36].forEach((nn,j)=>oscTone(hz(nn),t+j*beat*.25,beat*.22,'sine',av));
  }
  if(document.getElementById('melodyOn').checked&&notes.length){
    const mv=+document.getElementById('melVol').value;
    oscTone(hz(notes[i%notes.length]),t,beat*.72,'sawtooth',mv);
  }
}
function startMusic(){
  stopMusic();
  drawGraph();
  const duration=+document.getElementById('duration').value,bpm=+document.getElementById('bpm').value,genre=document.getElementById('genre').value;
  const totalSteps=Math.ceil(duration/(60/bpm));
  const notes=graphNotes(Math.min(900,totalSteps));
  audioCtx=new (window.AudioContext||window.webkitAudioContext)();
  master=audioCtx.createGain();master.gain.value=.75;master.connect(audioCtx.destination);
  playing=true;nextNote=audioCtx.currentTime+.08;songStart=nextNote;step=0;
  document.getElementById('musicStatus').textContent=`${genre} 스타일 · ${duration}초 · ${bpm} BPM · 그래프 구조를 멜로디로 변환 중`;
  timer=setInterval(()=>{
    if(!playing)return;
    const now=audioCtx.currentTime;
    while(nextNote<now+.8&&step<totalSteps){
      scheduleStep(nextNote,step,notes,bpm,genre);
      nextNote+=60/bpm;step++;
    }
    const elapsed=Math.max(0,now-songStart),pct=Math.min(100,elapsed/duration*100);
    document.getElementById('playbar').style.width=pct+'%';
    drawPlayhead(Math.min(1, elapsed/duration));
    if(elapsed>=duration||step>=totalSteps)stopMusic(false);
  },80);
}
function stopMusic(show=true){
  playing=false;
  if(timer){clearInterval(timer);timer=null}
  if(audioCtx){try{audioCtx.close()}catch(e){}audioCtx=null;master=null}
  document.getElementById('playbar').style.width='0%';
  if(show)document.getElementById('musicStatus').textContent='재생을 정지했습니다.';
}

let drawing=false;
S.addEventListener('pointerdown',e=>{drawing=true;sc.clearRect(0,0,S.width,S.height);drawSketchGrid();sketchPoint(e)})
S.addEventListener('pointermove',e=>{if(drawing)sketchPoint(e)})
window.addEventListener('pointerup',()=>drawing=false);
function drawSketchGrid(){sc.fillStyle='#070a12';sc.fillRect(0,0,S.width,S.height);sc.strokeStyle='#182139';for(let x=0;x<S.width;x+=60){sc.beginPath();sc.moveTo(x,0);sc.lineTo(x,S.height);sc.stroke()}for(let y=0;y<S.height;y+=45){sc.beginPath();sc.moveTo(0,y);sc.lineTo(S.width,y);sc.stroke()}sc.strokeStyle='#59647f';sc.beginPath();sc.moveTo(0,S.height/2);sc.lineTo(S.width,S.height/2);sc.stroke()}
let pts=[];
function sketchPoint(e){
  const r=S.getBoundingClientRect(),x=(e.clientX-r.left)*S.width/r.width,y=(e.clientY-r.top)*S.height/r.height;
  if(!pts.length)drawSketchGrid();
  pts.push({x,y});
  if(pts.length>1){const a=pts[pts.length-2],b=pts[pts.length-1];sc.strokeStyle='#7ee7ff';sc.lineWidth=4;sc.beginPath();sc.moveTo(a.x,a.y);sc.lineTo(b.x,b.y);sc.stroke()}
}
function clearSketch(){pts=[];fitExpression='';sc.clearRect(0,0,S.width,S.height);drawSketchGrid();document.getElementById('fitEq').textContent='아직 없음'}
function solve(A,b){
  const n=b.length,M=A.map((r,i)=>r.slice().concat([b[i]]));
  for(let i=0;i<n;i++){let p=i;for(let j=i+1;j<n;j++)if(Math.abs(M[j][i])>Math.abs(M[p][i]))p=j;[M[i],M[p]]=[M[p],M[i]];if(Math.abs(M[i][i])<1e-10)return null;for(let j=i+1;j<n;j++){let q=M[j][i]/M[i][i];for(let k=i;k<=n;k++)M[j][k]-=q*M[i][k]}}
  const x=new Array(n).fill(0);for(let i=n-1;i>=0;i--){let s=M[i][n];for(let j=i+1;j<n;j++)s-=M[i][j]*x[j];x[i]=s/M[i][i]}return x;
}
function fitSketch(){
  if(pts.length<8){document.getElementById('fitEq').textContent='점을 조금 더 그려 주세요.';return}
  const chosen=[];for(let i=0;i<pts.length;i+=Math.max(1,Math.floor(pts.length/80)))chosen.push(pts[i]);
  const ATA=Array.from({length:4},()=>Array(4).fill(0)),ATb=Array(4).fill(0);
  chosen.forEach(p=>{
    const x=p.x/S.width*24-12,y=(S.height/2-p.y)/(S.height/2)*5,row=[1,x,x*x,x*x*x];
    for(let i=0;i<4;i++){ATb[i]+=row[i]*y;for(let j=0;j<4;j++)ATA[i][j]+=row[i]*row[j]}
  });
  const c=solve(ATA,ATb);if(!c)return;
  const f=v=>c[0]+c[1]*v+c[2]*v*v+c[3]*v*v*v;
  const term=(v,pow)=>{if(Math.abs(v)<.0005)return '';const sign=v>=0?'+':'-';const num=Math.abs(v).toFixed(3).replace(/\.?0+$/,'');return `${sign}${num}${pow?'x'+(pow===2?'²':'³'):''}`};
  fitExpression=(c[0].toFixed(3)+term(c[1],1)+term(c[2],2)+term(c[3],3)).replace(/^1\.000/,'1');
  document.getElementById('fitEq').textContent='y = '+fitExpression;
  sc.strokeStyle='#ffcf6e';sc.lineWidth=3;sc.beginPath();
  for(let i=0;i<S.width;i++){let x=i/S.width*24-12,y=f(x),Y=S.height/2-y/(5)*S.height/2;if(i===0)sc.moveTo(i,Y);else sc.lineTo(i,Y)}sc.stroke();
}
function applyFit(){if(!fitExpression)return;document.getElementById('expr').value=fitExpression.replaceAll('²','**2').replaceAll('³','**3');drawGraph()}
drawSketchGrid();drawGraph();
</script>
</body>
</html>
"""

components.html(HTML, height=1500, scrolling=True)
