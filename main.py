import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos — Graph to Music",
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


<style>
:root{
    --bg:#f6f7fb;
    --surface:#ffffff;
    --surface-soft:#fbfbfd;
    --text:#17181d;
    --muted:#6f7480;
    --muted-2:#9aa0ab;
    --line:#e6e7ec;
    --line-strong:#d9dbe3;
    --accent:#7a5af8;
    --accent-dark:#6242e5;
    --accent-soft:#f0edff;
    --danger:#b4233c;
    --danger-soft:#fff1f3;
    --success:#167c62;
    --success-soft:#eaf8f3;
    --shadow:0 12px 36px rgba(25, 25, 40, .06);
    --shadow-sm:0 3px 14px rgba(25, 25, 40, .05);
}

*{box-sizing:border-box;}

html{scroll-behavior:smooth;}

body{
    margin:0;
    font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",
        "Noto Sans KR",sans-serif;
    background:var(--bg);
    color:var(--text);
}

button,input,select{font:inherit;}

button{
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    border-radius:9px;
    padding:9px 12px;
    min-height:38px;
    cursor:pointer;
    transition:
        background .16s ease,
        border-color .16s ease,
        color .16s ease,
        transform .16s ease,
        box-shadow .16s ease;
}

button:hover{
    background:#f8f8fb;
    border-color:#c9cbd5;
}

button:active{transform:translateY(1px);}

button.active,
button.primary{
    background:var(--accent);
    border-color:var(--accent);
    color:#fff;
    font-weight:700;
    box-shadow:0 5px 14px rgba(122,90,248,.18);
}

button.active:hover,
button.primary:hover{
    background:var(--accent-dark);
    border-color:var(--accent-dark);
}

button.danger{
    background:var(--danger-soft);
    border-color:#f2c7cf;
    color:var(--danger);
}

button.danger:hover{
    background:#ffe7eb;
    border-color:#e9aeb9;
}

button.success{
    background:var(--success-soft);
    border-color:#b9e5d7;
    color:var(--success);
}

button.success:hover{
    background:#def3eb;
}

button:disabled{
    opacity:.45;
    cursor:not-allowed;
}

#cosmos{
    width:100%;
    max-width:none;
    margin:0;
    padding:10px 12px 12px;
    box-sizing:border-box;
}

/* ---------- brand ---------- */

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:24px;
    margin-bottom:20px;
}

.brand{
    display:flex;
    align-items:center;
    gap:14px;
    min-width:0;
}

.brandMark{
    width:48px;
    height:48px;
    border:1px solid #ddd7ff;
    background:#fff;
    border-radius:14px;
    display:grid;
    place-items:center;
    box-shadow:var(--shadow-sm);
    flex:none;
}

.brandMark svg{
    width:34px;
    height:34px;
    display:block;
}

.brandText{min-width:0;}

.logo{
    font-size:25px;
    line-height:1;
    font-weight:800;
    letter-spacing:-.8px;
}

.logo span{color:var(--accent);}

.subtitle{
    color:var(--muted);
    font-size:13px;
    margin-top:7px;
    line-height:1.5;
}

.brandMeaning{
    display:flex;
    align-items:center;
    gap:7px;
    margin-top:6px;
    color:#8b8797;
    font-size:10px;
    letter-spacing:.08em;
    text-transform:uppercase;
}

.brandMeaning .dot{
    width:4px;
    height:4px;
    border-radius:50%;
    background:#b7adf7;
}

.badge{
    display:inline-flex;
    align-items:center;
    gap:6px;
    padding:7px 10px;
    border:1px solid var(--line);
    border-radius:999px;
    background:#fff;
    color:#6e687f;
    font-size:10px;
    font-weight:700;
    letter-spacing:.04em;
}

.badge::before{
    content:"";
    width:6px;
    height:6px;
    border-radius:50%;
    background:#72c6aa;
}

/* ---------- navigation ---------- */

.topNav{
    display:flex;
    align-items:center;
    gap:5px;
    padding:5px;
    margin-bottom:18px;
    border:1px solid var(--line);
    background:rgba(255,255,255,.84);
    border-radius:12px;
    box-shadow:var(--shadow-sm);
}

.navItem{
    appearance:none;
    -webkit-appearance:none;
    border:0;
    background:transparent;
    color:#707582;
    text-decoration:none;
    font-size:12px;
    font-weight:700;
    padding:8px 12px;
    min-height:34px;
    border-radius:8px;
    cursor:pointer;
    box-shadow:none;
}

.navItem:hover{
    background:#f3f2f8;
    color:var(--text);
    border-color:transparent;
}

.navItem.active,
.navItem.primaryNav{
    background:var(--accent-soft);
    color:#6548db;
}

.navItem.active:hover,
.navItem.primaryNav:hover{
    background:#e9e5ff;
    color:#573bc7;
}

/* ---------- layout ---------- */

.grid{
    display:grid;
    grid-template-columns:minmax(0,1fr) 390px;
    gap:18px;
    align-items:start;
}

.card{
    background:var(--surface);
    border:1px solid var(--line);
    border-radius:16px;
    padding:18px;
    box-shadow:var(--shadow);
}

.card + .card{margin-top:14px;}

.card h2{
    font-size:14px;
    line-height:1.3;
    margin:0 0 12px;
    letter-spacing:-.2px;
}

.section{
    margin-top:18px;
    padding-top:18px;
    border-top:1px solid #f0f0f3;
}

.section h2{
    font-size:12px;
    color:#555a66;
    margin-bottom:9px;
}

.eyebrow{
    color:var(--accent);
    font-size:10px;
    font-weight:800;
    letter-spacing:.1em;
    text-transform:uppercase;
    margin-bottom:6px;
}

.panelTitle{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    margin-bottom:12px;
}

.panelTitle h2{margin:0;}

.panelHint{
    color:var(--muted-2);
    font-size:10px;
}

/* ---------- graph ---------- */

.graphWrap{
    position:relative;
    overflow:hidden;
    border:1px solid var(--line);
    border-radius:12px;
    background:#fcfcfe;
}

canvas{
    width:100%;
    height:590px;
    background:#fcfcfe;
    border-radius:12px;
    display:block;
    touch-action:none;
}

.graphToolbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
    padding:10px 11px;
    border:1px solid var(--line);
    border-top:0;
    border-radius:0 0 12px 12px;
    background:#fff;
}

.graphToolbarLabel{
    color:var(--muted);
    font-size:10px;
}

.controls{
    display:flex;
    gap:7px;
    flex-wrap:wrap;
    margin-top:10px;
}

.graphControls button{
    min-height:34px;
    padding:7px 10px;
    font-size:11px;
}

/* ---------- modes ---------- */

.modeBar{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:6px;
}

.modeBar button{
    width:100%;
    font-size:11px;
    min-height:37px;
}

.help{
    font-size:11px;
    color:#777d89;
    line-height:1.7;
}

.help b{color:#505560;}

.editNotice{
    display:none;
    margin-top:8px;
    padding:10px 11px;
    border-radius:9px;
    background:var(--accent-soft);
    border:1px solid #ddd6ff;
    color:#6047c9;
    font-size:10px;
    line-height:1.55;
}

.editNotice.active{display:block;}

/* ---------- inputs ---------- */

input[type=text],
input[type=search]{
    width:100%;
    padding:10px 11px;
    border-radius:9px;
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    outline:none;
    transition:border-color .16s ease,box-shadow .16s ease;
}

input[type=text]:focus,
input[type=search]:focus,
select:focus{
    border-color:#b5a6ff;
    box-shadow:0 0 0 3px rgba(122,90,248,.09);
}

select{
    width:100%;
    padding:10px 11px;
    border-radius:9px;
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    outline:none;
}

label{
    display:block;
    font-size:10px;
    font-weight:700;
    color:#777d89;
    margin-bottom:6px;
}

.row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.row3{
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:8px;
}

/* ---------- info ---------- */

.info{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:7px;
    padding:9px;
    border-radius:10px;
    background:#fafafd;
    border:1px solid var(--line);
    font-size:11px;
    color:#707682;
    line-height:1.6;
}

.info > div{
    padding:7px 8px;
    border-radius:7px;
    background:#fff;
    border:1px solid #f0f0f3;
}

#message{
    min-height:18px;
    margin-top:7px;
    color:#b4233c;
    font-size:11px;
}

/* ---------- library ---------- */

.libraryList{
    display:flex;
    flex-direction:column;
    gap:6px;
    margin-top:10px;
}

.songItem{
    display:flex;
    align-items:center;
    gap:8px;
    padding:9px;
    border:1px solid var(--line);
    border-radius:9px;
    background:#fff;
}

.songInfo{
    flex:1;
    min-width:0;
}

.songTitle{
    font-size:11px;
    font-weight:700;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.songDate{
    font-size:9px;
    color:#9aa0ab;
    margin-top:3px;
}

.songActions{
    display:flex;
    gap:4px;
    flex:none;
}

.songActions button{
    min-height:27px;
    padding:4px 7px;
    font-size:9px;
}

.libraryMeta{
    font-size:10px;
    color:#8d929d;
    margin-top:7px;
}

/* ---------- layers ---------- */

.layerList{
    display:flex;
    flex-direction:column;
    gap:7px;
}

.layerItem{
    border:1px solid var(--line);
    border-radius:10px;
    padding:9px;
    background:#fff;
    cursor:default;
    transition:border-color .15s ease,box-shadow .15s ease,background .15s ease;
}

.layerItem:hover{background:#fcfcfe;}

.layerItem.selected{
    border-color:#bdb0ff;
    background:#fbfaff;
    box-shadow:0 0 0 2px rgba(122,90,248,.08);
}

.layerTop{
    display:flex;
    align-items:center;
    gap:8px;
    cursor:pointer;
}

.layerColor{
    width:9px;
    height:9px;
    border-radius:50%;
    flex:none;
}

.layerNameInput{
    flex:1;
    min-width:0;
    padding:5px 6px !important;
    min-height:28px;
    font-size:11px;
    font-weight:700;
    border-color:transparent !important;
    background:transparent !important;
    box-shadow:none !important;
}

.layerNameInput:focus{
    border-color:var(--line-strong) !important;
    background:#fff !important;
}

.layerType{
    font-size:8px;
    color:#a0a5ae;
    font-weight:800;
    letter-spacing:.06em;
    flex:none;
}

.layerActions{
    display:flex;
    align-items:center;
    gap:8px;
    margin-top:7px;
}

.layerActions button{
    min-height:28px;
    padding:4px 7px;
    font-size:9px;
}

.visibility{
    font-size:9px;
    color:#777d89;
    flex:none;
}

.volumeBox{
    flex:1;
    min-width:0;
}

.volumeHeader{
    display:flex;
    justify-content:space-between;
    font-size:9px;
    color:#999ea8;
    margin-bottom:3px;
}

.layerVolume{
    width:100%;
    accent-color:var(--accent);
}

/* ---------- music ---------- */

.musicBox{
    margin-top:14px;
}

.musicHero{
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap:12px;
    padding:12px;
    margin-bottom:12px;
    border:1px solid #e5defe;
    border-radius:11px;
    background:linear-gradient(180deg,#fbfaff,#fff);
}

.musicHeroTitle{
    font-size:12px;
    font-weight:800;
    color:#302b3b;
}

.musicHeroText{
    margin-top:3px;
    color:#888391;
    font-size:10px;
    line-height:1.5;
}

.musicMark{
    width:30px;
    height:30px;
    border-radius:9px;
    display:grid;
    place-items:center;
    background:var(--accent-soft);
    color:var(--accent);
    font-size:14px;
    flex:none;
}

.now{
    font-size:11px;
    color:#777d89;
    min-height:20px;
    margin:9px 0;
}

.progress{
    height:6px;
    background:#eeeef3;
    border-radius:99px;
    overflow:hidden;
}

#bar{
    height:100%;
    width:0;
    background:var(--accent);
    transition:width .05s linear;
}

.layerCount{
    font-size:10px;
    color:#8d929d;
    margin-top:6px;
}

/* ---------- principle ---------- */

.notice{
    padding:10px;
    border-radius:9px;
    background:#fafafd;
    border:1px solid var(--line);
    color:#777d89;
    font-size:10px;
    line-height:1.6;
}

hr{
    border:0;
    border-top:1px solid #eeeeF2;
    margin:14px 0;
}

/* ---------- footer ---------- */

.brandFooter{
    margin-top:18px;
    padding:13px 2px 0;
    border-top:1px solid var(--line);
    color:#9a9ea8;
    font-size:10px;
    display:flex;
    justify-content:space-between;
    gap:12px;
}

/* ---------- responsive ---------- */

@media(max-width:950px){
    #cosmos{padding:8px;}
    .grid{grid-template-columns:1fr;}
    canvas{height:500px;}
}

@media(max-width:600px){
    #cosmos{padding:6px;}
    .header{align-items:flex-start;}
    .badge{display:none;}
    .topNav{overflow-x:auto;}
    .navItem{white-space:nowrap;}
    canvas{height:390px;}
    .workspace{grid-template-columns:1fr;height:auto;}
    .expressionPane{height:300px;border-right:0;border-bottom:1px solid #dedfe6;}
    .graphWorkspace{height:650px;}
    .workspaceRail{position:absolute;right:6px;top:120px;bottom:auto;height:0;border:0;}
    .workspaceRailTab{position:relative;top:0;}
    .row,.row3,.info{grid-template-columns:1fr;}
    .brandFooter{flex-direction:column;}
}

/* =========================================================
   COSMOS WORKSPACE — DESMOS-LIKE STRUCTURE
========================================================= */

.workspaceShell{
    background:#fff;
    border:1px solid #dedfe6;
    border-radius:14px;
    box-shadow:0 8px 30px rgba(25,25,40,.07);
    overflow:hidden;
    min-height:0;
    height:calc(100vh - 118px);
}

.appToolbar{
    height:58px;
    display:flex;
    align-items:center;
    gap:12px;
    padding:0 16px;
    border-bottom:1px solid #e2e3e8;
    background:#fff;
}

.toolbarBrand{
    display:flex;
    align-items:center;
    gap:9px;
    font-weight:800;
    letter-spacing:-.3px;
    margin-right:6px;
}

.toolbarFlower{
    width:30px;
    height:30px;
    border:1px solid #ddd7ff;
    border-radius:8px;
    display:grid;
    place-items:center;
    background:#faf9ff;
}

.toolbarFlower svg{width:22px;height:22px;}

.fileTitle{
    height:34px;
    min-width:190px;
    border:1px solid transparent;
    background:transparent;
    padding:5px 9px;
    font-weight:650;
    color:#34353c;
    border-radius:7px;
}

.fileTitle:hover,
.fileTitle:focus{
    border-color:#d9dbe3;
    background:#fafafd;
    outline:none;
}

.toolbarSpacer{flex:1;}

.toolbarBtn{
    min-height:34px;
    padding:6px 10px;
    font-size:12px;
    border-radius:7px;
}

.toolbarBtn.icon{
    width:34px;
    padding:6px;
    font-size:16px;
}

.workspace{
    display:grid;
    grid-template-columns:290px minmax(0,1fr) 42px;
    flex:1;
    height:calc(100% - 58px);
    min-height:0;
}

.expressionPane{
    background:#fbfbfc;
    border-right:1px solid #dedfe6;
    display:flex;
    flex-direction:column;
    min-width:0;
    overflow:hidden;
}

.expressionHeader{
    height:58px;
    display:flex;
    align-items:center;
    gap:9px;
    padding:0 12px;
    border-bottom:1px solid #e4e5ea;
}

.expressionHeaderTitle{
    font-size:13px;
    font-weight:800;
    flex:1;
}

.addMenuWrap{position:relative;}

.addMenu{
    position:absolute;
    top:43px;
    left:0;
    z-index:30;
    width:190px;
    padding:6px;
    background:#fff;
    border:1px solid #dddfe6;
    border-radius:10px;
    box-shadow:0 14px 30px rgba(25,25,40,.12);
    display:none;
}

.addMenu.open{display:block;}

.addMenu button{
    width:100%;
    text-align:left;
    border:0;
    background:#fff;
    min-height:34px;
    font-size:11px;
    border-radius:7px;
}

.addMenu button:hover{background:#f4f2ff;}

.expressionScroll{
    flex:1;
    overflow:auto;
    padding:8px;
}

.expressionScroll .layerList{
    display:flex;
    flex-direction:column;
    gap:6px;
}

.expressionFooter{
    border-top:1px solid #e3e4e9;
    padding:9px;
    background:#fff;
}

.expressionFooterRow{
    display:flex;
    gap:6px;
}

.expressionFooter button{
    flex:1;
    min-height:32px;
    font-size:10px;
}

.compactLibrary{
    border-top:1px solid #e3e4e9;
    background:#fff;
}

.compactLibrary summary{
    cursor:pointer;
    padding:11px 12px;
    font-size:11px;
    font-weight:750;
    list-style:none;
}

.compactLibrary summary::-webkit-details-marker{display:none;}

.compactLibrary summary:after{
    content:"＋";
    float:right;
    color:#8b8e99;
}

.compactLibrary[open] summary:after{content:"−";}

.libraryInner{
    padding:0 10px 10px;
}

.libraryInner .controls{display:flex;gap:5px;flex-wrap:wrap;}
.libraryInner .controls button{min-height:30px;padding:5px 7px;font-size:9px;}
.libraryInner .section{padding-top:8px;margin-top:8px;}
.libraryInner input,.libraryInner select{min-height:32px;font-size:10px;}
.libraryInner .libraryList{max-height:100px;overflow:auto;}

.graphWorkspace{
    min-width:0;
    min-height:0;
    display:flex;
    flex-direction:column;
    background:#fff;
}

.graphTop{
    height:44px;
    display:flex;
    align-items:center;
    padding:0 12px;
    gap:8px;
    border-bottom:1px solid #e4e5ea;
}

.graphTopTitle{
    font-size:11px;
    font-weight:800;
    color:#34353c;
}

.graphTopHint{
    font-size:10px;
    color:#9a9ea8;
    flex:1;
}

.graphCanvasArea{
    position:relative;
    flex:1;
    min-height:260px;
    background:#fcfcfe;
}

.graphCanvasArea canvas{
    display:block;
    width:100%;
    height:100%;
    border:0;
    border-radius:0;
}

.canvasSettings{
    position:absolute;
    top:10px;
    right:10px;
    z-index:5;
}

.canvasSettingsBtn{
    width:34px;
    height:34px;
    min-height:34px;
    padding:0;
    border-radius:8px;
    background:rgba(255,255,255,.94);
    box-shadow:0 3px 12px rgba(20,20,30,.08);
}

.settingsPanel{
    position:absolute;
    top:48px;
    right:10px;
    z-index:20;
    width:250px;
    padding:12px;
    border:1px solid #dedfe6;
    border-radius:10px;
    background:#fff;
    box-shadow:0 16px 34px rgba(20,20,30,.13);
    display:none;
}

.settingsPanel.open{display:block;}

.settingsTitle{
    font-size:11px;
    font-weight:800;
    margin-bottom:9px;
}

.settingsGrid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:7px;
}

.settingsGrid label{
    font-size:9px;
    color:#777d89;
}

.settingsGrid input{
    margin-top:3px;
    width:100%;
    min-height:30px;
    padding:5px 7px;
    font-size:10px;
}

.settingsChecks{
    margin-top:9px;
    display:flex;
    gap:12px;
    flex-wrap:wrap;
    font-size:10px;
    color:#626670;
}

.graphBottom{
    min-height:126px;
    border-top:1px solid #e2e3e8;
    padding:10px 12px;
    background:#fff;
}

.bottomGrid{
    display:grid;
    grid-template-columns:minmax(0,1.6fr) minmax(230px,.8fr);
    gap:10px;
}

.functionEditor{
    border:1px solid #e1e2e8;
    border-radius:9px;
    background:#fbfbfc;
    padding:8px;
}

.functionEditor label{
    font-size:9px;
    color:#777d89;
    margin-bottom:4px;
}

.functionEditor input{
    min-height:34px;
    background:#fff;
}

.functionActions{
    display:flex;
    gap:6px;
    margin-top:6px;
}

.functionActions button{
    min-height:30px;
    padding:5px 9px;
    font-size:10px;
}

.analysisStrip{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:5px;
}

.analysisCell{
    border:1px solid #e4e5ea;
    border-radius:8px;
    padding:7px;
    background:#fff;
    min-width:0;
}

.analysisLabel{
    font-size:8px;
    color:#9296a0;
    margin-bottom:3px;
}

.analysisValue{
    font-size:10px;
    font-weight:700;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.workspaceRail{
    position:relative;
    border-left:1px solid #dedfe6;
    background:#fff;
}

.workspaceRailTab{
    position:absolute;
    right:0;
    top:18px;
    z-index:8;
    display:flex;
    flex-direction:column;
    gap:6px;
}

.railBtn{
    width:38px;
    min-height:38px;
    padding:0;
    border-radius:8px 0 0 8px;
    background:#fff;
    box-shadow:0 3px 12px rgba(20,20,30,.07);
    font-size:16px;
}

.railPanel{
    position:absolute;
    top:0;
    right:0;
    width:330px;
    height:100%;
    padding:14px;
    background:#fff;
    border-left:1px solid #dedfe6;
    box-shadow:-12px 0 30px rgba(20,20,30,.08);
    z-index:7;
    overflow:auto;
    display:none;
}

.railPanel.open{display:block;}

.railPanelHeader{
    display:flex;
    align-items:center;
    gap:8px;
    margin-bottom:12px;
}

.railPanelHeader h3{
    margin:0;
    font-size:14px;
    flex:1;
}

.railClose{
    width:30px;
    min-height:30px;
    padding:0;
}

.railPanel .musicBox{
    margin-top:0;
}

.railPanel .card{
    border:0;
    box-shadow:none;
    padding:0;
}

.railPanel .row{
    grid-template-columns:1fr 1fr;
}

.keypad{
    position:absolute;
    right:14px;
    bottom:14px;
    z-index:12;
    width:360px;
    padding:10px;
    border:1px solid #dedfe6;
    border-radius:10px;
    background:#fff;
    box-shadow:0 16px 34px rgba(20,20,30,.13);
    display:none;
}

.keypad.open{display:block;}

.keypadGrid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:5px;
}

.keypad button{
    min-height:34px;
    padding:5px;
    font-size:10px;
}

.principlePanel{
    font-size:11px;
    line-height:1.7;
    color:#656a75;
}

.principleFormula{
    margin:10px 0;
    padding:12px;
    border:1px solid #e2defc;
    background:#faf9ff;
    border-radius:9px;
    color:#4e3eb1;
    font-weight:750;
}

.workspaceHint{
    padding:7px 10px;
    font-size:9px;
    color:#9296a0;
    border-top:1px solid #e6e7ec;
    background:#fbfbfc;
}

@media(max-width:1050px){
    .workspace{grid-template-columns:270px minmax(0,1fr);}
    .bottomGrid{grid-template-columns:1fr;}
    .analysisStrip{grid-template-columns:repeat(3,1fr);}
}

@media(max-width:760px){
    .workspace{grid-template-columns:250px minmax(0,1fr) 38px;height:calc(100% - 58px);}
    .expressionPane{min-height:0;border-right:1px solid #dedfe6;border-bottom:0;}
    .graphWorkspace{height:auto;min-height:0;}
    .workspaceRail{position:absolute;inset:58px 0 0 0;pointer-events:none;border:0;}
    .workspaceRailTab,.railPanel{pointer-events:auto;}
    .railPanel{width:min(330px,92vw);}
}

/* Full-workspace sizing and the graph-to-music arrangement view */
html,body{margin:0!important;padding:0!important;width:100%;min-height:100%;overflow-x:hidden;background:#f6f7fb;}
[data-testid="stAppViewContainer"]{padding:0!important;background:#f6f7fb!important;}
[data-testid="stMainBlockContainer"]{max-width:none!important;padding:0!important;}
[data-testid="stHeader"],[data-testid="stToolbar"],#MainMenu,footer{display:none!important;}
#cosmos{min-height:0;}
.workspaceShell{display:flex;flex-direction:column;height:calc(100vh - 20px);min-height:620px;}
.workspace{flex:1;min-height:0;}
.expressionPane,.graphWorkspace,.workspaceRail{min-height:0;}
.graphCanvasArea{min-height:0;}
.graphBottom{flex-shrink:0;}
.brandFooter{display:none;}
.arrangementStudio{margin:12px 0 14px;padding:12px;border:1px solid #e6e6ef;border-radius:12px;background:#fbfbff;}
.arrangementHead{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px;}
.arrangementTitle{font-size:12px;font-weight:800;color:#252630;}
.arrangementSub{font-size:10px;color:#858896;}
.arrangementTrackList{display:flex;flex-direction:column;gap:6px;}
.arrangementTrack{display:grid;grid-template-columns:82px minmax(0,1fr);align-items:center;gap:8px;min-height:42px;}
.arrangementTrackName{font-size:10px;font-weight:750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.arrangementTrackName small{display:block;font-size:9px;font-weight:500;color:#8c8f9b;margin-top:2px;}
.arrangementLane{height:40px;position:relative;overflow:hidden;border-radius:6px;background:#f0f1f6;border:1px solid #e8e9f0;}
.arrangementLane svg{display:block;width:100%;height:100%;}
.arrangementPlayhead{position:absolute;top:0;bottom:0;left:0;width:2px;background:#ffffff;box-shadow:0 0 0 1px rgba(100,90,180,.28),0 0 10px rgba(139,108,246,.5);pointer-events:none;z-index:2;}
.bpmControl{padding:10px 12px;border:1px solid #e5e6ec;border-radius:10px;background:#fbfbfd;margin:10px 0 14px!important;}
.bpmHeading{display:flex;align-items:center;justify-content:space-between;gap:8px;}
.bpmHeading label{font-size:12px;font-weight:750;color:#30333a;}
#bpmValue{font-size:12px;font-weight:800;color:#4169e1;font-variant-numeric:tabular-nums;}
#bpm{width:100%;accent-color:#4169e1;margin:10px 0 2px;}
.bpmScale{display:flex;justify-content:space-between;color:#8a8d96;font-size:10px;}

.arrangementPlayhead:after{content:"";position:absolute;top:0;left:-3px;width:8px;height:8px;border-radius:50%;background:#8b6cf6;}
.arrangementLegend{display:flex;justify-content:space-between;color:#9a9daa;font-size:9px;margin:7px 0 0 90px;}
.arrangementEmpty{padding:13px 8px;color:#898c98;font-size:10px;text-align:center;background:#f5f5fa;border-radius:7px;}
.musicBox .musicHero{margin-bottom:10px;}
.musicBox .musicHeroText{line-height:1.5;}
.musicBox .controls button{flex:1;min-width:0;}
@media(max-width:850px){.workspaceShell{height:auto;min-height:0}.workspace{height:auto;min-height:0}.graphWorkspace{min-height:680px}.expressionPane{min-height:480px}.arrangementTrack{grid-template-columns:68px minmax(0,1fr)}.arrangementLegend{margin-left:76px}}


/* Desmos-inspired compact graphing workspace */
:root{--bg:#fff;--surface:#fff;--surface-soft:#fff;--text:#202124;--muted:#686b70;--line:#e3e5e8;--line-strong:#c8cbd0;--accent:#4169d5;--accent-dark:#3156bd;--accent-soft:#edf2ff;--shadow:0 2px 8px rgba(0,0,0,.08);--shadow-sm:0 1px 4px rgba(0,0,0,.08)}
body{background:#fff!important;color:#202124!important;font-family:Arial,"Noto Sans KR",sans-serif!important}
#cosmos{width:100%!important;max-width:none!important;margin:0!important;padding:0!important}
.header{display:none!important}
.workspaceShell{width:100%!important;max-width:none!important;margin:0!important;border:0!important;border-radius:0!important;box-shadow:none!important;height:calc(100dvh - 2px)!important;min-height:620px!important;background:#fff!important}
.appToolbar{height:54px!important;min-height:54px!important;padding:5px 12px!important;background:#292929!important;color:#fff!important;border:0!important;border-radius:0!important}
.toolbarBrand{color:#fff!important}.toolbarFlower{display:none!important}.toolbarBrand span{font-size:18px!important;letter-spacing:1px!important;color:#fff!important}
.fileTitle{background:transparent!important;color:#fff!important;border:0!important;border-left:1px solid #777!important;border-radius:0!important;font-size:17px!important;min-width:80px!important;max-width:220px!important}
.toolbarBtn{border-radius:5px!important;min-height:34px!important;padding:6px 10px!important;font-size:13px!important}
.workspace{height:calc(100% - 54px)!important;min-height:0!important;grid-template-columns:minmax(250px,29%) minmax(0,1fr) 38px!important;gap:0!important;background:#fff!important;overflow:visible!important;}
.workspaceRail{display:block!important;position:relative!important;width:38px!important;min-width:38px!important;overflow:visible!important;z-index:40!important;background:#fff!important;border-left:1px solid #d8dadd!important;}
.railPanel{box-sizing:border-box!important;position:absolute!important;top:0!important;right:0!important;width:min(420px,calc(100vw - 48px))!important;height:100%!important;max-height:100%!important;padding:14px!important;overflow:auto!important;background:#fff!important;z-index:100!important;border:1px solid #d8dadd!important;box-shadow:-10px 0 28px #0002!important;}
.railPanel.open{display:block!important;}
.workspaceRailTab{right:0!important;top:10px!important;z-index:110!important;}
.helpContent{padding-bottom:18px!important;}
.helpSection{padding:12px 0!important;border-bottom:1px solid #e7e8eb!important;line-height:1.6!important;}
.helpSection p{margin:6px 0 0!important;color:#555b65!important;font-size:12px!important;}
.helpSection code{display:inline-block;background:#f1f3f5!important;padding:1px 4px!important;border-radius:3px!important;color:#222!important;}
.toolbarPlayAll{background:#4b72d8!important;color:#fff!important;border-color:#4b72d8!important;font-weight:700!important;}
.expressionPane{background:#fff!important;border-right:1px solid #d8dadd!important;border-radius:0!important;min-height:0!important;overflow:hidden!important}
.expressionHeader{padding:8px 10px!important;border-bottom:1px solid #d8dadd!important;background:#f7f7f7!important}
.expressionHeaderTitle,.graphTopTitle{font-size:14px!important;font-weight:600!important;color:#45474b!important}
.layerItem{border-radius:0!important;border:0!important;border-bottom:1px solid #e4e5e7!important;background:#fff!important;padding:0!important;margin:0!important;box-shadow:none!important}
.layerItem.selected{background:#f7f9ff!important;outline:1px solid #4c74d9!important;outline-offset:-1px!important}
.layerTop{min-height:42px!important;padding:7px 8px!important;gap:8px!important}
.layerColor{width:5px!important;height:34px!important;border-radius:0!important;flex:0 0 5px!important}
.layerNameInput{font-size:16px!important;border-radius:3px!important;border:1px solid transparent!important;background:transparent!important}
.layerNameInput:focus{border-color:#4b74d8!important;background:#fff!important}
.layerType{display:none!important}
.layerActions{padding:4px 8px 8px 21px!important;gap:8px!important;align-items:center!important}
.layerActions button{min-height:28px!important;padding:3px 8px!important;font-size:12px!important;border-radius:4px!important}
.volumeBox{flex:1!important;min-width:60px!important}
.expressionFooter{padding:8px!important;border-top:1px solid #e0e1e4!important;background:#fafafa!important}
.workspaceHint,.editNotice{font-size:11px!important}
.graphWorkspace{min-width:0!important;min-height:0!important;border:0!important;border-radius:0!important;background:#fff!important;display:flex!important;flex-direction:column!important;overflow:hidden!important}
.graphTop{height:34px!important;min-height:34px!important;padding:5px 12px!important;background:#fff!important;border-bottom:1px solid #ececef!important}
.graphTopHint{font-size:11px!important;color:#8a8d92!important}
.graphCanvasArea{flex:1 1 auto!important;min-height:0!important;height:auto!important;border:0!important;border-radius:0!important;background:#fff!important;overflow:hidden!important}
#graph{width:100%!important;height:100%!important;min-height:0!important;background:#fff!important;touch-action:none!important}
.canvasSettings{top:8px!important;right:8px!important}
.canvasSettingsBtn{width:38px!important;height:38px!important;border-radius:4px!important;background:#f7f7f7!important;color:#555!important;box-shadow:0 1px 3px #0002!important}
/* 수학식 입력기: 지수는 실제 위첨자로 표시하고 곱셈 기호는 ×로 렌더링 */
.mathEditor{
    width:100%;min-height:42px;max-height:112px;overflow:auto;box-sizing:border-box;
    padding:9px 12px;border:1px solid #cfd2d8;border-radius:8px;background:#fff;
    color:#202124;font:20px/1.55 "Cambria Math","STIX Two Math",Cambria,serif;
    white-space:pre-wrap;overflow-wrap:anywhere;outline:none;cursor:text;
}
.mathEditor:focus{border-color:#4169e1;box-shadow:0 0 0 2px rgba(65,105,225,.12)}
.mathEditor .implicitProduct{display:inline-block;width:0;overflow:hidden;vertical-align:baseline}
.mathEditor sup.mathExponent{display:inline-block;font-size:.68em;line-height:1;vertical-align:super;position:static;white-space:nowrap;color:inherit;min-width:0.35em}.mathEditor sup.mathExponent *{font-size:1em}.mathEditor sup.mathExponent:empty::after{content:"□";opacity:.35}
.mathEditor sup.mathExponent:empty::after{content:"□";opacity:.35}
.mathEditor sup.mathExponent:focus{outline:1px dotted #4169e1}
.mathEditor .mathExitPoint{display:inline;white-space:pre;min-width:0;outline:none;color:inherit}
.functionEditor #exprVisual{margin:2px 0 5px}
.keypad{position:absolute!important;left:auto!important;right:12px!important;bottom:12px!important;top:auto!important;transform:none!important;width:min(390px,calc(100% - 24px))!important;max-height:min(42vh,360px)!important;overflow:auto!important;border:1px solid #c9cdd3!important;border-radius:8px!important;background:#f5f6f7!important;box-shadow:0 4px 18px rgba(0,0,0,.18)!important;padding:8px!important;z-index:30!important}
.keypadGrid{grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:5px!important}.keypadGrid button{border-radius:4px!important;min-height:34px!important;background:#fff!important;border:1px solid #d6d6d6!important;color:#202124!important;font-size:12px!important}
.brandFooter{display:none!important}
.layerSoundBtn{width:34px!important;min-width:34px!important;padding:3px!important;font-size:17px!important;background:#fff!important;border:1px solid #d5d8de!important;border-radius:4px!important}
.layerSoundBtn.active{background:#eaf0ff!important;border-color:#4169d5!important;color:#3156bd!important}
@media(max-width:850px){.workspaceShell{height:calc(100dvh - 2px)!important;min-height:0!important}.workspace{height:calc(100% - 54px)!important;grid-template-columns:minmax(0,1fr)!important;grid-template-rows:minmax(0,1fr) minmax(150px,32%)!important;position:relative!important}.graphWorkspace{grid-row:1;min-height:0!important}.expressionPane{grid-row:2;min-height:0!important;border-top:1px solid #d8dadd!important;border-right:0!important}.workspaceRail{position:absolute!important;top:0!important;right:0!important;bottom:0!important;width:38px!important;min-width:38px!important;border:0!important;background:transparent!important}.railPanel{right:38px!important;width:min(420px,calc(100vw - 44px))!important;height:100%!important}.expressionScroll{min-height:0!important;overflow:auto!important}.keypad{max-height:38vh!important;right:6px!important;bottom:6px!important;width:min(360px,calc(100% - 12px))!important}.graphTopHint{display:none!important}.toolbarPlayAll{display:inline-flex!important;font-size:11px!important;padding:5px 7px!important;min-height:30px!important}}
@media(max-height:700px){.keypad{max-height:125px!important}.expressionFooter .workspaceHint{display:none!important}}

</style>

</head>

<body>

<div id="cosmos">

<div class="header">
    <div class="brand">
        <div class="brandMark" aria-label="Cosmos flower logo">
            <svg viewBox="0 0 48 48" aria-hidden="true">
                <g fill="#8b6cf6">
                    <ellipse cx="24" cy="10.5" rx="5.2" ry="10"/>
                    <ellipse cx="35.5" cy="16" rx="5.2" ry="10" transform="rotate(45 35.5 16)"/>
                    <ellipse cx="37.5" cy="29" rx="5.2" ry="10" transform="rotate(90 37.5 29)"/>
                    <ellipse cx="29.5" cy="37" rx="5.2" ry="10" transform="rotate(135 29.5 37)"/>
                    <ellipse cx="18.5" cy="37" rx="5.2" ry="10" transform="rotate(225 18.5 37)"/>
                    <ellipse cx="10.5" cy="29" rx="5.2" ry="10" transform="rotate(270 10.5 29)"/>
                    <ellipse cx="12.5" cy="16" rx="5.2" ry="10" transform="rotate(315 12.5 16)"/>
                </g>
                <circle cx="24" cy="24" r="5.2" fill="#f5c76a"/>
                <circle cx="24" cy="24" r="2.2" fill="#8b6cf6"/>
            </svg>
        </div>
        <div class="brandText">
            <div class="logo">Cos<span>mos</span></div>
            <div class="subtitle">Graph → Music · 수학적 구조를 시각화하고 소리로 경험하는 그래핑 스튜디오</div>
            <div class="brandMeaning"><span>ORDER</span><span class="dot"></span><span>HARMONY</span><span class="dot"></span><span>EXPRESSION</span></div>
        </div>
    </div>
    <span class="badge">Cosmos v3.2 · Mathematics in Harmony</span>
</div>

<div class="workspaceShell">

    <div class="appToolbar">
        <div class="toolbarBrand">
            <div class="toolbarFlower">
                <svg viewBox="0 0 48 48" aria-hidden="true">
                    <g fill="#8b6cf6">
                        <ellipse cx="24" cy="10.5" rx="5.2" ry="10"/>
                        <ellipse cx="35.5" cy="16" rx="5.2" ry="10" transform="rotate(45 35.5 16)"/>
                        <ellipse cx="37.5" cy="29" rx="5.2" ry="10" transform="rotate(90 37.5 29)"/>
                        <ellipse cx="29.5" cy="37" rx="5.2" ry="10" transform="rotate(135 29.5 37)"/>
                        <ellipse cx="18.5" cy="37" rx="5.2" ry="10" transform="rotate(225 18.5 37)"/>
                        <ellipse cx="10.5" cy="29" rx="5.2" ry="10" transform="rotate(270 10.5 29)"/>
                        <ellipse cx="12.5" cy="16" rx="5.2" ry="10" transform="rotate(315 12.5 16)"/>
                    </g>
                    <circle cx="24" cy="24" r="5.2" fill="#f5c76a"/>
                </svg>
            </div>
            <span>COSMOS</span>
        </div>

        <input id="songName" class="fileTitle" type="text" value="Untitled Cosmos" autocomplete="off" aria-label="현재 곡 이름">

        <button id="newSong" class="toolbarBtn" title="새 작업 공간">새로 만들기</button>
        <button id="saveSong" class="toolbarBtn primary" title="현재 곡 저장">저장</button>
        <div class="toolbarSpacer"></div>
        <button id="toolbarPlayAll" class="toolbarBtn toolbarPlayAll" title="표시된 모든 그래프를 동시에 재생">▶ 전체 재생</button>
        <button id="musicRailOpen" class="toolbarBtn">♫ Graph → Music</button>
        <button id="principleRailOpen" class="toolbarBtn icon" title="도움말">?</button>
    </div>

    <div class="workspace">

        <!-- LEFT: EXPRESSIONS -->
        <aside class="expressionPane">

            <div class="expressionHeader">
                <div class="addMenuWrap">
                    <button id="addMenuToggle" class="toolbarBtn primary" title="항목 추가">＋</button>
                    <div id="addMenu" class="addMenu">
                        <button id="addFunctionLayer">ƒ　함수 그래프</button>
                        <button id="addSketchLayer">✎　손그림 그래프</button>
                    </div>
                </div>
                <div class="expressionHeaderTitle">Expressions</div>
                <button id="deleteLayer" class="toolbarBtn danger" title="선택 항목 삭제">삭제</button>
            </div>

            <div class="expressionScroll">
                <div class="layerList" id="layerList"></div>
            </div>

            <div class="expressionFooter">
                <div id="editNotice" class="editNotice">Edit 모드: 그래프를 직접 선택하고 드래그해 이동·크기 조절·회전합니다.</div>
                <div id="layerCount" style="display:none;"></div>
                <div class="expressionFooterRow">
                    <button id="navigateMode" class="active">이동</button>
                    <button id="sketchMode">손그림</button>
                    <button id="editMode">Edit</button>
                </div>
                <div class="workspaceHint">그래프를 드래그해 이동하고 휠로 확대·축소합니다. Edit에서는 그래프를 직접 잡아 움직입니다.</div>
            </div>

            <details class="compactLibrary">
                <summary>Library</summary>
                <div class="libraryInner">
                    <select id="librarySelect"></select>
                    <div class="controls">
                        <button id="newLibrary" class="primary">＋ Library</button>
                        <button id="renameLibrary">이름 변경</button>
                        <button id="deleteLibrary" class="danger">삭제</button>
                    </div>
                    <div class="section">
                        <label>현재 곡</label>
                        <div class="controls">
                            <button id="saveSongSecondary" class="primary">곡 저장</button>
                        </div>
                    </div>
                    <div class="libraryMeta" id="libraryMeta">0개 곡</div>
                    <div class="libraryList" id="songList"></div>
                </div>
            </details>
        </aside>

        <!-- CENTER: GRAPH -->
        <main class="graphWorkspace">

            <div class="graphTop">
                <span class="graphTopTitle">Graph</span>
                <span class="graphTopHint">수식을 입력하면 그래프가 즉시 캔버스에 표시됩니다.</span>
            </div>

            <div class="graphCanvasArea">
                <canvas id="graph" width="1200" height="650"></canvas>

                <div class="canvasSettings">
                    <button id="settingsToggle" class="canvasSettingsBtn" title="그래프 설정">⚙</button>
                    <div id="settingsPanel" class="settingsPanel">
                        <div class="settingsTitle">Graph Settings</div>
                        <div class="settingsGrid">
                            <div><label>X 최소</label><input id="xminInput" type="number" value="-10" step="1"></div>
                            <div><label>X 최대</label><input id="xmaxInput" type="number" value="10" step="1"></div>
                            <div><label>Y 최소</label><input id="yminInput" type="number" value="-6" step="1"></div>
                            <div><label>Y 최대</label><input id="ymaxInput" type="number" value="6" step="1"></div>
                        </div>
                        <div class="settingsChecks">
                            <label><input id="gridToggle" type="checkbox" checked> 격자</label>
                            <label><input id="axisToggle" type="checkbox" checked> 축</label>
                        </div>
                        <button id="resetView" style="width:100%;margin-top:9px;">기본 화면으로</button>
                    </div>
                </div>

                <div id="keypad" class="keypad">
                    <div class="keypadGrid">
                        <button data-key="x">x</button>
                        <button data-key="y">y</button>
                        <button data-key="(">(</button>
                        <button data-key=")">)</button>
                        <button data-key="[">[ ]</button>
                        <button data-key="]">]</button>
                        <button data-key="^">aᵇ</button>
                        <button data-key="pi">π</button>
                        <button data-key="7">7</button>
                        <button data-key="8">8</button>
                        <button data-key="9">9</button>
                        <button data-key="/">÷</button>
                        <button data-key="sqrt(">√</button>
                        <button data-key="frac(">frac</button>
                        <button data-key="sin(">sin</button>
                        <button data-key="4">4</button>
                        <button data-key="5">5</button>
                        <button data-key="6">6</button>
                        <button data-key="*">×</button>
                        <button data-key="cos(">cos</button>
                        <button data-key="tan(">tan</button>
                        <button data-key="mod">mod</button>
                        <button data-key="1">1</button>
                        <button data-key="2">2</button>
                        <button data-key="3">3</button>
                        <button data-key="-">−</button>
                        <button data-key="abs(">abs</button>
                        <button data-key="log(">log</button>
                        <button data-key="0">0</button>
                        <button data-key=".">.</button>
                        <button data-key="+">+</button>
                        <button data-key="=">=</button>
                        <button data-key="ln(">ln</button>
                        <button data-key="e">e</button>
                    </div>
                </div>
            </div>

            <div class="graphBottom">
                <div class="bottomGrid">
                    <div class="functionEditor">
                        <label for="exprVisual">선택된 표현식</label>
                        <input id="expr" type="text" value="sin(x)" autocomplete="off" spellcheck="false" aria-hidden="true" tabindex="-1" style="display:none!important">
                        <div id="exprVisual" class="mathEditor" contenteditable="true" role="textbox" aria-label="수식 입력. 지수 입력 후 오른쪽 화살표를 누르면 지수 밖으로 이동합니다." spellcheck="false"></div>
                        <div class="functionActions">
                            <button id="draw" class="primary">그래프 적용</button>
                            <button id="clearLayer">지우기</button>
                            <button id="keypadToggle">⌨ 키패드</button>
                        </div>
                        <div id="message"></div>
                    </div>

                    <div class="analysisStrip">
                        <div class="analysisCell"><div class="analysisLabel">정의역</div><div class="analysisValue" id="domain">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">최솟값</div><div class="analysisValue" id="minY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">최댓값</div><div class="analysisValue" id="maxY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">평균</div><div class="analysisValue" id="avgY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">선택</div><div class="analysisValue" id="selectedLayerInfo">—</div></div>
                    </div>
                </div>
            </div>

        </main>

        <!-- RIGHT RAIL -->
        <aside class="workspaceRail">

            <div class="workspaceRailTab">
                <button id="musicRailButton" class="railBtn" title="Graph → Music">♫</button>
                <button id="principleRailButton" class="railBtn" title="도움말">?</button>
            </div>

            <div id="musicDrawer" class="railPanel">
                <div class="railPanelHeader">
                    <h3>Graph → Music</h3>
                    <button id="musicRailClose" class="railClose">×</button>
                </div>

                <section class="card musicBox" id="music">
                    <div class="musicHero">
                        <div>
                            <div class="musicHeroTitle">Graph → Music</div>
                            <div class="musicHeroText">x축은 시간, y값은 음높이로 변환됩니다. 표시된 그래프는 동시에 하나의 음악으로 구성됩니다.</div>
                        </div>
                        <div class="musicMark">♫</div>
                    </div>

                    <div class="arrangementStudio" aria-label="음악 트랙 미리보기">
                        <div class="arrangementHead">
                            <div>
                                <div class="arrangementTitle">Arrangement · 함수별 트랙</div>
                                <div class="arrangementSub">각 그래프가 독립적인 소리 트랙으로 겹쳐집니다.</div>
                            </div>
                            <span class="arrangementSub" id="arrangementStatus">READY</span>
                        </div>
                        <div class="arrangementTrackList" id="arrangementTrackList">
                            <div class="arrangementEmpty">그래프를 추가하면 트랙 미리보기가 표시됩니다.</div>
                        </div>
                        <div class="arrangementLegend"><span>0:00</span><span>전체 구간</span><span id="arrangementEnd">재생 끝</span></div>
                    </div>

                    <div class="row">
                        <div>
                            <label>음악 길이</label>
                            <select id="duration">
                                <option value="10">10초</option><option value="20">20초</option><option value="30">30초</option>
                                <option value="60">1분</option><option value="120">2분</option><option value="180">3분</option>
                                <option value="240">4분</option><option value="300">5분</option>
                            </select>
                        </div>
                        <div>
                            <label>음계</label>
                            <select id="scale">
                                <option value="major">C Major</option>
                                <option value="minor">A Minor</option>
                                <option value="pentatonic">Pentatonic</option>
                                <option value="chromatic">Chromatic</option>
                            </select>
                        </div>
                    </div>
                    <div class="section bpmControl">
                        <div class="bpmHeading"><label for="bpm">BPM · 템포</label><output id="bpmValue" for="bpm">145 BPM</output></div>
                        <input id="bpm" type="range" min="50" max="220" step="1" value="145" aria-label="음악 템포 BPM">
                        <div class="bpmScale"><span>50 느리게</span><span>220 빠르게</span></div>
                    </div>

                    <div class="section">
                        <label for="arrangementMode">편곡 방식</label>
                        <select id="arrangementMode">
                            <option value="all">모든 그래프를 각각 다른 악기 파트로 편성</option>
                            <option value="backing">그래프는 멜로디로, 자동 반주·베이스·드럼 추가</option>
                        </select>
                        <div class="muted">모든 그래프 모드에서는 레이어마다 음색을 나누고, 자동 반주 모드에서는 코드·베이스·리듬을 더합니다.</div>
                    </div>

                    <div class="section">
                        <label>음악 스타일 / 장르</label>
                        <select id="style">
                            <optgroup label="Pop">
                                <option value="pop">Pop</option><option value="kpop">K-pop</option><option value="jpop">J-pop</option>
                                <option value="citypop">City Pop</option><option value="rnb">R&B</option>
                            </optgroup>
                            <optgroup label="Electronic">
                                <option value="edm">EDM</option><option value="house">House</option><option value="techno">Techno</option>
                                <option value="trance">Trance</option><option value="futurebass">Future Bass</option><option value="dnb">Drum & Bass</option>
                                <option value="synthwave">Synthwave</option>
                            </optgroup>
                            <optgroup label="Hip-Hop">
                                <option value="hiphop">Hip-Hop</option><option value="trap">Trap</option><option value="boombap">Boom Bap</option>
                                <option value="phonk">Phonk</option><option value="funk">Funk</option>
                            </optgroup>
                            <optgroup label="Band & Jazz">
                                <option value="rock">Rock</option><option value="jazz">Jazz</option><option value="blues">Blues</option>
                            </optgroup>
                            <optgroup label="Classical & Atmosphere">
                                <option value="classic">Classic</option><option value="piano">Piano & Strings</option><option value="ambient">Ambient</option><option value="cinematic">Cinematic OST</option><option value="epic">Epic Fantasy</option><option value="lofi">Lo-fi</option>
                            </optgroup>
                        </select>
                    </div>

                    <div class="controls">
                        <button id="play" class="primary">▶ 그래프 전체로 음악 만들기</button>
                        <button id="stop">■ 정지</button>
                        <button id="downloadWav" class="success">↓ WAV 저장</button>
                    </div>
                    <div class="now" id="now">표시된 모든 그래프가 동시에 음악으로 변환됩니다.</div>
                    <div class="progress"><div id="bar"></div></div>
                </section>
            </div>

            <div id="principleDrawer" class="railPanel">
                <div class="railPanelHeader">
                    <h3>Cosmos Principle</h3>
                    <button id="principleRailClose" class="railClose">×</button>
                </div>
                <div id="principle" class="principlePanel helpContent">
                    <div class="principleFormula">COSMOS 빠른 사용 안내</div>
                    <section class="helpSection"><b>1. 그래프 입력</b><p>왼쪽의 <b>＋</b>를 눌러 함수 그래프를 추가하고, 식을 입력한 뒤 Enter 또는 <b>그래프 적용</b>을 누르세요. 예: <code>sin(x)</code>, <code>x^2</code>, <code>abs(x)</code>.</p></section>
                    <section class="helpSection"><b>2. 여러 그래프 다루기</b><p>각 식은 별도 레이어입니다. 레이어를 선택해 식을 바꾸거나, 표시/숨김을 전환하고, 음량을 조절할 수 있습니다. 숨겨진 레이어는 전체 재생에 포함되지 않습니다.</p></section>
                    <section class="helpSection"><b>3. 그래프를 음악으로</b><p><b>▶ 전체 재생</b> 또는 <b>Graph → Music</b>을 누르세요. 표시 중인 모든 레이어가 동시에 재생됩니다. x축은 곡의 진행 시간, y값은 음높이에 대응하며 재생 중인 점이 각 그래프를 따라 움직입니다.</p></section>
                    <section class="helpSection"><b>4. 음악 설정 및 저장</b><p>Graph → Music 패널에서 곡 길이, BPM(템포), 음계, 음악 스타일을 고른 뒤 재생하세요. <b>정지</b>로 재생을 멈추고 <b>WAV 저장</b>으로 오디오 파일을 내보낼 수 있습니다.</p></section>
                    <section class="helpSection"><b>5. 그래프 화면</b><p>마우스 휠로 확대/축소하고 그래프 영역을 드래그해 이동하세요. ⚙ 설정에서 x·y 범위, 격자, 축 표시를 바꿀 수 있습니다. ⌨ 키패드 버튼으로 수식 기호 패널을 열 수 있습니다.</p></section>
                    <section class="helpSection"><b>6. 수식 예시</b><p><code>sin(x)</code> · <code>cos(2x)</code> · <code>x^2</code> · <code>sqrt(abs(x))</code> · <code>frac(x)</code> · <code>[x]</code> · <code>x mod 2</code></p></section>
                </div>
            </div>

        </aside>

    </div>
</div>

<div class="brandFooter">
    <span>Cosmos · Mathematics in Harmony</span>
    <span>수학적 구조를 발견하고, 시각과 소리의 다른 표현으로 경험합니다.</span>
</div>

</div>
<script>

(function(){

"use strict";


/* 상단 페이지 내비게이션은 작업공간 툴바/레일 구조로 대체되었습니다. */

/* =========================================================
   기본 DOM
========================================================= */

const canvas =
    document.getElementById("graph");

const ctx =
    canvas.getContext("2d");

const expr =
    document.getElementById("expr");
const exprVisual = document.getElementById("exprVisual");

// 내부 계산용 ASCII 수식과 화면에 보이는 수학식 표기를 서로 변환합니다.
let savedMathRange = null;
function selectionInsideMathEditor(){
    const sel=window.getSelection();
    return !!(sel && sel.rangeCount && exprVisual && exprVisual.contains(sel.anchorNode));
}
function saveMathSelection(){
    const sel=window.getSelection();
    if(sel && sel.rangeCount && exprVisual && exprVisual.contains(sel.anchorNode)){
        savedMathRange=sel.getRangeAt(0).cloneRange();
    }
}
function restoreMathSelection(){
    const sel=window.getSelection();
    // 현재 커서가 편집기 안에 있으면 저장된 커서로 덮어쓰지 않습니다.
    if(sel && sel.rangeCount && exprVisual && exprVisual.contains(sel.anchorNode)){
        return sel.getRangeAt(0).cloneRange();
    }
    exprVisual.focus({preventScroll:true});
    const live=window.getSelection();
    if(!live) return null;
    if(savedMathRange && exprVisual.contains(savedMathRange.startContainer) && exprVisual.contains(savedMathRange.endContainer)){
        live.removeAllRanges(); live.addRange(savedMathRange);
        return live.getRangeAt(0).cloneRange();
    }
    const r=document.createRange(); r.selectNodeContents(exprVisual); r.collapse(false);
    live.removeAllRanges(); live.addRange(r); return r;
}
function setMathCaret(range){
    const sel=window.getSelection();
    if(!sel || !range) return;
    range.collapse(true); sel.removeAllRanges(); sel.addRange(range);
    savedMathRange=range.cloneRange();
}
function mathNodeToSource(node){
    if(node.nodeType===Node.TEXT_NODE){
        return (node.nodeValue||"").replace(/\u200B/g,"")
            .replace(/×/g,"*").replace(/÷/g,"/").replace(/[−–]/g,"-").replace(/π/g,"pi");
    }
    if(node.nodeType!==Node.ELEMENT_NODE) return "";
    if(node.matches && node.matches("span.implicitProduct")) return "*";
    if(node.matches && node.matches("sup.mathExponent")){
        const inner=Array.from(node.childNodes).map(mathNodeToSource).join("");
        return inner ? "^("+inner+")" : "^";
    }
    return Array.from(node.childNodes).map(mathNodeToSource).join("");
}
function appendMathSource(parent, source){
    let i=0, plain="";
    const flush=()=>{if(plain){parent.appendChild(document.createTextNode(plain));plain="";}};
    while(i<source.length){
        const ch=source[i];
        if(ch==="^"){
            flush(); i++;
            let exponent="";
            if(source[i]==="("){
                i++; let depth=1; let start=i;
                while(i<source.length && depth>0){if(source[i]==="(")depth++;else if(source[i]===")")depth--;if(depth>0)i++;}
                exponent=source.slice(start,i); if(source[i]===")")i++;
            }else if(i<source.length){
                if(/[+-]/.test(source[i])) exponent+=source[i++];
                if(source[i]==="("){
                    i++; let depth=1; let start=i;
                    while(i<source.length && depth>0){if(source[i]==="(")depth++;else if(source[i]===")")depth--;if(depth>0)i++;}
                    exponent+=source.slice(start,i); if(source[i]===")")i++;
                }else if(/[A-Za-z_]/.test(source[i])){while(i<source.length && /[A-Za-z_]/.test(source[i])) exponent+=source[i++];}
                else if(/[0-9.]/.test(source[i])){while(i<source.length && /[0-9.]/.test(source[i])) exponent+=source[i++];}
            }
            const sup=document.createElement("sup"); sup.className="mathExponent"; sup.setAttribute("data-exp","1");
            appendMathSource(sup,exponent || "\u200B"); parent.appendChild(sup); continue;
        }
        if(ch==="*"){
            const prev=source[i-1]||"", next=source[i+1]||"";
            if((/[0-9)\]]/.test(prev) && /[A-Za-z_(\[]/.test(next))){flush();const product=document.createElement("span");product.className="implicitProduct";product.setAttribute("data-implicit-product","1");product.setAttribute("aria-label","곱하기");parent.appendChild(product);}
            else plain+="×";
            i++; continue;
        }
        if(ch==="p" && source.slice(i,i+2)==="pi"){plain+="π";i+=2;continue;}
        plain += ch==="/" ? "÷" : (ch==="-" ? "−" : ch); i++;
    }
    flush();
}
function syncMathEditorFromSource(){
    if(!exprVisual) return;
    exprVisual.replaceChildren(); appendMathSource(exprVisual,expr.value||""); savedMathRange=null;
}
function syncSourceFromMathEditor(){
    if(!exprVisual) return;
    expr.value=Array.from(exprVisual.childNodes).map(mathNodeToSource).join("");
    saveMathSelection();
}
function insertMathText(text){
    const range=restoreMathSelection();
    const sel=window.getSelection(); if(!sel || !range) return;
    range.deleteContents();
    if(text==="^"){
        const sup=document.createElement("sup");sup.className="mathExponent";sup.setAttribute("data-exp","1");
        const placeholder=document.createTextNode("\u200B");sup.appendChild(placeholder);range.insertNode(sup);
        const caret=document.createRange();caret.setStart(placeholder,1);caret.collapse(true);setMathCaret(caret);
    }else{
        const shown=text==="*"?"×":text==="/"?"÷":text==="-"?"−":text==="pi"?"π":text;
        const node=document.createTextNode(shown);range.insertNode(node);
        const caret=document.createRange();caret.setStartAfter(node);caret.collapse(true);setMathCaret(caret);
    }
    syncSourceFromMathEditor();
    // syncSourceFromMathEditor는 DOM을 재생성하지 않으므로 현재 커서를 다시 저장합니다.
    saveMathSelection();
}
function moveCaretOutsideExponentIfAtEnd(){
    const sel=window.getSelection();
    if(!sel || !sel.isCollapsed || !sel.rangeCount || !exprVisual) return false;
    const current=sel.getRangeAt(0);
    const node=current.startContainer;
    const host=node.nodeType===Node.ELEMENT_NODE ? node : node.parentElement;
    const exponent=host && host.closest ? host.closest("sup.mathExponent") : null;
    if(!exponent || !exprVisual.contains(exponent)) return false;

    // 커서부터 지수 끝까지 실제 문자가 남아 있는지 검사합니다.
    // 서로 다른 DOM 경계점을 비교하는 방식은 브라우저별 contenteditable 처리 차이가 있어
    // 남은 텍스트 범위를 직접 검사합니다.
    let tailText="";
    try {
        const tail=document.createRange();
        tail.setStart(current.startContainer,current.startOffset);
        tail.setEnd(exponent,exponent.childNodes.length);
        tailText=tail.toString().replace(/\u200B/g,"");
    } catch(_) {
        if(current.startContainer===exponent && current.startOffset===exponent.childNodes.length) tailText="";
        else return false;
    }
    if(tailText.length!==0) return false;

    // 지수 바로 뒤에 전용 인라인 편집 지점을 둡니다. 빈 노드에 커서를 두면
    // 일부 브라우저가 커서를 sup 안으로 되돌리므로 zero-width space를 사용합니다.
    let exitPoint=exponent.nextSibling;
    if(!(exitPoint && exitPoint.nodeType===Node.ELEMENT_NODE && exitPoint.classList.contains("mathExitPoint"))){
        exitPoint=document.createElement("span");
        exitPoint.className="mathExitPoint";
        exitPoint.setAttribute("data-math-exit","1");
        exitPoint.appendChild(document.createTextNode("\u200B"));
        exponent.parentNode.insertBefore(exitPoint,exponent.nextSibling);
    } else if(!exitPoint.firstChild){
        exitPoint.appendChild(document.createTextNode("\u200B"));
    }
    let textNode=exitPoint.firstChild;
    if(textNode.nodeType!==Node.TEXT_NODE){
        textNode=document.createTextNode("\u200B");
        exitPoint.replaceChildren(textNode);
    }
    const r=document.createRange();
    r.setStart(textNode,textNode.nodeValue.length);
    r.collapse(true);
    sel.removeAllRanges();
    sel.addRange(r);
    savedMathRange=r.cloneRange();
    exprVisual.focus({preventScroll:true});
    // focus() may reset selection in some engines; reapply after focus.
    const live=window.getSelection();
    if(live){live.removeAllRanges();live.addRange(r);}
    savedMathRange=r.cloneRange();
    return true;
}
if(exprVisual){
    exprVisual.addEventListener("input",syncSourceFromMathEditor);
    exprVisual.addEventListener("keyup",saveMathSelection);
    exprVisual.addEventListener("mouseup",saveMathSelection);
    exprVisual.addEventListener("beforeinput",saveMathSelection);
    exprVisual.addEventListener("focus",saveMathSelection);
    document.addEventListener("selectionchange",()=>{if(selectionInsideMathEditor())saveMathSelection();});
    exprVisual.addEventListener("keydown",e=>{
        if(e.key==="ArrowRight" && moveCaretOutsideExponentIfAtEnd()){
            e.preventDefault();e.stopPropagation();
            syncSourceFromMathEditor();
            saveMathSelection();
            return;
        }
        if(e.key==="^" || e.key==="*"){e.preventDefault();insertMathText(e.key);}
        else if(e.key==="/"){e.preventDefault();insertMathText("/");}
    });
    exprVisual.addEventListener("paste",e=>{
        e.preventDefault();const text=(e.clipboardData||window.clipboardData).getData("text").replace(/\s+/g,"");
        expr.value=text;syncMathEditorFromSource();exprVisual.focus();
        const r=document.createRange();r.selectNodeContents(exprVisual);r.collapse(false);const sel=window.getSelection();sel.removeAllRanges();sel.addRange(r);savedMathRange=r.cloneRange();syncSourceFromMathEditor();
    });
    syncMathEditorFromSource();
}

function syncBpmLabel(){
    const bpm=document.getElementById("bpm");
    const label=document.getElementById("bpmValue");
    if(bpm && label) label.textContent=Math.max(50,Math.min(220,Number(bpm.value)||145))+" BPM";
}
const bpmControl=document.getElementById("bpm");
if(bpmControl){bpmControl.addEventListener("input",syncBpmLabel);syncBpmLabel();}

const msg =
    document.getElementById("message");

const editNotice =
    document.getElementById("editNotice");


/* =========================================================
   그래프 화면
========================================================= */

let xmin = -10;
let xmax = 10;

let ymin = -6;
let ymax = 6;


function W(){
    return canvas.getBoundingClientRect().width;
}


function H(){
    return canvas.getBoundingClientRect().height;
}


function sx(x){

    return (
        (x-xmin) /
        (xmax-xmin)
    ) * W();

}


function sy(y){

    return (
        H() -
        (y-ymin) /
        (ymax-ymin) *
        H()
    );

}


function invx(px){

    return xmin +
        px/W() *
        (xmax-xmin);

}


function invy(py){

    return ymin +
        (H()-py)/H() *
        (ymax-ymin);

}


/* =========================================================
   상태
========================================================= */

let mode = "navigate";

let draggingView = false;

let lastX = 0;
let lastY = 0;

let layerIdCounter = 2;

let selectedLayerId = 1;


/* =========================================================
   오디오
========================================================= */

let audioCtx = null;

let playing = false;

let raf = null;

let playbackStart = 0;

let playbackDuration = 10;

let audioVoices = [];
let backingNodes = [];


/* =========================================================
   Edit 상태
========================================================= */

let editAction = null;

let editPointerId = null;

let editStartX = 0;

let editStartY = 0;

let editStartTx = 0;

let editStartTy = 0;

let editStartScale = 1;

let editStartDistance = 1;

let editStartRotation = 0;

let editStartAngle = 0;


/* =========================================================
   Library 상태
========================================================= */

const LIBRARY_KEY =
    "cosmos_v31_libraries";

let libraries = [];

let currentLibraryId = "";

let currentSongId = null;


/* =========================================================
   레이어 색상
========================================================= */

const layerColors = [

    "#91a4ff",
    "#ff8fab",
    "#7ee7c4",
    "#ffd166",
    "#c49bff",
    "#67d8ff",
    "#ff9f68",
    "#b8f27c"

];


/* =========================================================
   레이어
========================================================= */

let layers = [

    {

        id:1,

        name:"Graph 1",

        type:"function",

        expression:"sin(x)",

        visible:true,

        volume:0.55,

        color:layerColors[0],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    },


    {

        id:2,

        name:"Graph 2",

        type:"function",

        expression:"0.5*cos(2*x)",

        visible:true,

        volume:0.40,

        color:layerColors[1],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    }

];


/* =========================================================
   수식 파서
========================================================= */

const funcs = {

    sin:Math.sin,

    cos:Math.cos,

    tan:Math.tan,

    sqrt:Math.sqrt,

    abs:Math.abs,

    log:Math.log,

    ln:Math.log,

    exp:Math.exp,

    asin:Math.asin,

    acos:Math.acos,

    atan:Math.atan,
    frac:x=>x-Math.floor(x),
    floor:Math.floor,
    ceil:Math.ceil,
    round:Math.round

};


function tokenize(s){

    s = s
        .replace(/π/g,"pi")
        .replace(/√/g,"sqrt")
        .replace(/[×·⋅]/g,"*")
        .replace(/÷/g,"/")
        .replace(/[−–—]/g,"-")
        .replace(/ /g," ");

    const tokens = [];

    let i = 0;

    while(i < s.length){

        if(/\s/.test(s[i])){

            i++;

            continue;

        }


        if(/[0-9.]/.test(s[i])){

            let j = i+1;

            while(
                j < s.length &&
                /[0-9.]/.test(s[j])
            ){
                j++;
            }

            const n =
                Number(
                    s.slice(i,j)
                );

            if(!Number.isFinite(n)){
                throw Error("숫자를 확인하세요.");
            }

            tokens.push({
                t:"num",
                v:n
            });

            i=j;

            continue;

        }


        if(/[A-Za-z_]/.test(s[i])){

            let j=i+1;

            while(
                j<s.length &&
                /[A-Za-z_]/.test(s[j])
            ){
                j++;
            }

            const word = s.slice(i,j).toLowerCase();
            tokens.push({
                t: word === "mod" ? "mod" : "id",
                v: word
            });

            i=j;

            continue;

        }


        if("+-*/^(),[]".includes(s[i])){

            tokens.push({

                t:s[i],

                v:s[i]

            });

            i++;

            continue;

        }


        throw Error(
            "지원하지 않는 문자가 있습니다: " +
            s[i]
        );

    }

    return tokens;

}


function parseExpression(s){

    const ts =
        tokenize(s);

    let p=0;


    function primary(){

        const z=ts[p];

        if(!z){
            throw Error(
                "수식이 완성되지 않았습니다."
            );
        }


        if(z.t==="num"){

            p++;

            return ()=>z.v;

        }


        if(z.t==="id"){

            p++;


            if(z.v==="x"){
                return x=>x;
            }


            if(z.v==="pi"){
                return ()=>Math.PI;
            }


            if(z.v==="e"){
                return ()=>Math.E;
            }


            if(funcs[z.v]){

                if(
                    !ts[p] ||
                    ts[p].t!=="("
                ){
                    throw Error(
                        z.v +
                        " 뒤에 괄호가 필요합니다."
                    );
                }

                p++;

                const a =
                    addsub();

                if(
                    !ts[p] ||
                    ts[p].t!==")"
                ){
                    throw Error(
                        "괄호를 닫아주세요."
                    );
                }

                p++;

                return x =>
                    funcs[z.v](a(x));

            }


            throw Error(
                "알 수 없는 함수/변수: " +
                z.v
            );

        }


        if(z.t==="("){

            p++;

            const a =
                addsub();

            if(
                !ts[p] ||
                ts[p].t!==")"
            ){
                throw Error(
                    "괄호를 닫아주세요."
                );
            }

            p++;

            return a;

        }

        // [x] 표기는 가우스 기호(내림 함수)로 처리합니다.
        if(z.t==="["){
            p++;
            const a=addsub();
            if(!ts[p] || ts[p].t!=="]"){
                throw Error("대괄호 ]를 닫아주세요.");
            }
            p++;
            return x=>Math.floor(a(x));
        }


        if(z.t==="+"){

            p++;

            return primary();

        }


        if(z.t==="-"){

            p++;

            const a =
                primary();

            return x=>-a(x);

        }


        throw Error(
            "수식을 확인하세요."
        );

    }


    function power(){

        let a =
            primary();

        if(
            ts[p] &&
            ts[p].t==="^"
        ){

            p++;

            const b =
                power();

            const aa =
                a;

            return x =>
                Math.pow(
                    aa(x),
                    b(x)
                );

        }

        return a;

    }


    function muldiv(){
        let a=power();
        while(ts[p]){
            const token=ts[p];
            const isExplicit = token.t==="*" || token.t==="/" || token.t==="mod";
            const beginsPrimary = token.t==="num" || token.t==="id" || token.t==="(" || token.t==="[";
            if(!isExplicit && !beginsPrimary) break;
            const op = isExplicit ? ts[p++].t : "*";
            const b=power();
            const aa=a;
            if(op==="*") a=x=>aa(x)*b(x);
            else if(op==="/") a=x=>aa(x)/b(x);
            else a=x=>{const divisor=b(x); return ((aa(x)%divisor)+divisor)%divisor;};
        }
        return a;
    }

    function addsub(){

        let a =
            muldiv();

        while(
            ts[p] &&
            (
                ts[p].t==="+" ||
                ts[p].t==="-"
            )
        ){

            const op =
                ts[p++].t;

            const b =
                muldiv();

            const aa =
                a;

            if(op==="+"){

                a =
                    x =>
                        aa(x)+b(x);

            }else{

                a =
                    x =>
                        aa(x)-b(x);

            }

        }

        return a;

    }


    const f =
        addsub();

    if(
        p!==ts.length
    ){
        throw Error(
            "수식을 확인하세요."
        );
    }

    return f;

}


/* =========================================================
   중심
========================================================= */

function getCenter(points){

    if(!points.length){

        return {
            x:0,
            y:0
        };

    }


    let ax=0;
    let ay=0;

    points.forEach(p=>{

        ax+=p.x;
        ay+=p.y;

    });


    return {

        x:
            ax/points.length,

        y:
            ay/points.length

    };

}


/* =========================================================
   함수 그래프 생성
========================================================= */

function generateFunctionPoints(expression){

    const f =
        parseExpression(
            expression
        );

    const result=[];

    const N=1200;


    for(
        let i=0;
        i<=N;
        i++
    ){

        const x =
            xmin +
            (xmax-xmin) *
            i/N;

        let y;

        try{

            y=f(x);

        }catch(e){

            y=NaN;

        }


        if(
            Number.isFinite(y) &&
            Math.abs(y)<100000
        ){

            result.push({

                x:x,

                y:y,

                cx:x,

                cy:y

            });

        }

    }


    return result;

}


/* =========================================================
   주기 함수 작업용 자동 보기 맞춤
========================================================= */
function refreshFunctionLayerPoints(layer){
    if(!layer || layer.type!=="function" || !layer.expression) return;
    const points=generateFunctionPoints(layer.expression);
    const center=getCenter(points);
    points.forEach(p=>{p.cx=center.x;p.cy=center.y;});
    layer.points=points;
}

function fitPeriodicWorkspace(){
    // mod가 들어간 식은 반복 구간과 음표 패턴을 한눈에 보기 쉽게 표시합니다.
    if(xmax-xmin>10 || xmin<0 || xmax>10){
        xmin=0;
        xmax=3.2;
    }
    layers.forEach(layer=>{
        if(layer.type==="function") refreshFunctionLayerPoints(layer);
    });
    const values=[];
    layers.filter(layer=>layer.visible).forEach(layer=>{
        (layer.points||[]).forEach(point=>{
            if(Number.isFinite(point.y)) values.push(point.y);
        });
    });
    if(values.length){
        const low=Math.min(...values);
        const high=Math.max(...values);
        const span=Math.max(1,high-low);
        const pad=Math.max(0.8,span*0.1);
        ymin=low-pad;
        ymax=high+pad;
    }
    syncViewInputs();
}


/* =========================================================
   변환
========================================================= */

function transformPoint(
    point,
    transform
){

    const x0 =
        point.x-point.cx;

    const y0 =
        point.y-point.cy;

    const c =
        Math.cos(
            transform.rotation
        );

    const s =
        Math.sin(
            transform.rotation
        );


    const x1 =
        (
            x0*c -
            y0*s
        ) *
        transform.scale;


    const y1 =
        (
            x0*s +
            y0*c
        ) *
        transform.scale;


    return {

        x:
            point.cx +
            x1 +
            transform.tx,

        y:
            point.cy +
            y1 +
            transform.ty

    };

}


function transformedPoints(layer){

    if(
        !layer ||
        !layer.points ||
        !layer.points.length
    ){
        return [];
    }


    return layer.points.map(
        p =>
            transformPoint(
                p,
                layer.transform
            )
    );

}


/* =========================================================
   선택 레이어
========================================================= */

function selectedLayer(){

    return layers.find(
        l =>
            l.id ===
            selectedLayerId
    ) || null;

}


function selectLayer(id){

    const exists =
        layers.some(
            l => l.id === id
        );

    if(!exists){
        return;
    }

    selectedLayerId=id;

    const l=
        selectedLayer();

    expr.value =
        l.expression || "";
    syncMathEditorFromSource();

    renderLayers();

    draw();

}


/* =========================================================
   레이어 UI
========================================================= */

function playExpressionSound(layer, button){
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) { alert("이 브라우저는 웹 오디오를 지원하지 않습니다."); return; }
        if (!audioCtx || audioCtx.state === "closed") audioCtx = new AudioCtx();
        audioCtx.resume();
        const ctx = audioCtx;
        const gain = ctx.createGain();
        const osc = ctx.createOscillator();
        const now = ctx.currentTime;
        const duration = 6;
        const samples = 240;
        const parse = layer.type === "function" ? parseExpression(layer.expression || "0") : null;
        const pts = layer.type === "function" ? null : (layer.points || []);
        osc.type = "sine";
        gain.gain.setValueAtTime(0.0001, now);
        gain.gain.linearRampToValueAtTime(Math.max(0.015, Math.min(0.13, Number(layer.volume ?? 0.6) * 0.12)), now + 0.04);
        gain.gain.setValueAtTime(Math.max(0.015, Math.min(0.13, Number(layer.volume ?? 0.6) * 0.12)), now + duration - 0.08);
        gain.gain.linearRampToValueAtTime(0.0001, now + duration);
        osc.connect(gain); gain.connect(ctx.destination);
        for (let i=0; i<=samples; i++) {
            const t=i/samples;
            const x=xmin+(xmax-xmin)*t;
            let y=0;
            try {
                if (parse) y=parse(x);
                else if (pts && pts.length) {
                    const index=Math.min(pts.length-1, Math.round(t*(pts.length-1)));
                    y=pts[index].y;
                }
            } catch(_e) { y=NaN; }
            const at=now+t*duration;
            if (Number.isFinite(y)) {
                const bounded=Math.max(-8,Math.min(8,y));
                const hz=220*Math.pow(2,bounded/12);
                osc.frequency.setValueAtTime(Math.max(55,Math.min(1760,hz)),at);
            } else {
                // Undefined sections are represented by a very quiet low tone.
                osc.frequency.setValueAtTime(55,at);
            }
        }
        layer.soundPlaying=true;
        button.classList.add("active"); button.textContent="Ⅱ";
        osc.start(now); osc.stop(now+duration+0.03);
        const cleanup=()=>{ layer.soundPlaying=false; layer.soundStop=null; button.classList.remove("active"); button.textContent="🔊"; try{gain.disconnect();}catch(_e){} };
        osc.onended=cleanup;
        layer.soundStop=()=>{ try{gain.gain.cancelScheduledValues(ctx.currentTime); gain.gain.setTargetAtTime(0.0001,ctx.currentTime,0.02); osc.stop(ctx.currentTime+0.08);}catch(_e){cleanup();} };
    } catch(err) { console.error(err); alert("소리를 재생하지 못했습니다. 그래프 식을 확인해 주세요."); }
}

function renderLayers(){

    const box =
        document.getElementById(
            "layerList"
        );

    box.innerHTML="";


    layers.forEach(layer=>{

        const item =
            document.createElement(
                "div"
            );

        item.className =
            "layerItem" +
            (
                layer.id===selectedLayerId
                ? " selected"
                : ""
            );


        const top =
            document.createElement(
                "div"
            );

        top.className =
            "layerTop";


        const dot =
            document.createElement(
                "span"
            );

        dot.className =
            "layerColor";

        dot.style.background =
            layer.color;


        const nameInput =
            document.createElement(
                "input"
            );

        nameInput.type="text";

        nameInput.value =
            layer.name;

        nameInput.className =
            "layerNameInput";


        const type =
            document.createElement(
                "span"
            );

        type.className =
            "layerType";

        type.textContent =
            layer.type==="function"
            ? "FUNCTION"
            : "SKETCH";


        top.appendChild(dot);

        top.appendChild(
            nameInput
        );

        top.appendChild(type);


        const actions =
            document.createElement(
                "div"
            );

        actions.className =
            "layerActions";


        const visibility =
            document.createElement(
                "button"
            );

        visibility.className =
            "visibility";

        visibility.textContent =
            layer.visible
            ? "👁 표시"
            : "○ 숨김";


        const soundButton = document.createElement("button");
        soundButton.className = "layerSoundBtn" + (layer.soundPlaying ? " active" : "");
        soundButton.type = "button";
        soundButton.title = "이 그래프 소리 재생/정지";
        soundButton.textContent = layer.soundPlaying ? "Ⅱ" : "🔊";
        soundButton.setAttribute("aria-label", "그래프 소리 재생/정지");

        const volumeBox =
            document.createElement(
                "div"
            );

        volumeBox.className =
            "volumeBox";


        const volumeHeader =
            document.createElement(
                "div"
            );

        volumeHeader.className =
            "volumeHeader";


        const volumeText =
            document.createElement(
                "span"
            );

        volumeText.textContent =
            "음량";


        const volumeValue =
            document.createElement(
                "span"
            );

        volumeValue.textContent =
            Math.round(
                layer.volume*100
            ) + "%";


        volumeHeader.appendChild(
            volumeText
        );

        volumeHeader.appendChild(
            volumeValue
        );


        const volume =
            document.createElement(
                "input"
            );

        volume.type="range";

        volume.min="0";

        volume.max="1";

        volume.step="0.01";

        volume.value =
            layer.volume;

        volume.className =
            "layerVolume";


        volumeBox.appendChild(
            volumeHeader
        );

        volumeBox.appendChild(
            volume
        );


        actions.appendChild(visibility);
        actions.appendChild(soundButton);
        actions.appendChild(volumeBox);


        item.appendChild(top);

        item.appendChild(actions);


        /*
           선택은 layerItem 자체에서만 처리.
           내부 입력/버튼은 selection 이벤트가
           부모로 전파되지 않도록 막는다.
        */

        top.addEventListener(
            "click",
            e=>{
                if(
                    e.target === nameInput
                ){
                    return;
                }
                selectLayer(layer.id);
            }
        );


        item.addEventListener(
            "click",
            e=>{
                if(
                    e.target === visibility ||
                    e.target === volume ||
                    actions.contains(e.target)
                ){
                    e.stopPropagation();
                }
            }
        );


        item.addEventListener(
            "pointerdown",
            e=>{
                if(
                    actions.contains(e.target) ||
                    e.target === nameInput
                ){
                    e.stopPropagation();
                }
            }
        );


        nameInput.addEventListener(
            "click",
            e=>{
                e.stopPropagation();
            }
        );


        nameInput.addEventListener(
            "pointerdown",
            e=>{
                e.stopPropagation();
            }
        );


        nameInput.addEventListener(
            "change",
            e=>{

                const newName =
                    e.target.value.trim();

                layer.name =
                    newName ||
                    "Graph " +
                    layer.id;

                e.target.value =
                    layer.name;

                updateSelectedInfo();

            }
        );


        soundButton.addEventListener("pointerdown", e=>e.stopPropagation());
        soundButton.addEventListener("click", e=>{
            e.stopPropagation();
            if (layer.soundPlaying && layer.soundStop) {
                layer.soundStop();
                layer.soundPlaying = false;
                layer.soundStop = null;
                soundButton.classList.remove("active");
                soundButton.textContent = "🔊";
            } else {
                playExpressionSound(layer, soundButton);
            }
        });

        visibility.addEventListener(
            "click",
            e=>{

                e.stopPropagation();

                layer.visible =
                    !layer.visible;

                renderLayers();

                draw();

            }
        );


        visibility.addEventListener(
            "pointerdown",
            e=>{
                e.stopPropagation();
            }
        );


        volume.addEventListener(
            "click",
            e=>{

                e.stopPropagation();

            }
        );


        volume.addEventListener(
            "pointerdown",
            e=>{

                e.stopPropagation();

            }
        );


        volume.addEventListener(
            "input",
            e=>{

                e.stopPropagation();

                layer.volume =
                    Number(
                        e.target.value
                    );

                volumeValue.textContent =
                    Math.round(
                        layer.volume*100
                    ) + "%";

            }
        );


        box.appendChild(item);

    });


    document.getElementById(
        "layerCount"
    ).textContent =
        layers.length +
        "개 레이어 · " +
        layers.filter(
            l=>l.visible
        ).length +
        "개 재생";


    updateSelectedInfo();
    renderArrangement(playing && playbackDuration ? Math.max(0,Math.min(1,((performance.now()-playbackStart)/1000)/playbackDuration)) : 0);

}


/* =========================================================
   선택 레이어 정보
========================================================= */

function updateSelectedInfo(){

    const selected =
        selectedLayer();

    const box =
        document.getElementById(
            "selectedLayerInfo"
        );


    if(!selected){

        box.textContent =
            "선택 없음";

        return;

    }


    box.textContent =
        selected.name +
        " · " +
        (
            selected.type ===
            "function"
            ? "함수"
            : "손그림"
        );

}


/* =========================================================
   함수 그래프 생성
========================================================= */

document
.getElementById("draw")
.addEventListener(
    "click",
    ()=>{

        const layer =
            selectedLayer();

        if(!layer){
            return;
        }


        try{

            const points =
                generateFunctionPoints(
                    expr.value.trim()
                );


            if(points.length<10){

                throw Error(
                    "그래프를 충분히 생성할 수 없습니다."
                );

            }


            const center =
                getCenter(points);


            points.forEach(p=>{

                p.cx =
                    center.x;

                p.cy =
                    center.y;

            });


            layer.type =
                "function";

            layer.expression =
                expr.value.trim();

            layer.points =
                points;

            // 수식 유형에 따라 참고 이미지와 비슷한 색을 자동 적용합니다.
            if(/frac\s*\(|\[[^\]]+\]/i.test(layer.expression) && /\bmod\b/i.test(layer.expression)){
                layer.color="#f0cf4a";
            }else if(/\be\s*\^/i.test(layer.expression) && /\^/.test(layer.expression) && /\bmod\b/i.test(layer.expression)){
                layer.color="#202124";
            }

            layer.transform={

                tx:0,

                ty:0,

                scale:1,

                rotation:0

            };

            if(/\bmod\b/i.test(layer.expression)){
                fitPeriodicWorkspace();
            }

            msg.textContent="";

            renderLayers();

            draw();

        }catch(e){

            msg.textContent =
                e.message;

        }

    }
);


/* =========================================================
   레이어 추가
========================================================= */

function addLayer(type){

    layerIdCounter++;


    const index =
        (
            layers.length
        ) %
        layerColors.length;


    const layer={

        id:
            layerIdCounter,

        name:
            type==="function"
            ? "Function " +
                layerIdCounter
            : "Sketch " +
                layerIdCounter,

        type:type,

        expression:
            type==="function"
            ? "sin(x)"
            : "",

        visible:true,

        volume:
            type==="function"
            ? 0.45
            : 0.35,

        color:
            layerColors[index],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    };


    if(
        type==="function"
    ){

        try{

            const points =
                generateFunctionPoints(
                    layer.expression
                );

            const center =
                getCenter(points);


            points.forEach(p=>{

                p.cx =
                    center.x;

                p.cy =
                    center.y;

            });


            layer.points =
                points;

        }catch(e){}

    }


    layers.push(layer);

    selectedLayerId =
        layer.id;

    expr.value =
        layer.expression;
    syncMathEditorFromSource();

    renderLayers();

    draw();

}


document
.getElementById(
    "addFunctionLayer"
)
.addEventListener(
    "click",
    ()=>{
        addLayer("function");
    }
);


document
.getElementById(
    "addSketchLayer"
)
.addEventListener(
    "click",
    ()=>{
        addLayer("sketch");
    }
);


/* =========================================================
   레이어 삭제
========================================================= */

document
.getElementById(
    "deleteLayer"
)
.addEventListener(
    "click",
    ()=>{

        if(
            layers.length<=1
        ){

            msg.textContent =
                "최소 한 개의 레이어는 필요합니다.";

            return;

        }


        const index =
            layers.findIndex(
                l =>
                    l.id ===
                    selectedLayerId
            );


        layers =
            layers.filter(
                l =>
                    l.id !==
                    selectedLayerId
            );


        selectedLayerId =
            layers[
                Math.max(
                    0,
                    index-1
                )
            ].id;


        expr.value =
            selectedLayer()
            ?.expression || "";
        syncMathEditorFromSource();

        renderLayers();

        draw();

    }
);


/* =========================================================
   손그림
========================================================= */

let sketchPoints=[];


canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        const layer =
            selectedLayer();

        if(!layer){
            return;
        }


        sketchPoints=[];


        const rect =
            canvas.getBoundingClientRect();


        const x =
            invx(
                e.clientX -
                rect.left
            );


        const y =
            invy(
                e.clientY -
                rect.top
            );


        sketchPoints.push({

            x:x,

            y:y

        });


        canvas.setPointerCapture(
            e.pointerId
        );

    }
);


canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        if(
            !sketchPoints.length
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const x =
            invx(
                e.clientX -
                rect.left
            );


        const y =
            invy(
                e.clientY -
                rect.top
            );


        sketchPoints.push({

            x:x,

            y:y

        });


        drawSketchPreview();

    }
);


canvas.addEventListener(
    "pointerup",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        if(
            sketchPoints.length<5
        ){

            sketchPoints=[];

            draw();

            return;

        }


        const layer =
            selectedLayer();


        if(!layer){
            return;
        }


        const simplified =
            simplifyPoints(
                sketchPoints,
                2
            );


        const center =
            getCenter(
                simplified
            );


        layer.type =
            "sketch";

        layer.expression="";


        layer.points =
            simplified.map(
                p=>({

                    x:p.x,

                    y:p.y,

                    cx:center.x,

                    cy:center.y

                })
            );


        layer.transform={

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        };


        sketchPoints=[];


        renderLayers();

        draw();

    }
);


function simplifyPoints(
    points,
    step
){

    const result=[];


    for(
        let i=0;
        i<points.length;
        i+=step
    ){

        result.push({

            x:
                points[i].x,

            y:
                points[i].y

        });

    }


    return result;

}


/* =========================================================
   손그림 미리보기
========================================================= */

function drawSketchPreview(){

    draw();


    if(
        sketchPoints.length<2
    ){
        return;
    }


    const layer =
        selectedLayer();


    if(!layer){
        return;
    }


    ctx.save();


    ctx.strokeStyle =
        layer.color;

    ctx.lineWidth=4;

    ctx.lineCap="round";

    ctx.lineJoin="round";


    ctx.beginPath();


    sketchPoints.forEach(
        (p,i)=>{

            const px =
                sx(p.x);

            const py =
                sy(p.y);


            if(i===0){

                ctx.moveTo(
                    px,
                    py
                );

            }else{

                ctx.lineTo(
                    px,
                    py
                );

            }

        }
    );


    ctx.stroke();

    ctx.restore();

}


/* =========================================================
   Edit 도구
========================================================= */

function getEditData(layer){

    if(
        !layer ||
        !layer.points.length
    ){
        return null;
    }


    const points =
        transformedPoints(
            layer
        );


    if(
        points.length<2
    ){
        return null;
    }


    const screenPoints =
        points.map(
            p=>({

                x:sx(p.x),

                y:sy(p.y)

            })
        );


    let minX=Infinity;

    let maxX=-Infinity;

    let minY=Infinity;

    let maxY=-Infinity;


    screenPoints.forEach(p=>{

        minX=Math.min(
            minX,
            p.x
        );

        maxX=Math.max(
            maxX,
            p.x
        );

        minY=Math.min(
            minY,
            p.y
        );

        maxY=Math.max(
            maxY,
            p.y
        );

    });


    const center =
        getCenter(points);


    const cx =
        sx(center.x);

    const cy =
        sy(center.y);


    return {

        points:screenPoints,

        minX:minX,

        maxX:maxX,

        minY:minY,

        maxY:maxY,

        centerX:cx,

        centerY:cy

    };

}


function getEditHandles(layer){

    const data =
        getEditData(layer);


    if(!data){
        return null;
    }


    const size=8;


    const corners=[

        {
            type:"scale",
            x:data.minX,
            y:data.minY
        },

        {
            type:"scale",
            x:data.maxX,
            y:data.minY
        },

        {
            type:"scale",
            x:data.minX,
            y:data.maxY
        },

        {
            type:"scale",
            x:data.maxX,
            y:data.maxY
        },

        {
            type:"rotate",
            x:
                (
                    data.minX+
                    data.maxX
                )/2,

            y:
                data.minY-36
        }

    ];


    return {
        corners:corners,
        size:size
    };

}


function distance(
    x1,
    y1,
    x2,
    y2
){

    return Math.hypot(
        x1-x2,
        y1-y2
    );

}


function distanceToSegment(
    px,
    py,
    ax,
    ay,
    bx,
    by
){

    const dx =
        bx-ax;

    const dy =
        by-ay;


    const len2 =
        dx*dx+
        dy*dy;


    if(
        len2===0
    ){

        return distance(
            px,
            py,
            ax,
            ay
        );

    }


    let t =
        (
            (
                px-ax
            )*dx+
            (
                py-ay
            )*dy
        ) /
        len2;


    t =
        Math.max(
            0,
            Math.min(
                1,
                t
            )
        );


    const x =
        ax+t*dx;

    const y =
        ay+t*dy;


    return distance(
        px,
        py,
        x,
        y
    );

}


function pointNearLayer(
    layer,
    px,
    py
){

    const data =
        getEditData(layer);


    if(!data){
        return false;
    }


    for(
        let i=1;
        i<data.points.length;
        i++
    ){

        const a =
            data.points[i-1];

        const b =
            data.points[i];


        if(
            distanceToSegment(
                px,
                py,
                a.x,
                a.y,
                b.x,
                b.y
            ) <= 12
        ){
            return true;
        }

    }


    return false;

}


function pointInsideBox(
    data,
    px,
    py
){

    return (
        px>=data.minX-8 &&
        px<=data.maxX+8 &&
        py>=data.minY-8 &&
        py<=data.maxY+8
    );

}


function nearHandle(
    handle,
    px,
    py,
    radius=14
){

    return (
        distance(
            px,
            py,
            handle.x,
            handle.y
        ) <= radius
    );

}


/* =========================================================
   Edit Pointer Down
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode !==
            "edit"
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        const current =
            selectedLayer();


        /*
           1. 선택된 그래프의 핸들을 먼저 검사
        */

        if(current){

            const handles =
                getEditHandles(
                    current
                );


            if(handles){

                const rotateHandle =
                    handles.corners.find(
                        h =>
                            h.type==="rotate"
                    );


                if(
                    rotateHandle &&
                    nearHandle(
                        rotateHandle,
                        px,
                        py,
                        16
                    )
                ){

                    editAction =
                        "rotate";

                    editPointerId =
                        e.pointerId;

                    const data =
                        getEditData(
                            current
                        );


                    editStartX =
                        px;

                    editStartY =
                        py;

                    editStartRotation =
                        current.transform.rotation;

                    editStartAngle =
                        Math.atan2(
                            py-data.centerY,
                            px-data.centerX
                        );


                    canvas.setPointerCapture(
                        e.pointerId
                    );

                    return;

                }


                const scaleHandle =
                    handles.corners.find(
                        h =>
                            h.type==="scale" &&
                            nearHandle(
                                h,
                                px,
                                py,
                                15
                            )
                    );


                if(scaleHandle){

                    editAction =
                        "scale";

                    editPointerId =
                        e.pointerId;

                    const data =
                        getEditData(
                            current
                        );


                    editStartScale =
                        current.transform.scale;

                    editStartDistance =
                        distance(
                            px,
                            py,
                            data.centerX,
                            data.centerY
                        );


                    editStartX=px;

                    editStartY=py;


                    canvas.setPointerCapture(
                        e.pointerId
                    );

                    return;

                }

            }

        }


        /*
           2. 그래프 선을 클릭했는지 검사
           뒤에 그려진 레이어부터 검사
        */

        let hitLayer=null;


        for(
            let i=
                layers.length-1;
            i>=0;
            i--
        ){

            const layer =
                layers[i];


            if(
                !layer.visible ||
                layer.points.length<2
            ){
                continue;
            }


            if(
                pointNearLayer(
                    layer,
                    px,
                    py
                )
            ){

                hitLayer =
                    layer;

                break;

            }

        }


        if(hitLayer){

            selectLayer(
                hitLayer.id
            );


            editAction =
                "move";

            editPointerId =
                e.pointerId;


            editStartX =
                px;

            editStartY =
                py;


            editStartTx =
                hitLayer.transform.tx;

            editStartTy =
                hitLayer.transform.ty;


            canvas.setPointerCapture(
                e.pointerId
            );

            return;

        }


        /*
           3. 선택된 그래프 내부를 클릭해도 이동
        */

        if(current){

            const data =
                getEditData(
                    current
                );


            if(
                data &&
                pointInsideBox(
                    data,
                    px,
                    py
                )
            ){

                editAction =
                    "move";

                editPointerId =
                    e.pointerId;


                editStartX=px;

                editStartY=py;


                editStartTx =
                    current.transform.tx;

                editStartTy =
                    current.transform.ty;


                canvas.setPointerCapture(
                    e.pointerId
                );

            }

        }

    }
);


/* =========================================================
   Edit Pointer Move
========================================================= */

canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode !==
            "edit"
        ){
            return;
        }


        const layer =
            selectedLayer();


        if(
            !layer ||
            !editAction
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        if(
            editAction ===
            "move"
        ){

            const dx =
                px -
                editStartX;

            const dy =
                py -
                editStartY;


            layer.transform.tx =
                editStartTx +
                dx/W() *
                (xmax-xmin);


            layer.transform.ty =
                editStartTy -
                dy/H() *
                (ymax-ymin);


        }else if(
            editAction ===
            "scale"
        ){

            const data =
                getEditData(
                    layer
                );


            if(!data){
                return;
            }


            const currentDistance =
                distance(
                    px,
                    py,
                    data.centerX,
                    data.centerY
                );


            if(
                editStartDistance>0
            ){

                layer.transform.scale =
                    editStartScale *
                    (
                        currentDistance /
                        editStartDistance
                    );


                layer.transform.scale =
                    Math.max(
                        0.15,
                        Math.min(
                            5,
                            layer.transform.scale
                        )
                    );

            }


        }else if(
            editAction ===
            "rotate"
        ){

            const data =
                getEditData(
                    layer
                );


            if(!data){
                return;
            }


            const angle =
                Math.atan2(
                    py-data.centerY,
                    px-data.centerX
                );


            const delta =
                angle -
                editStartAngle;


            layer.transform.rotation =
                editStartRotation +
                delta;

        }


        draw();

    }
);


/* =========================================================
   Edit Pointer Up
========================================================= */

function endEdit(){

    editAction=null;

    editPointerId=null;

}


canvas.addEventListener(
    "pointerup",
    endEdit
);


canvas.addEventListener(
    "pointercancel",
    endEdit
);


/* =========================================================
   Edit Hover Cursor
========================================================= */

canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode!=="edit"
        ){
            return;
        }


        if(editAction){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        const current =
            selectedLayer();


        if(current){

            const handles =
                getEditHandles(
                    current
                );


            if(handles){

                if(
                    handles.corners.some(
                        h =>
                            nearHandle(
                                h,
                                px,
                                py,
                                15
                            )
                    )
                ){

                    const rotate =
                        handles.corners.find(
                            h =>
                                h.type ===
                                "rotate" &&
                                nearHandle(
                                    h,
                                    px,
                                    py,
                                    15
                                )
                        );


                    canvas.style.cursor =
                        rotate
                        ? "crosshair"
                        : "nwse-resize";

                    return;

                }

            }

        }


        canvas.style.cursor =
            "default";

    }
);


/* =========================================================
   모드
========================================================= */

function setMode(newMode){

    mode =
        newMode;


    document
    .getElementById(
        "navigateMode"
    )
    .classList.toggle(
        "active",
        mode==="navigate"
    );


    document
    .getElementById(
        "sketchMode"
    )
    .classList.toggle(
        "active",
        mode==="sketch"
    );


    document
    .getElementById(
        "editMode"
    )
    .classList.toggle(
        "active",
        mode==="edit"
    );


    editNotice.classList.toggle(
        "active",
        mode==="edit"
    );


    editAction=null;


    if(
        mode!=="edit"
    ){
        canvas.style.cursor =
            "default";
    }


    draw();

}


document
.getElementById(
    "navigateMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("navigate");
    }
);


document
.getElementById(
    "sketchMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("sketch");
    }
);


document
.getElementById(
    "editMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("edit");
    }
);


/* =========================================================
   레이어 지우기
========================================================= */

document
.getElementById(
    "clearLayer"
)
.addEventListener(
    "click",
    ()=>{

        const l =
            selectedLayer();

        if(!l){
            return;
        }


        l.points=[];

        l.expression="";


        expr.value="";
        syncMathEditorFromSource();

        renderLayers();

        draw();

    }
);


/* =========================================================
   화면 이동
========================================================= */

function changeView(
    factor,
    dx=0,
    dy=0
){

    const cx =
        (
            xmin+xmax
        )/2 +
        dx *
        (
            xmax-xmin
        );


    const cy =
        (
            ymin+ymax
        )/2 +
        dy *
        (
            ymax-ymin
        );


    const xr =
        (
            xmax-xmin
        ) *
        factor;


    const yr =
        (
            ymax-ymin
        ) *
        factor;


    xmin =
        cx-xr/2;

    xmax =
        cx+xr/2;

    ymin =
        cy-yr/2;

    ymax =
        cy+yr/2;


    draw();

}


/* =========================================================
   화면 드래그
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode!=="navigate"
        ){
            return;
        }


        draggingView=true;

        lastX=e.clientX;

        lastY=e.clientY;


        canvas.setPointerCapture(
            e.pointerId
        );

    }
);


canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode!=="navigate" ||
            !draggingView
        ){
            return;
        }


        const dx =
            e.clientX-lastX;

        const dy =
            e.clientY-lastY;


        const xr =
            xmax-xmin;

        const yr =
            ymax-ymin;


        xmin -=
            dx/W()*xr;

        xmax -=
            dx/W()*xr;


        ymin +=
            dy/H()*yr;

        ymax +=
            dy/H()*yr;


        lastX=
            e.clientX;

        lastY=
            e.clientY;


        draw();

    }
);


canvas.addEventListener(
    "pointerup",
    ()=>{
        draggingView=false;
    }
);


canvas.addEventListener(
    "pointercancel",
    ()=>{
        draggingView=false;
    }
);


/* =========================================================
   휠 확대
========================================================= */

canvas.addEventListener(
    "wheel",
    e=>{

        if(
            mode!=="navigate"
        ){
            return;
        }


        e.preventDefault();


        const factor =
            e.deltaY<0
            ? .8
            : 1.25;


        const mx =
            invx(
                e.offsetX
            );


        const my =
            invy(
                e.offsetY
            );


        xmin =
            mx +
            (
                xmin-mx
            )*factor;


        xmax =
            mx +
            (
                xmax-mx
            )*factor;


        ymin =
            my +
            (
                ymin-my
            )*factor;


        ymax =
            my +
            (
                ymax-my
            )*factor;


        draw();

    },
    {
        passive:false
    }
);


/* =========================================================
   그래프 그리기
========================================================= */

function niceStep(range){

    const raw =
        range/10;


    const p =
        Math.pow(
            10,
            Math.floor(
                Math.log10(raw)
            )
        );


    const n =
        raw/p;


    return (
        n<1.5
        ?1
        :n<3
        ?2
        :n<7
        ?5
        :10
    )*p;

}


function fmt(v){

    if(
        !Number.isFinite(v)
    ){
        return "—";
    }


    if(
        Math.abs(v)<1e-9
    ){
        return "0";
    }


    if(
        Math.abs(v)>=100
    ){
        return Math.round(v)
            .toString();
    }


    return Number(
        v.toFixed(2)
    ).toString();

}


function draw(){

    const w =
        W();

    const h =
        H();


    ctx.clearRect(
        0,
        0,
        w,
        h
    );


    ctx.fillStyle =
        "#fcfcfe";


    ctx.fillRect(
        0,
        0,
        w,
        h
    );


    /* grid */

    const xs =
        niceStep(
            xmax-xmin
        );


    const ys =
        niceStep(
            ymax-ymin
        );


    ctx.lineWidth=1;

    ctx.strokeStyle =
        document.getElementById("gridToggle")?.checked
        ? "#ececf1"
        : "transparent";

    ctx.fillStyle =
        "#9a9ea8";

    ctx.font =
        "11px system-ui";


    for(
        let x =
            Math.ceil(
                xmin/xs
            )*xs;
        x<=xmax;
        x+=xs
    ){

        const px =
            sx(x);


        ctx.beginPath();

        ctx.moveTo(
            px,
            0
        );

        ctx.lineTo(
            px,
            h
        );

        ctx.stroke();


        if(
            Math.abs(x)>1e-9
        ){

            ctx.fillText(
                fmt(x),
                px+4,
                h-7
            );

        }

    }


    for(
        let y =
            Math.ceil(
                ymin/ys
            )*ys;
        y<=ymax;
        y+=ys
    ){

        const py =
            sy(y);


        ctx.beginPath();

        ctx.moveTo(
            0,
            py
        );

        ctx.lineTo(
            w,
            py
        );

        ctx.stroke();


        if(
            Math.abs(y)>1e-9
        ){

            ctx.fillText(
                fmt(y),
                6,
                py-4
            );

        }

    }


    /* axes */

    ctx.strokeStyle =
        document.getElementById("axisToggle")?.checked
        ? "#c8cad2"
        : "transparent";

    ctx.lineWidth =
        1.4;


    if(
        xmin<=0 &&
        xmax>=0
    ){

        const px =
            sx(0);


        ctx.beginPath();

        ctx.moveTo(
            px,
            0
        );

        ctx.lineTo(
            px,
            h
        );

        ctx.stroke();

    }


    if(
        ymin<=0 &&
        ymax>=0
    ){

        const py =
            sy(0);


        ctx.beginPath();

        ctx.moveTo(
            0,
            py
        );

        ctx.lineTo(
            w,
            py
        );

        ctx.stroke();

    }


    /* layers */

    layers.forEach(layer=>{

        if(
            !layer.visible
        ){
            return;
        }


        const points =
            transformedPoints(
                layer
            );


        if(
            points.length<2
        ){
            return;
        }


        ctx.save();


        ctx.strokeStyle =
            layer.color;


        ctx.lineWidth =
            layer.id===
            selectedLayerId
            ? 3.5
            : 2.4;


        ctx.lineJoin =
            "round";

        ctx.lineCap =
            "round";


        ctx.beginPath();

        let hasStarted=false;
        let previousPoint=null;
        const stepLike=/frac\s*\(|\[[^\]]+\]/i.test(layer.expression||"");
        const jumpThreshold=stepLike ? 0.45 : Math.max(0.8,(ymax-ymin)*0.22);

        points.forEach(p=>{
            const px=sx(p.x);
            const py=sy(p.y);
            if(px<-100 || px>w+100 || py<-100 || py>h+100){
                previousPoint=null;
                hasStarted=false;
                return;
            }
            const discontinuity=previousPoint && Math.abs(p.y-previousPoint.y)>jumpThreshold;
            if(!hasStarted || discontinuity){
                ctx.moveTo(px,py);
                hasStarted=true;
            }else{
                ctx.lineTo(px,py);
            }
            previousPoint=p;
        });


        ctx.stroke();


        ctx.restore();

    });


    /* =====================================================
       재생 위치
    ===================================================== */

    if(
        playing &&
        playbackStart
    ){

        const elapsed =
            (
                performance.now() -
                playbackStart
            )/1000;


        const progress =
            Math.max(
                0,
                Math.min(
                    1,
                    elapsed/
                    playbackDuration
                )
            );


        layers.forEach(layer=>{

            if(
                !layer.visible ||
                layer.points.length<2
            ){
                return;
            }


            const points =
                transformedPoints(
                    layer
                );


            const index =
                Math.min(
                    points.length-1,
                    Math.floor(
                        progress *
                        (
                            points.length-1
                        )
                    )
                );


            const p =
                points[index];


            if(!p){
                return;
            }


            const px =
                sx(p.x);

            const py =
                sy(p.y);


            ctx.save();


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                12,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                layer.color;

            ctx.globalAlpha=.18;

            ctx.fill();

            ctx.globalAlpha=1;


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                6,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                "#ffffff";

            ctx.fill();


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                4,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                layer.color;

            ctx.fill();


            ctx.restore();

        });

    }


    /* =====================================================
       Edit 선택 박스
    ===================================================== */

    if(
        mode==="edit"
    ){

        const selected =
            selectedLayer();


        if(
            selected &&
            selected.visible &&
            selected.points.length>=2
        ){

            const data =
                getEditData(
                    selected
                );


            if(data){

                ctx.save();


                ctx.strokeStyle =
                    "#b7a9ff";

                ctx.lineWidth=1.5;

                ctx.setLineDash([
                    6,
                    5
                ]);


                ctx.strokeRect(
                    data.minX-5,
                    data.minY-5,
                    data.maxX-data.minX+10,
                    data.maxY-data.minY+10
                );


                ctx.setLineDash([]);


                /*
                   회전 연결선
                */

                ctx.beginPath();

                ctx.moveTo(
                    (
                        data.minX+
                        data.maxX
                    )/2,
                    data.minY-5
                );

                ctx.lineTo(
                    (
                        data.minX+
                        data.maxX
                    )/2,
                    data.minY-36
                );

                ctx.stroke();


                const handles =
                    getEditHandles(
                        selected
                    );


                handles.corners.forEach(
                    h=>{

                        ctx.beginPath();

                        ctx.arc(
                            h.x,
                            h.y,
                            h.type==="rotate"
                            ? 7
                            : 6,
                            0,
                            Math.PI*2
                        );

                        ctx.fillStyle =
                            h.type==="rotate"
                            ? "#7a5af8"
                            : "#ffffff";

                        ctx.fill();

                        ctx.strokeStyle =
                            "#9c8bf0";

                        ctx.stroke();

                    }
                );


                ctx.restore();

            }

        }

    }


    /* =====================================================
       분석
    ===================================================== */

    const l =
        selectedLayer();


    if(
        l &&
        l.points.length
    ){

        const points =
            transformedPoints(
                l
            );


        const ys =
            points
            .map(
                p=>p.y
            )
            .filter(
                Number.isFinite
            );


        if(ys.length){

            const min =
                Math.min(
                    ...ys
                );


            const max =
                Math.max(
                    ...ys
                );


            const avg =
                ys.reduce(
                    (a,b)=>a+b,
                    0
                ) /
                ys.length;


            document.getElementById(
                "domain"
            ).textContent =
                fmt(xmin) +
                " ≤ x ≤ " +
                fmt(xmax);


            document.getElementById(
                "minY"
            ).textContent =
                fmt(min);


            document.getElementById(
                "maxY"
            ).textContent =
                fmt(max);


            document.getElementById(
                "avgY"
            ).textContent =
                fmt(avg);

        }

    }

}


/* =========================================================
   음계
========================================================= */

const scales={

    major:[
        0,2,4,5,7,9,11,
        12,14,16,17,19,21,23,24
    ],

    minor:[
        0,2,3,5,7,8,10,
        12,14,15,17,19,20,22,24
    ],

    pentatonic:[
        0,2,4,7,9,
        12,14,16,19,21,24
    ],

    chromatic:[
        0,1,2,3,4,5,
        6,7,8,9,10,11,
        12,13,14,15,16,17,
        18,19,20,21,22,23,24
    ]

};


/* =========================================================
   스타일
========================================================= */

const styles={

    pop:{
        waveform:"triangle",
        attack:.025,
        release:.15,
        baseGain:1,
        subGain:.02
    },

    kpop:{
        waveform:"sawtooth",
        attack:.012,
        release:.10,
        baseGain:.78,
        subGain:.04
    },

    jpop:{
        waveform:"triangle",
        attack:.018,
        release:.12,
        baseGain:.9,
        subGain:.03
    },

    citypop:{
        waveform:"triangle",
        attack:.035,
        release:.18,
        baseGain:.85,
        subGain:.04
    },

    rnb:{
        waveform:"sine",
        attack:.04,
        release:.22,
        baseGain:.9,
        subGain:.06
    },

    edm:{
        waveform:"square",
        attack:.008,
        release:.07,
        baseGain:.55,
        subGain:.12
    },

    house:{
        waveform:"sawtooth",
        attack:.012,
        release:.11,
        baseGain:.62,
        subGain:.12
    },

    techno:{
        waveform:"square",
        attack:.006,
        release:.08,
        baseGain:.58,
        subGain:.13
    },

    trance:{
        waveform:"sawtooth",
        attack:.02,
        release:.15,
        baseGain:.68,
        subGain:.08
    },

    futurebass:{
        waveform:"sawtooth",
        attack:.03,
        release:.24,
        baseGain:.72,
        subGain:.12
    },

    dnb:{
        waveform:"square",
        attack:.006,
        release:.07,
        baseGain:.60,
        subGain:.15
    },

    synthwave:{
        waveform:"sawtooth",
        attack:.035,
        release:.20,
        baseGain:.72,
        subGain:.10
    },

    hiphop:{
        waveform:"triangle",
        attack:.02,
        release:.13,
        baseGain:.83,
        subGain:.07
    },

    trap:{
        waveform:"sawtooth",
        attack:.008,
        release:.11,
        baseGain:.68,
        subGain:.13
    },

    boombap:{
        waveform:"triangle",
        attack:.018,
        release:.16,
        baseGain:.78,
        subGain:.07
    },

    phonk:{
        waveform:"sawtooth",
        attack:.006,
        release:.13,
        baseGain:.72,
        subGain:.18
    },

    funk:{
        waveform:"square",
        attack:.009,
        release:.09,
        baseGain:.82,
        subGain:.06
    },

    rock:{
        waveform:"sawtooth",
        attack:.014,
        release:.12,
        baseGain:.72,
        subGain:.10
    },

    jazz:{
        waveform:"triangle",
        attack:.045,
        release:.24,
        baseGain:.78,
        subGain:.04
    },

    blues:{
        waveform:"sine",
        attack:.04,
        release:.23,
        baseGain:.80,
        subGain:.05
    },

    classic:{
        waveform:"sine",
        attack:.08,
        release:.42,
        baseGain:.72,
        subGain:.025
    },

    ambient:{
        waveform:"sine",
        attack:.22,
        release:.55,
        baseGain:.52,
        subGain:.04
    },

    cinematic:{
        waveform:"triangle",
        attack:.12,
        release:.48,
        baseGain:.72,
        subGain:.10
    },

    epic:{
        waveform:"sawtooth",
        attack:.16,
        release:.62,
        baseGain:.58,
        subGain:.16
    },

    piano:{
        waveform:"triangle",
        attack:.008,
        release:.38,
        baseGain:.82,
        subGain:.025
    },

    lofi:{
        waveform:"sine",
        attack:.055,
        release:.22,
        baseGain:.62,
        subGain:.07
    }

};


/* =========================================================
   y → MIDI
========================================================= */

function graphMidi(
    y,
    lo,
    hi,
    scale
){

    if(
        !Number.isFinite(y) ||
        !Number.isFinite(lo) ||
        !Number.isFinite(hi) ||
        hi<=lo
    ){
        return 60;
    }


    const norm =
        Math.max(
            0,
            Math.min(
                1,
                (y-lo)/(hi-lo)
            )
        );


    const index =
        Math.round(
            norm*
            (
                scale.length-1
            )
        );


    return 48 +
        scale[
            Math.max(
                0,
                Math.min(
                    scale.length-1,
                    index
                )
            )
        ];

}


function midiFreq(m){

    return 440 *
        Math.pow(
            2,
            (
                m-69
            )/12
        );

}


/* =========================================================
   그래프 음 데이터
========================================================= */

function prepareLayerAudio(layer){

    const points =
        transformedPoints(
            layer
        );


    if(
        points.length<2
    ){
        return null;
    }


    const values =
        points
        .map(
            p=>p.y
        )
        .filter(
            Number.isFinite
        );


    if(
        values.length<2
    ){
        return null;
    }


    return {

        points:points,

        lo:
            Math.min(
                ...values
            ),

        hi:
            Math.max(
                ...values
            )

    };

}


/* =========================================================
   라이브 음성 생성
========================================================= */

function createLiveVoice(
    layer,
    data,
    style,
    start
){

    const osc =
        audioCtx.createOscillator();


    const gain =
        audioCtx.createGain();


    osc.type =
        style.waveform;


    gain.gain.setValueAtTime(
        0,
        start
    );


    gain.gain.linearRampToValueAtTime(
        layer.volume *
        style.baseGain,
        start+
        style.attack
    );


    osc.connect(gain);


    gain.connect(
        audioCtx.destination
    );


    osc.start(start);


    let subOsc=null;

    let subGain=null;


    if(
        style.subGain>0
    ){

        subOsc =
            audioCtx
            .createOscillator();


        subGain =
            audioCtx
            .createGain();


        subOsc.type =
            style.waveform;


        subGain.gain.setValueAtTime(
            0,
            start
        );


        subGain.gain.linearRampToValueAtTime(
            layer.volume *
            style.subGain,
            start+
            style.attack
        );


        subOsc.connect(
            subGain
        );


        subGain.connect(
            audioCtx.destination
        );


        subOsc.start(start);

    }


    return {

        layer:layer,

        data:data,

        osc:osc,

        gain:gain,

        subOsc:subOsc,

        subGain:subGain,

        lastFreq:0

    };

}


/* =========================================================
   함수별 음악 트랙 미리보기
========================================================= */
function renderArrangement(progressOverride){
    const host=document.getElementById("arrangementTrackList");
    if(!host) return;
    const visible=layers.filter(layer=>layer.visible && Array.isArray(layer.points) && layer.points.length>1);
    if(!visible.length){
        host.innerHTML='<div class="arrangementEmpty">표시 중인 그래프가 없습니다. 왼쪽에서 함수를 추가하거나 숨김을 해제하세요.</div>';
        return;
    }
    const progress=typeof progressOverride==="number" ? Math.max(0,Math.min(1,progressOverride)) : (playing && playbackDuration ? Math.max(0,Math.min(1,((performance.now()-playbackStart)/1000)/playbackDuration)) : 0);
    host.innerHTML=visible.map((layer,index)=>{
        const pts=layer.points;
        let lo=Infinity,hi=-Infinity;
        pts.forEach(p=>{if(Number.isFinite(p.y)){lo=Math.min(lo,p.y);hi=Math.max(hi,p.y);}});
        if(!Number.isFinite(lo)||!Number.isFinite(hi)){lo=-1;hi=1;}
        const span=Math.max(0.0001,hi-lo);
        const d=pts.map((p,i)=>{
            const x=pts.length<2?0:(i/(pts.length-1))*1000;
            const y=35-((p.y-lo)/span)*27;
            return (i?'L':'M')+x.toFixed(2)+' '+y.toFixed(2);
        }).join(' ');
        const color=layer.color||['#8b6cf6','#22b8a7','#f5b942','#f27d54','#5b8def'][index%5];
        const label=(layer.name||('Graph '+(index+1))).replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
        const type=layer.type==='sketch'?'손그림':'함수';
        return `<div class="arrangementTrack"><div class="arrangementTrackName" style="color:${color}">${label}<small>${type} · ${pts.length} points</small></div><div class="arrangementLane"><svg viewBox="0 0 1000 40" preserveAspectRatio="none" aria-hidden="true"><path d="${d}" fill="none" stroke="${color}" stroke-opacity=".16" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/><path d="${d}" fill="none" stroke="${color}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/></svg><div class="arrangementPlayhead" style="left:calc(${(progress*100).toFixed(3)}% - 1px)"></div></div></div>`;
    }).join('');
    const status=document.getElementById('arrangementStatus');
    if(status) status.textContent=playing?'PLAYING':'READY';
    const end=document.getElementById('arrangementEnd');
    if(end){const sec=Number(document.getElementById('duration')?.value||30);end.textContent=sec>=60?Math.floor(sec/60)+':'+String(sec%60).padStart(2,'0')+' end':sec+'s end';}
}

/* =========================================================
   자동 반주: 코드 패드 + 베이스 + 드럼
========================================================= */
function scheduleBacking(context, destination, duration, styleKey, bpm, scaleName){
    const mode=document.getElementById("arrangementMode")?.value||"all";
    if(mode!=="backing") return [];
    const nodes=[];
    const beat=60/Math.max(50,Math.min(220,Number(bpm)||145));
    const isEpic=styleKey==="epic"||styleKey==="cinematic";
    const isPiano=styleKey==="piano"||styleKey==="classic";
    const roots=scaleName==="minor"?[57,60,62,57]:[60,65,67,60];
    const chordSteps=scaleName==="minor"?[[0,3,7],[0,3,7],[0,4,7],[0,3,7]]:[[0,4,7],[0,5,9],[0,4,7],[0,5,9]];
    const chordEvery=beat*(isEpic?2:4);
    for(let t=0,bar=0;t<duration;t+=chordEvery,bar++){
        const root=roots[bar%roots.length];
        const tones=chordSteps[bar%chordSteps.length];
        tones.forEach((step,j)=>{
            const osc=context.createOscillator();
            const gain=context.createGain();
            osc.type=isEpic?"sawtooth":(isPiano?"triangle":"sine");
            osc.frequency.setValueAtTime(midiFreq(root+step+(isEpic?12:0)),t);
            gain.gain.setValueAtTime(0,t);
            gain.gain.linearRampToValueAtTime(isEpic?.035:.022,t+Math.min(.18,beat*.35));
            gain.gain.setValueAtTime(isEpic?.035:.022,Math.min(duration,t+chordEvery*.72));
            gain.gain.linearRampToValueAtTime(0,Math.min(duration,t+chordEvery*.95));
            osc.connect(gain);gain.connect(destination);osc.start(t);osc.stop(Math.min(duration,t+chordEvery));nodes.push(osc);
        });
        // Low bass pulse on each bar
        const bass=context.createOscillator(); const bg=context.createGain();
        bass.type="sine"; bass.frequency.setValueAtTime(midiFreq(root-12),t);
        bg.gain.setValueAtTime(0,t); bg.gain.linearRampToValueAtTime(isEpic?.12:.075,t+.025); bg.gain.exponentialRampToValueAtTime(.001,Math.min(duration,t+beat*1.6));
        bass.connect(bg);bg.connect(destination);bass.start(t);bass.stop(Math.min(duration,t+beat*1.65));nodes.push(bass);
    }
    // Simple percussive beat; use a short noise burst for kick/snare-like attacks.
    if(!isPiano){
        const step=beat/2;
        for(let t=0,i=0;t<duration;t+=step,i++){
            const osc=context.createOscillator(); const gain=context.createGain();
            const kick=(i%4===0); osc.type="sine"; osc.frequency.setValueAtTime(kick?105:190,t); osc.frequency.exponentialRampToValueAtTime(kick?42:95,Math.min(duration,t+.11));
            gain.gain.setValueAtTime(kick?.18:.055,t); gain.gain.exponentialRampToValueAtTime(.001,Math.min(duration,t+.13));
            osc.connect(gain);gain.connect(destination);osc.start(t);osc.stop(Math.min(duration,t+.14));nodes.push(osc);
        }
    }
    return nodes;
}

/* =========================================================
   음악 재생
========================================================= */

async function playMusic(){

    stopMusic();


    const visibleLayers =
        layers.filter(
            l =>
                l.visible &&
                l.points.length>=2
        );


    if(
        !visibleLayers.length
    ){

        msg.textContent =
            "음악으로 변환할 표시된 그래프가 없습니다.";

        return;

    }


    if(!audioCtx){

        audioCtx =
            new(
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }


    if(
        audioCtx.state==="suspended"
    ){

        await audioCtx.resume();

    }


    const duration =
        Number(
            document.getElementById(
                "duration"
            ).value
        );


    const scale =
        scales[
            document.getElementById(
                "scale"
            ).value
        ];


    const style =
        styles[
            document.getElementById(
                "style"
            ).value
        ];


    playbackDuration =
        duration;


    playbackStart =
        performance.now();


    playing=true;
    renderArrangement(0);


    const start =
        audioCtx.currentTime+
        .05;


    audioVoices=[];
    backingNodes=[];
    const arrangementMode=document.getElementById("arrangementMode")?.value||"all";
    const instrumentStyles=["piano","cinematic","epic","synthwave","classic","edm","ambient"];


    visibleLayers.forEach(
        layer=>{

            const data =
                prepareLayerAudio(
                    layer
                );


            if(!data){
                return;
            }


            const layerStyle = arrangementMode==="all"
                ? (styles[instrumentStyles[visibleLayers.indexOf(layer)%instrumentStyles.length]]||style)
                : style;
            const voice =
                createLiveVoice(
                    layer,
                    data,
                    layerStyle,
                    start
                );


            audioVoices.push(
                voice
            );

        }
    );

    backingNodes=scheduleBacking(
        audioCtx,
        audioCtx.destination,
        duration,
        document.getElementById("style").value,
        document.getElementById("bpm")?.value||145,
        document.getElementById("scale").value
    );

    if(
        !audioVoices.length
    ){

        stopMusic();

        msg.textContent =
            "재생할 수 있는 그래프가 없습니다.";

        return;

    }


    document.getElementById(
        "now"
    ).textContent =
        audioVoices.length +
        "개 그래프 레이어 재생 중 · " +
        (document.getElementById("arrangementMode")?.value==="backing" ? "자동 코드·베이스·리듬 포함" : "레이어별 악기 편성");


    raf =
        requestAnimationFrame(
            musicTick
        );

}


/* =========================================================
   음악 Tick
========================================================= */

function musicTick(){

    if(!playing){
        return;
    }


    const elapsed =
        (
            performance.now() -
            playbackStart
        )/1000;


    const progress =
        Math.max(
            0,
            Math.min(
                1,
                elapsed/
                playbackDuration
            )
        );
    const bpm=Math.max(50,Math.min(220,Number(document.getElementById("bpm")?.value)||145));
    const beatStep=30/bpm; // 8분음표마다 음높이를 갱신합니다.
    const musicalElapsed=Math.floor(elapsed/beatStep)*beatStep;
    const musicalProgress=Math.max(0,Math.min(1,musicalElapsed/playbackDuration));

    renderArrangement(progress);


    audioVoices.forEach(
        voice=>{

            const points =
                voice.data.points;


            const index =
                Math.min(
                    points.length-1,
                    Math.floor(
                        musicalProgress*
                        (
                            points.length-1
                        )
                    )
                );


            const p =
                points[index];


            if(!p){
                return;
            }


            const scale =
                scales[
                    document.getElementById(
                        "scale"
                    ).value
                ];


            const midi =
                graphMidi(
                    p.y,
                    voice.data.lo,
                    voice.data.hi,
                    scale
                );


            const freq =
                Math.max(
                    45,
                    Math.min(
                        1800,
                        midiFreq(midi)
                    )
                );


            const now =
                audioCtx.currentTime;


            if(
                !voice.lastFreq
            ){

                voice.osc.frequency
                    .setValueAtTime(
                        freq,
                        now
                    );


                if(
                    voice.subOsc
                ){

                    voice.subOsc
                        .frequency
                        .setValueAtTime(
                            freq/2,
                            now
                        );

                }

            }else{

                voice.osc.frequency
                    .cancelScheduledValues(
                        now
                    );


                voice.osc.frequency
                    .linearRampToValueAtTime(
                        freq,
                        now+.055
                    );


                if(
                    voice.subOsc
                ){

                    voice.subOsc.frequency
                        .cancelScheduledValues(
                            now
                        );


                    voice.subOsc.frequency
                        .linearRampToValueAtTime(
                            freq/2,
                            now+.055
                        );

                }

            }


            voice.lastFreq =
                freq;

        }
    );


    document.getElementById(
        "bar"
    ).style.width =
        (
            progress*100
        )+"%";


    document.getElementById(
        "now"
    ).textContent =
        "재생 중 · " +
        Math.round(
            progress*100
        ) +
        "% · " +
        audioVoices.length +
        "개 그래프 동시 재생";


    draw();


    if(
        progress<1
    ){

        raf =
            requestAnimationFrame(
                musicTick
            );

    }else{

        finishMusic();

    }

}


/* =========================================================
   음악 종료
========================================================= */

function finishMusic(){

    playing=false;


    const now =
        audioCtx
        ? audioCtx.currentTime
        : 0;


    audioVoices.forEach(
        voice=>{

            try{

                voice.gain.gain
                    .cancelScheduledValues(
                        now
                    );


                voice.gain.gain
                    .linearRampToValueAtTime(
                        0,
                        now+.12
                    );


                voice.osc.stop(
                    now+.2
                );


                if(
                    voice.subGain &&
                    voice.subOsc
                ){

                    voice.subGain.gain
                        .cancelScheduledValues(
                            now
                        );


                    voice.subGain.gain
                        .linearRampToValueAtTime(
                            0,
                            now+.12
                        );


                    voice.subOsc.stop(
                        now+.2
                    );

                }

            }catch(e){}

        }
    );


    audioVoices=[];

    playbackStart=0;


    document.getElementById(
        "bar"
    ).style.width="100%";


    document.getElementById(
        "now"
    ).textContent =
        "재생 완료";


    draw();

}


/* =========================================================
   정지
========================================================= */

function stopMusic(){

    playing=false;


    if(raf){

        cancelAnimationFrame(
            raf
        );

    }


    raf=null;


    if(audioCtx){

        const now =
            audioCtx.currentTime;


        audioVoices.forEach(
            voice=>{

                try{

                    voice.gain.gain
                        .cancelScheduledValues(
                            now
                        );


                    voice.gain.gain
                        .setTargetAtTime(
                            0,
                            now,
                            .03
                        );


                    voice.osc.stop(
                        now+.1
                    );


                    if(
                        voice.subGain &&
                        voice.subOsc
                    ){

                        voice.subGain.gain
                            .cancelScheduledValues(
                                now
                            );


                        voice.subGain.gain
                            .setTargetAtTime(
                                0,
                                now,
                                .03
                            );


                        voice.subOsc.stop(
                            now+.1
                        );

                    }

                }catch(e){}

            }
        );

    }


    backingNodes.forEach(node=>{try{node.stop(audioCtx.currentTime+.03);}catch(e){}});
    backingNodes=[];
    audioVoices=[];

    playbackStart=0;


    renderArrangement(0);

    document.getElementById(
        "bar"
    ).style.width="0%";


    document.getElementById(
        "now"
    ).textContent =
        "정지됨";


    draw();

}


document
.getElementById("play")
.addEventListener(
    "click",
    playMusic
);


document
.getElementById("stop")
.addEventListener(
    "click",
    stopMusic
);


/* =========================================================
   WAV 파일 생성
========================================================= */

function safeFilename(name){

    return (
        name
        .replace(
            /[<>:"/\\|?*]+/g,
            "_"
        )
        .trim() ||
        "Cosmos Song"
    );

}


function createWavBlob(
    audioBuffer
){

    const numChannels =
        1;

    const sampleRate =
        audioBuffer.sampleRate;

    const samples =
        audioBuffer.getChannelData(0);


    const bytesPerSample=2;

    const dataSize =
        samples.length *
        bytesPerSample;


    const buffer =
        new ArrayBuffer(
            44+dataSize
        );


    const view =
        new DataView(buffer);


    function writeString(
        offset,
        string
    ){

        for(
            let i=0;
            i<string.length;
            i++
        ){

            view.setUint8(
                offset+i,
                string.charCodeAt(i)
            );

        }

    }


    writeString(
        0,
        "RIFF"
    );


    view.setUint32(
        4,
        36+dataSize,
        true
    );


    writeString(
        8,
        "WAVE"
    );


    writeString(
        12,
        "fmt "
    );


    view.setUint32(
        16,
        16,
        true
    );


    view.setUint16(
        20,
        1,
        true
    );


    view.setUint16(
        22,
        numChannels,
        true
    );


    view.setUint32(
        24,
        sampleRate,
        true
    );


    view.setUint32(
        28,
        sampleRate *
        numChannels *
        bytesPerSample,
        true
    );


    view.setUint16(
        32,
        numChannels *
        bytesPerSample,
        true
    );


    view.setUint16(
        34,
        16,
        true
    );


    writeString(
        36,
        "data"
    );


    view.setUint32(
        40,
        dataSize,
        true
    );


    let offset=44;


    for(
        let i=0;
        i<samples.length;
        i++
    ){

        const s =
            Math.max(
                -1,
                Math.min(
                    1,
                    samples[i]
                )
            );


        const value =
            s<0
            ? s*0x8000
            : s*0x7fff;


        view.setInt16(
            offset,
            value,
            true
        );


        offset+=2;

    }


    return new Blob(
        [buffer],
        {
            type:"audio/wav"
        }
    );

}


/* =========================================================
   WAV 오프라인 렌더링
========================================================= */

async function downloadWav(){

    const visibleLayers =
        layers.filter(
            l =>
                l.visible &&
                l.points.length>=2
        );


    if(
        !visibleLayers.length
    ){

        msg.textContent =
            "저장할 수 있는 표시된 그래프가 없습니다.";

        return;

    }


    stopMusic();


    const duration =
        Number(
            document.getElementById(
                "duration"
            ).value
        );


    const scale =
        scales[
            document.getElementById(
                "scale"
            ).value
        ];


    const style =
        styles[
            document.getElementById(
                "style"
            ).value
        ];


    const sampleRate =
        44100;


    const totalSamples =
        Math.floor(
            duration*
            sampleRate
        );


    msg.textContent =
        "WAV 파일을 만드는 중입니다. 잠시만 기다려 주세요...";


    document.getElementById(
        "now"
    ).textContent =
        "오디오 렌더링 중 · " +
        duration +
        "초";


    const offline =
        new OfflineAudioContext(
            1,
            totalSamples,
            sampleRate
        );


    /*
       마스터 컴프레서로 레이어가
       동시에 울릴 때 지나치게 튀는 것을 줄임
    */

    const compressor =
        offline.createDynamicsCompressor();


    compressor.threshold.value =
        -18;

    compressor.knee.value =
        12;

    compressor.ratio.value =
        5;

    compressor.attack.value =
        .003;

    compressor.release.value =
        .15;


    compressor.connect(
        offline.destination
    );

    // WAV에도 라이브 재생과 동일한 자동 코드·베이스·드럼 편성을 렌더링합니다.
    scheduleBacking(
        offline,
        compressor,
        duration,
        document.getElementById("style").value,
        document.getElementById("bpm")?.value||145,
        document.getElementById("scale").value
    );

    const arrangementMode=document.getElementById("arrangementMode")?.value||"all";
    const instrumentStyles=["piano","cinematic","epic","synthwave","classic","edm","ambient"];

    visibleLayers.forEach(
        layer=>{

            const data =
                prepareLayerAudio(
                    layer
                );


            if(!data){
                return;
            }


            const osc =
                offline.createOscillator();


            const gain =
                offline.createGain();


            const layerStyle = arrangementMode==="all"
                ? (styles[instrumentStyles[visibleLayers.indexOf(layer)%instrumentStyles.length]]||style)
                : style;
            osc.type =
                layerStyle.waveform;


            const points =
                data.points;


            const initialMidi =
                graphMidi(
                    points[0].y,
                    data.lo,
                    data.hi,
                    scale
                );


            const initialFreq =
                midiFreq(
                    initialMidi
                );


            osc.frequency.setValueAtTime(
                initialFreq,
                0
            );


            const bpm=Math.max(50,Math.min(220,Number(document.getElementById("bpm")?.value)||145));
            const beatStep=30/bpm;
            for(let t=beatStep;t<duration;t+=beatStep){
                const progress=Math.min(1,t/duration);
                const pointIndex=Math.min(points.length-1,Math.floor(progress*(points.length-1)));
                const midi=graphMidi(points[pointIndex].y,data.lo,data.hi,scale);


                const freq =
                    Math.max(
                        45,
                        Math.min(
                            1800,
                            midiFreq(midi)
                        )
                    );


                osc.frequency
                    .linearRampToValueAtTime(
                        freq,
                        t
                    );

            }


            const level =
                layer.volume *
                layerStyle.baseGain;


            gain.gain.setValueAtTime(
                0,
                0
            );


            gain.gain
                .linearRampToValueAtTime(
                    level,
                    Math.min(
                        layerStyle.attack,
                        duration/4
                    )
                );


            gain.gain
                .linearRampToValueAtTime(
                    level,
                    Math.max(
                        layerStyle.attack,
                        duration-.12
                    )
                );


            gain.gain
                .linearRampToValueAtTime(
                    0,
                    duration
                );


            osc.connect(gain);

            gain.connect(compressor);

            osc.start(0);

            osc.stop(duration);


            /*
               서브 옥타브
            */

            if(layerStyle.subGain>0){

                const sub =
                    offline
                    .createOscillator();


                const subGain =
                    offline
                    .createGain();


                sub.type =
                    layerStyle.waveform;


                sub.frequency.setValueAtTime(
                    initialFreq/2,
                    0
                );


                for(
                    let i=1;
                    i<points.length;
                    i++
                ){

                    const progress =
                        i/
                        (
                            points.length-1
                        );


                    const t =
                        progress*
                        duration;


                    const midi =
                        graphMidi(
                            points[i].y,
                            data.lo,
                            data.hi,
                            scale
                        );


                    const freq =
                        Math.max(
                            30,
                            Math.min(
                                900,
                                midiFreq(midi)/2
                            )
                        );


                    sub.frequency
                        .linearRampToValueAtTime(
                            freq,
                            t
                        );

                }


                subGain.gain.setValueAtTime(
                    0,
                    0
                );


                subGain.gain
                    .linearRampToValueAtTime(
                        layer.volume *
                        layerStyle.subGain,
                        Math.min(
                            layerStyle.attack,
                            duration/4
                        )
                    );


                subGain.gain
                    .linearRampToValueAtTime(
                        layer.volume *
                        layerStyle.subGain,
                        Math.max(
                            layerStyle.attack,
                            duration-.12
                        )
                    );


                subGain.gain
                    .linearRampToValueAtTime(
                        0,
                        duration
                    );


                sub.connect(
                    subGain
                );


                subGain.connect(
                    compressor
                );


                sub.start(0);

                sub.stop(duration);

            }

        }
    );


    try{

        const rendered =
            await offline.startRendering();


        const blob =
            createWavBlob(
                rendered
            );


        const url =
            URL.createObjectURL(
                blob
            );


        const a =
            document.createElement(
                "a"
            );


        const filename =
            safeFilename(
                document.getElementById(
                    "songName"
                ).value
            );


        a.href=url;

        a.download =
            filename +
            ".wav";


        document.body.appendChild(
            a
        );


        a.click();

        a.remove();


        setTimeout(
            ()=>{
                URL.revokeObjectURL(
                    url
                );
            },
            5000
        );


        msg.textContent =
            "WAV 파일을 저장했습니다.";


        document.getElementById(
            "now"
        ).textContent =
            "WAV 저장 완료";

    }catch(error){

        console.error(error);

        msg.textContent =
            "WAV 생성 중 오류가 발생했습니다.";

    }

}


document
.getElementById(
    "downloadWav"
)
.addEventListener(
    "click",
    downloadWav
);


/* =========================================================
   Library
========================================================= */

function createId(
    prefix
){

    return (
        prefix+
        Date.now()+
        "_" +
        Math.random()
        .toString(36)
        .slice(2,8)
    );

}


function defaultLibraries(){

    return [

        {

            id:
                createId(
                    "lib_"
                ),

            name:
                "My Library",

            songs:[]

        }

    ];

}


function loadLibraries(){

    try{

        const raw =
            localStorage.getItem(
                LIBRARY_KEY
            );


        if(!raw){

            return defaultLibraries();

        }


        const parsed =
            JSON.parse(raw);


        if(
            !Array.isArray(parsed) ||
            !parsed.length
        ){

            return defaultLibraries();

        }


        return parsed;

    }catch(e){

        return defaultLibraries();

    }

}


function saveLibraries(){

    try{

        localStorage.setItem(
            LIBRARY_KEY,
            JSON.stringify(
                libraries
            )
        );

    }catch(e){

        msg.textContent =
            "Library 저장 공간을 사용할 수 없습니다.";

    }

}


function currentLibrary(){

    return libraries.find(
        l =>
            l.id===
            currentLibraryId
    ) || null;

}


/* =========================================================
   Library UI
========================================================= */

function renderLibrarySelect(){

    const select =
        document.getElementById(
            "librarySelect"
        );


    select.innerHTML="";


    libraries.forEach(
        lib=>{

            const option =
                document.createElement(
                    "option"
                );

            option.value =
                lib.id;

            option.textContent =
                lib.name;

            if(
                lib.id===
                currentLibraryId
            ){

                option.selected=true;

            }

            select.appendChild(
                option
            );

        }
    );

}


function renderSongList(){

    const box =
        document.getElementById(
            "songList"
        );


    box.innerHTML="";


    const lib =
        currentLibrary();


    if(!lib){

        return;

    }


    document.getElementById(
        "libraryMeta"
    ).textContent =
        lib.songs.length +
        "개 곡";


    if(
        !lib.songs.length
    ){

        const empty =
            document.createElement(
                "div"
            );

        empty.className =
            "notice";

        empty.textContent =
            "아직 저장된 곡이 없습니다. 현재 곡 이름을 입력하고 '곡 저장'을 눌러주세요.";

        box.appendChild(
            empty
        );

        return;

    }


    lib.songs
        .slice()
        .reverse()
        .forEach(
            song=>{

                const item =
                    document.createElement(
                        "div"
                    );

                item.className =
                    "songItem";


                const info =
                    document.createElement(
                        "div"
                    );

                info.className =
                    "songInfo";


                const title =
                    document.createElement(
                        "div"
                    );

                title.className =
                    "songTitle";

                title.textContent =
                    song.name;


                const date =
                    document.createElement(
                        "div"
                    );

                date.className =
                    "songDate";

                date.textContent =
                    new Date(
                        song.savedAt
                    )
                    .toLocaleString(
                        "ko-KR"
                    );


                info.appendChild(
                    title
                );

                info.appendChild(
                    date
                );


                const actions =
                    document.createElement(
                        "div"
                    );

                actions.className =
                    "songActions";


                const loadBtn =
                    document.createElement(
                        "button"
                    );

                loadBtn.textContent =
                    "불러오기";


                const deleteBtn =
                    document.createElement(
                        "button"
                    );

                deleteBtn.textContent =
                    "삭제";

                deleteBtn.className =
                    "danger";


                actions.appendChild(
                    loadBtn
                );

                actions.appendChild(
                    deleteBtn
                );


                item.appendChild(
                    info
                );

                item.appendChild(
                    actions
                );


                loadBtn.addEventListener(
                    "click",
                    e=>{

                        e.stopPropagation();

                        loadSong(
                            song.id
                        );

                    }
                );


                deleteBtn.addEventListener(
                    "click",
                    e=>{

                        e.stopPropagation();

                        deleteSong(
                            song.id
                        );

                    }
                );


                box.appendChild(
                    item
                );

            }
        );

}


/* =========================================================
   곡 직렬화
========================================================= */

function serializeLayers(){

    return layers.map(
        layer=>({

            id:
                layer.id,

            name:
                layer.name,

            type:
                layer.type,

            expression:
                layer.expression,

            visible:
                layer.visible,

            volume:
                layer.volume,

            color:
                layer.color,

            /*
               함수는 expression으로
               다시 생성할 수 있으므로 points를
               저장하지 않아도 됨.
            */

            points:
                layer.type==="sketch"
                ? layer.points
                : [],

            transform:{
                tx:
                    layer.transform.tx,

                ty:
                    layer.transform.ty,

                scale:
                    layer.transform.scale,

                rotation:
                    layer.transform.rotation
            }

        })
    );

}


/* =========================================================
   곡 불러오기용 레이어 복원
========================================================= */

function restoreLayers(
    savedLayers
){

    layers =
        savedLayers.map(
            layer=>({

                id:
                    layer.id,

                name:
                    layer.name ||
                    "Graph " +
                    layer.id,

                type:
                    layer.type ||
                    "function",

                expression:
                    layer.expression ||
                    "",

                visible:
                    layer.visible !==
                    false,

                volume:
                    Number.isFinite(
                        layer.volume
                    )
                    ? layer.volume
                    : .4,

                color:
                    layer.color ||
                    layerColors[
                        (
                            layer.id-1
                        ) %
                        layerColors.length
                    ],

                points:
                    layer.type==="sketch"
                    ? (
                        layer.points ||
                        []
                    )
                    : [],

                transform:{
                    tx:
                        layer.transform
                        ?.tx || 0,

                    ty:
                        layer.transform
                        ?.ty || 0,

                    scale:
                        layer.transform
                        ?.scale || 1,

                    rotation:
                        layer.transform
                        ?.rotation || 0
                }

            })
        );


    /*
       함수 레이어 points 재생성
    */

    layers.forEach(
        layer=>{

            if(
                layer.type==="function"
            ){

                try{

                    const points =
                        generateFunctionPoints(
                            layer.expression
                        );


                    const center =
                        getCenter(
                            points
                        );


                    points.forEach(
                        p=>{

                            p.cx =
                                center.x;

                            p.cy =
                                center.y;

                        }
                    );


                    layer.points =
                        points;

                }catch(e){

                    layer.points=[];

                }

            }else{

                const center =
                    getCenter(
                        layer.points
                    );


                layer.points =
                    layer.points.map(
                        p=>({

                            x:p.x,

                            y:p.y,

                            cx:
                                p.cx ??
                                center.x,

                            cy:
                                p.cy ??
                                center.y

                        })
                    );

            }

        }
    );


    layerIdCounter =
        Math.max(
            ...layers.map(
                l=>l.id
            ),
            1
        );

}


/* =========================================================
   현재 상태 직렬화
========================================================= */

function buildSongSnapshot(){

    return {

        id:
            currentSongId ||
            createId(
                "song_"
            ),

        name:
            document.getElementById(
                "songName"
            ).value.trim()
            ||
            "Untitled Cosmos",

        savedAt:
            Date.now(),

        duration:
            document.getElementById(
                "duration"
            ).value,

        bpm:
            Number(document.getElementById("bpm")?.value || 145),

        scale:
            document.getElementById(
                "scale"
            ).value,

        style:
            document.getElementById(
                "style"
            ).value,

        view:{

            xmin:xmin,

            xmax:xmax,

            ymin:ymin,

            ymax:ymax

        },

        layers:
            serializeLayers()

    };

}


/* =========================================================
   곡 저장
========================================================= */

function saveSong(){

    const lib =
        currentLibrary();


    if(!lib){

        return;

    }


    const name =
        document.getElementById(
            "songName"
        ).value.trim()
        ||
        "Untitled Cosmos";


    document.getElementById(
        "songName"
    ).value =
        name;


    const snapshot =
        buildSongSnapshot();


    let index =
        lib.songs.findIndex(
            s =>
                s.id===
                currentSongId
        );


    if(index>=0){

        snapshot.id =
            currentSongId;

        lib.songs[index] =
            snapshot;

    }else{

        currentSongId =
            snapshot.id;

        lib.songs.push(
            snapshot
        );

    }


    saveLibraries();

    renderSongList();


    msg.textContent =
        "'" +
        name +
        "' 곡을 '" +
        lib.name +
        "'에 저장했습니다.";

}


document
.getElementById(
    "saveSong"
)
.addEventListener(
    "click",
    saveSong
);


/* =========================================================
   곡 불러오기
========================================================= */

function loadSong(songId){

    const lib =
        currentLibrary();


    if(!lib){
        return;
    }


    const song =
        lib.songs.find(
            s =>
                s.id===
                songId
        );


    if(!song){
        return;
    }


    stopMusic();


    currentSongId =
        song.id;


    document.getElementById(
        "songName"
    ).value =
        song.name;


    document.getElementById(
        "duration"
    ).value =
        song.duration ||
        "30";

    document.getElementById("bpm").value = String(Math.max(50,Math.min(220,Number(song.bpm)||145)));
    syncBpmLabel();

    document.getElementById(
        "scale"
    ).value =
        song.scale ||
        "major";


    document.getElementById(
        "style"
    ).value =
        song.style ||
        "pop";


    if(song.view){

        xmin =
            Number.isFinite(
                song.view.xmin
            )
            ? song.view.xmin
            : -10;

        xmax =
            Number.isFinite(
                song.view.xmax
            )
            ? song.view.xmax
            : 10;

        ymin =
            Number.isFinite(
                song.view.ymin
            )
            ? song.view.ymin
            : -6;

        ymax =
            Number.isFinite(
                song.view.ymax
            )
            ? song.view.ymax
            : 6;

    }


    restoreLayers(
        song.layers
    );


    selectedLayerId =
        layers.length
        ? layers[0].id
        : null;


    expr.value =
        selectedLayer()
        ?.expression || "";
    syncMathEditorFromSource();

    renderLayers();

    draw();


    msg.textContent =
        "'" +
        song.name +
        "' 곡을 불러왔습니다.";

}


/* =========================================================
   곡 삭제
========================================================= */

function deleteSong(songId){

    const lib =
        currentLibrary();


    if(!lib){
        return;
    }


    const song =
        lib.songs.find(
            s =>
                s.id===
                songId
        );


    if(!song){
        return;
    }


    if(
        !confirm(
            "'" +
            song.name +
            "' 곡을 삭제할까요?"
        )
    ){
        return;
    }


    lib.songs =
        lib.songs.filter(
            s =>
                s.id!==
                songId
        );


    if(
        currentSongId===
        songId
    ){

        currentSongId=null;

    }


    saveLibraries();

    renderSongList();


    msg.textContent =
        "곡을 삭제했습니다.";

}


/* =========================================================
   새 곡
========================================================= */

function createFreshWorkspace(){

    stopMusic();


    xmin=-10;

    xmax=10;

    ymin=-6;

    ymax=6;


    layerIdCounter=2;

    selectedLayerId=1;


    layers=[

        {

            id:1,

            name:"Graph 1",

            type:"function",

            expression:"sin(x)",

            visible:true,

            volume:.55,

            color:layerColors[0],

            points:[],

            transform:{
                tx:0,
                ty:0,
                scale:1,
                rotation:0
            }

        },

        {

            id:2,

            name:"Graph 2",

            type:"function",

            expression:"0.5*cos(2*x)",

            visible:true,

            volume:.40,

            color:layerColors[1],

            points:[],

            transform:{
                tx:0,
                ty:0,
                scale:1,
                rotation:0
            }

        }

    ];


    layers.forEach(
        layer=>{

            const points =
                generateFunctionPoints(
                    layer.expression
                );


            const center =
                getCenter(
                    points
                );


            points.forEach(
                p=>{

                    p.cx =
                        center.x;

                    p.cy =
                        center.y;

                }
            );


            layer.points =
                points;

        }
    );


    document.getElementById(
        "songName"
    ).value =
        "Untitled Cosmos";


    document.getElementById(
        "duration"
    ).value =
        "30";

    document.getElementById("bpm").value = "145";
    syncBpmLabel();

    document.getElementById(
        "scale"
    ).value =
        "major";


    document.getElementById(
        "style"
    ).value =
        "pop";


    expr.value =
        "sin(x)";
    syncMathEditorFromSource();

    currentSongId=null;


    renderLayers();

    draw();

}


document
.getElementById(
    "newSong"
)
.addEventListener(
    "click",
    ()=>{

        createFreshWorkspace();

        msg.textContent =
            "새 곡 작업 공간을 만들었습니다.";

    }
);


/* =========================================================
   새 Library
========================================================= */

document
.getElementById(
    "newLibrary"
)
.addEventListener(
    "click",
    ()=>{

        const name =
            prompt(
                "새 Library 이름을 입력하세요."
            );


        if(!name){
            return;
        }


        const library={

            id:
                createId(
                    "lib_"
                ),

            name:
                name.trim(),

            songs:[]

        };


        libraries.push(
            library
        );


        currentLibraryId =
            library.id;


        currentSongId=null;


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "'" +
            library.name +
            "' Library를 만들었습니다.";

    }
);


/* =========================================================
   Library 이름 변경
========================================================= */

document
.getElementById(
    "renameLibrary"
)
.addEventListener(
    "click",
    ()=>{

        const lib =
            currentLibrary();


        if(!lib){
            return;
        }


        const name =
            prompt(
                "새 Library 이름",
                lib.name
            );


        if(!name){
            return;
        }


        lib.name =
            name.trim();


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "Library 이름을 변경했습니다.";

    }
);


/* =========================================================
   Library 삭제
========================================================= */

document
.getElementById(
    "deleteLibrary"
)
.addEventListener(
    "click",
    ()=>{

        if(
            libraries.length<=1
        ){

            msg.textContent =
                "최소 한 개의 Library는 필요합니다.";

            return;

        }


        const lib =
            currentLibrary();


        if(!lib){
            return;
        }


        if(
            !confirm(
                "'" +
                lib.name +
                "' Library와 안의 저장된 곡들을 모두 삭제할까요?"
            )
        ){
            return;
        }


        libraries =
            libraries.filter(
                l =>
                    l.id!==
                    currentLibraryId
            );


        currentLibraryId =
            libraries[0].id;

        currentSongId=null;


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "Library를 삭제했습니다.";

    }
);


/* =========================================================
   Library 변경
========================================================= */

document
.getElementById(
    "librarySelect"
)
.addEventListener(
    "change",
    e=>{

        currentLibraryId =
            e.target.value;

        currentSongId=null;

        renderSongList();


        msg.textContent =
            "'" +
            currentLibrary()
            ?.name +
            "' Library를 선택했습니다.";

    }
);



/* =========================================================
   WORKSPACE UI
========================================================= */

const addMenuToggle =
    document.getElementById("addMenuToggle");

const addMenu =
    document.getElementById("addMenu");

addMenuToggle.addEventListener(
    "click",
    e=>{
        e.stopPropagation();
        addMenu.classList.toggle("open");
    }
);

document.addEventListener(
    "click",
    e=>{
        if(
            !e.target.closest(".addMenuWrap")
        ){
            addMenu.classList.remove("open");
        }
    }
);

document
.querySelectorAll("#addMenu button")
.forEach(
    button=>{
        button.addEventListener(
            "click",
            ()=>{
                addMenu.classList.remove("open");
            }
        );
    }
);


/* ---------- rail ---------- */

function toggleRail(
    id,
    open
){
    document
    .querySelectorAll(".railPanel")
    .forEach(
        panel=>{
            panel.classList.toggle(
                "open",
                panel.id===id
                    ? open
                    : false
            );
        }
    );
}

document
.getElementById("musicRailOpen")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",true)
);

document
.getElementById("toolbarPlayAll")
.addEventListener(
    "click",
    ()=>{
        toggleRail("musicDrawer",true);
        playMusic();
    }
);

document
.getElementById("musicRailButton")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",true)
);

document
.getElementById("musicRailClose")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",false)
);

document
.getElementById("principleRailOpen")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",true)
);

document
.getElementById("principleRailButton")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",true)
);

document
.getElementById("principleRailClose")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",false)
);


/* ---------- secondary save ---------- */

document
.getElementById("saveSongSecondary")
.addEventListener(
    "click",
    ()=>{
        document
        .getElementById("saveSong")
        .click();
    }
);


/* ---------- graph settings ---------- */

const settingsToggle =
    document.getElementById("settingsToggle");

const settingsPanel =
    document.getElementById("settingsPanel");

settingsToggle.addEventListener(
    "click",
    e=>{
        e.stopPropagation();
        settingsPanel.classList.toggle("open");
    }
);

document.addEventListener(
    "click",
    e=>{
        if(
            !e.target.closest(".canvasSettings")
        ){
            settingsPanel.classList.remove("open");
        }
    }
);

function syncViewInputs(){
    document.getElementById("xminInput").value = fmt(xmin);
    document.getElementById("xmaxInput").value = fmt(xmax);
    document.getElementById("yminInput").value = fmt(ymin);
    document.getElementById("ymaxInput").value = fmt(ymax);
}

function applyViewInputs(){
    const a = Number(document.getElementById("xminInput").value);
    const b = Number(document.getElementById("xmaxInput").value);
    const c = Number(document.getElementById("yminInput").value);
    const d = Number(document.getElementById("ymaxInput").value);

    if(
        !Number.isFinite(a) ||
        !Number.isFinite(b) ||
        !Number.isFinite(c) ||
        !Number.isFinite(d) ||
        a>=b ||
        c>=d
    ){
        msg.textContent = "축 범위를 올바르게 입력하세요.";
        return;
    }

    xmin=a;
    xmax=b;
    ymin=c;
    ymax=d;
    draw();
}

["xminInput","xmaxInput","yminInput","ymaxInput"]
.forEach(
    id=>{
        document
        .getElementById(id)
        .addEventListener(
            "change",
            applyViewInputs
        );
    }
);

document
.getElementById("resetView")
.addEventListener(
    "click",
    ()=>{
        xmin=-10;
        xmax=10;
        ymin=-6;
        ymax=6;
        syncViewInputs();
        draw();
    }
);

document
.getElementById("gridToggle")
.addEventListener(
    "change",
    draw
);

document
.getElementById("axisToggle")
.addEventListener(
    "change",
    draw
);


/* ---------- keypad ---------- */

document
.getElementById("keypadToggle")
.addEventListener(
    "click",
    ()=>{
        document
        .getElementById("keypad")
        .classList.toggle("open");
    }
);

document
.querySelectorAll("#keypad [data-key]")
.forEach(
    button=>{
        button.addEventListener("mousedown", e=>{e.preventDefault();saveMathSelection();});
        button.addEventListener(
            "click",
            ()=>{
                const key=button.dataset.key;
                insertMathText(key);
            }
        );
    }
);


/* ---------- initial workspace values ---------- */

syncViewInputs();

/* =========================================================
   리사이즈
========================================================= */

function resize(){

    const rect =
        canvas.getBoundingClientRect();


    const dpr =
        window.devicePixelRatio ||
        1;


    canvas.width =
        Math.max(
            600,
            Math.floor(
                rect.width*dpr
            )
        );


    canvas.height =
        Math.max(
            400,
            Math.floor(
                rect.height*dpr
            )
        );


    ctx.setTransform(
        dpr,
        0,
        0,
        dpr,
        0,
        0
    );


    draw();

}


window.addEventListener(
    "resize",
    resize
);


/* =========================================================
   초기화
========================================================= */

libraries =
    loadLibraries();


currentLibraryId =
    libraries[0].id;


createFreshWorkspace();


renderLibrarySelect();

renderSongList();


resize();

renderLayers();
renderArrangement(0);

draw();


})();

</script>

</body>
</html>
"""

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background:#fff !important;
        margin:0 !important;
        padding:0 !important;
        overflow:hidden !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display:none !important;
    }
    [data-testid="stMainBlockContainer"] {
        max-width:none !important;
        width:100% !important;
        padding:0 !important;
        margin:0 !important;
    }
    [data-testid="stIFrame"], [data-testid="stIFrame"] iframe {
        height:calc(100vh - 2px) !important;
        min-height:0 !important;
        border:0 !important;
        display:block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)




TRACE_HTML = '<!DOCTYPE html>\n<html lang="ko">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Cosmos | 그래핑 계산기</title>\n    <!-- Tailwind CSS CDN -->\n    <script src="https://cdn.tailwindcss.com"></script>\n    <!-- Math.js CDN -->\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>\n    <!-- FontAwesome CDN -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n    \n    <style>\n        @import url(\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap\');\n        \n        body {\n            font-family: \'Inter\', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n            overflow: hidden;\n            user-select: none;\n            -webkit-user-select: none;\n        }\n\n        /* Cosmos Keypad Button Styling */\n        .key-btn {\n            background-color: #f1f3f4;\n            border: 1px solid #dadce0;\n            border-radius: 4px;\n            font-family: \'Inter\', system-ui, sans-serif;\n            font-size: 13px;\n            font-weight: 500;\n            color: #202124;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            cursor: pointer;\n            transition: all 0.08s ease;\n            box-shadow: 0 1px 1px rgba(0,0,0,0.05);\n        }\n        .key-btn:hover {\n            background-color: #e8eaed;\n            border-color: #bdc1c6;\n        }\n        .key-btn:active {\n            background-color: #d2d6da;\n            transform: translateY(1px);\n        }\n        .key-btn-dark {\n            background-color: #dadce0;\n            color: #3c4043;\n            font-weight: 600;\n        }\n        .key-btn-dark:hover {\n            background-color: #bdc1c6;\n        }\n        .key-btn-blue {\n            background-color: #2b72ee;\n            color: white;\n            border-color: #1a62e0;\n            font-weight: 600;\n        }\n        .key-btn-blue:hover {\n            background-color: #1a62e0;\n        }\n\n        /* Cosmos Audio Trace Panel Button Styling */\n        .audio-btn {\n            background-color: #ffffff;\n            border: 1px solid #dadce0;\n            border-radius: 4px;\n            font-size: 12px;\n            font-weight: 500;\n            color: #3c4043;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            cursor: pointer;\n            transition: all 0.1s;\n        }\n        .audio-btn:hover {\n            background-color: #f8f9fa;\n            border-color: #bdc1c6;\n        }\n        .audio-btn:active {\n            background-color: #e8eaed;\n        }\n\n        /* Custom Scrollbar */\n        ::-webkit-scrollbar {\n            width: 6px;\n            height: 6px;\n        }\n        ::-webkit-scrollbar-track {\n            background: #f8f9fa;\n        }\n        ::-webkit-scrollbar-thumb {\n            background: #dadce0;\n            border-radius: 3px;\n        }\n        ::-webkit-scrollbar-thumb:hover {\n            background: #bdc1c6;\n        }\n\n        .color-popover {\n            box-shadow: 0 4px 12px rgba(0,0,0,0.15);\n            border: 1px solid #dadce0;\n        }\n    </style>\n</head>\n<body class="bg-slate-100 h-screen w-screen flex flex-col font-sans text-slate-800">\n\n    <!-- 1. TOP NAVBAR -->\n    <header class="bg-[#1c2836] text-white h-12 px-3 flex items-center justify-between z-30 shrink-0 select-none">\n        <!-- Left Title and Save -->\n        <div class="flex items-center space-x-2">\n            <button onclick="showToast(\'폴더 목록을 불러왔습니다.\')" class="p-1.5 hover:bg-slate-700/60 rounded text-slate-300 hover:text-white transition">\n                <i class="fa-regular fa-folder text-base"></i>\n            </button>\n            <input id="graph-title-input" type="text" value="Cosmos 그래프" \n                   class="bg-transparent text-slate-100 text-sm font-medium px-2 py-1 rounded hover:bg-slate-700/40 focus:bg-slate-800 focus:outline-none border border-transparent focus:border-slate-600 transition w-36 sm:w-48">\n            <button onclick="saveGraphState()" class="bg-[#2b72ee] hover:bg-blue-600 text-white text-xs font-semibold px-3 py-1.5 rounded transition shadow-sm">\n                저장\n            </button>\n        </div>\n\n        <!-- Center Logo -->\n        <div class="absolute left-1/2 transform -translate-x-1/2 flex items-center cursor-pointer" onclick="resetView()">\n            <span class="text-xl font-bold tracking-tight text-white font-serif italic">cosmos</span>\n        </div>\n\n        <!-- Right User Actions -->\n        <div class="flex items-center space-x-1 sm:space-x-2">\n            <button onclick="openModal(\'login-modal\')" class="hidden sm:inline-block text-xs font-medium px-3 py-1.5 rounded hover:bg-slate-700/60 transition">\n                로그인\n            </button>\n            <button onclick="openModal(\'signup-modal\')" class="bg-[#2b72ee] hover:bg-blue-600 text-white text-xs font-semibold px-3 py-1.5 rounded transition shadow-sm">\n                회원가입\n            </button>\n            <div class="h-4 w-[1px] bg-slate-600 mx-1"></div>\n            <button onclick="openModal(\'share-modal\')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="공유">\n                <i class="fa-solid fa-share-nodes text-sm"></i>\n            </button>\n            <button onclick="openModal(\'help-modal\')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="도움말">\n                <i class="fa-regular fa-circle-question text-sm"></i>\n            </button>\n            <button onclick="toggleAngleMode()" id="btn-lang-toggle" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition text-xs font-semibold" title="각도 단위 전환 (라디안/각도)">\n                Rad\n            </button>\n            <button onclick="openModal(\'settings-modal\')" class="p-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 rounded transition" title="설정">\n                <i class="fa-solid fa-wrench text-sm"></i>\n            </button>\n        </div>\n    </header>\n\n    <!-- MAIN WORKSPACE -->\n    <div class="flex-1 flex relative overflow-hidden">\n\n        <!-- 2. LEFT SIDEBAR (EXPRESSIONS PANEL) -->\n        <aside id="sidebar-panel" class="w-[340px] sm:w-[380px] bg-white border-r border-slate-300 flex flex-col z-20 transition-all duration-200 shrink-0">\n            \n            <!-- Sidebar Toolbar Header -->\n            <div class="h-10 border-b border-slate-200 px-3 flex items-center justify-between bg-slate-50 shrink-0 relative">\n                <div class="flex items-center space-x-1">\n                    <!-- Add Item Menu Dropdown -->\n                    <button id="btn-add-menu" onclick="toggleAddMenu()" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="항목 추가">\n                        <i class="fa-solid fa-plus text-base"></i>\n                    </button>\n                    <!-- History Undo/Redo -->\n                    <button onclick="undo()" id="btn-undo" class="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200/70 rounded transition" title="되돌리기">\n                        <i class="fa-solid fa-rotate-left text-xs"></i>\n                    </button>\n                    <button onclick="redo()" id="btn-redo" class="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200/70 rounded transition" title="다시 실행">\n                        <i class="fa-solid fa-rotate-right text-xs"></i>\n                    </button>\n                </div>\n\n                <div class="flex items-center space-x-1">\n                    <button onclick="showToast(\'편집 모드가 활성화되었습니다.\')" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="수식 목록 편집">\n                        <i class="fa-solid fa-gear text-sm"></i>\n                    </button>\n                    <button id="btn-collapse-sidebar" class="p-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70 rounded transition" title="패널 숨기기">\n                        <i class="fa-solid fa-angles-left text-sm"></i>\n                    </button>\n                </div>\n\n                <!-- Add Menu Popover -->\n                <div id="add-menu-popover" class="hidden absolute top-9 left-2 bg-white border border-slate-300 rounded-lg shadow-xl z-50 py-1 w-40 text-sm">\n                    <button onclick="addExpression(\'\'); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">\n                        <i class="fa-solid fa-calculator text-blue-600 text-xs"></i>\n                        <span>수식 (Expression)</span>\n                    </button>\n                    <button onclick="addTableItem(); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">\n                        <i class="fa-solid fa-table text-emerald-600 text-xs"></i>\n                        <span>표 (Table)</span>\n                    </button>\n                    <button onclick="addNoteItem(); hideAddMenu()" class="w-full text-left px-3 py-1.5 hover:bg-slate-100 flex items-center space-x-2">\n                        <i class="fa-regular fa-note-sticky text-amber-600 text-xs"></i>\n                        <span>주석 (Note)</span>\n                    </button>\n                </div>\n            </div>\n\n            <!-- Expressions Scrollable List -->\n            <div id="expressions-list" class="flex-1 overflow-y-auto divide-y divide-slate-100">\n                <!-- Dynamically populated math items -->\n            </div>\n        </aside>\n\n        <!-- Sidebar Re-open Floating Button -->\n        <button id="btn-expand-sidebar" class="hidden absolute top-3 left-3 z-30 bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 p-2 rounded-lg shadow-md transition">\n            <i class="fa-solid fa-angles-right text-sm"></i>\n        </button>\n\n        <!-- 3. GRAPH CANVAS ENGINE -->\n        <main class="flex-1 relative bg-white overflow-hidden flex flex-col">\n            <canvas id="graph-canvas" class="w-full h-full block cursor-crosshair"></canvas>\n\n            <!-- Top Right Graph Controls -->\n            <div class="absolute top-3 right-3 flex flex-col bg-white border border-slate-300 rounded-lg shadow-md overflow-hidden z-10 text-slate-700">\n                <button onclick="openModal(\'settings-modal\')" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="그래프 설정">\n                    <i class="fa-solid fa-wrench text-xs"></i>\n                </button>\n                <button onclick="zoomIn()" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="확대">\n                    <i class="fa-solid fa-plus text-xs"></i>\n                </button>\n                <button onclick="zoomOut()" class="p-2.5 hover:bg-slate-100 border-b border-slate-200 transition" title="축소">\n                    <i class="fa-solid fa-minus text-xs"></i>\n                </button>\n                <button onclick="resetView()" class="p-2.5 hover:bg-slate-100 transition" title="기본 보기로 돌아가기">\n                    <i class="fa-solid fa-house text-xs"></i>\n                </button>\n            </div>\n\n            <!-- Hover / Pinned Point Label Overlay -->\n            <div id="point-tooltip" class="pointer-events-none absolute hidden bg-slate-900/90 text-white text-xs px-2.5 py-1 rounded shadow-lg z-20 font-mono -translate-x-1/2 -translate-y-full mb-2">\n                <span id="tooltip-coords">(0, 0)</span>\n            </div>\n        </main>\n    </div>\n\n    <!-- 4. BOTTOM KEYPAD & AUDIO TRACE CONTROLS PANEL -->\n    <div id="bottom-panel" class="bg-[#e8eaed] border-t border-slate-300 z-30 flex flex-col shrink-0 select-none shadow-2xl transition-all duration-200">\n        \n        <!-- Tab Header Selector: Math Keyboard vs Audio Trace -->\n        <div class="h-8 bg-[#dadce0] px-3 flex items-center justify-between text-xs text-slate-600 border-b border-slate-300">\n            <div class="flex items-center space-x-2">\n                <button id="tab-btn-keypad" onclick="switchBottomTab(\'keypad\')" class="px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition">\n                    가상 키보드\n                </button>\n                <button id="tab-btn-audio" onclick="switchBottomTab(\'audio\')" class="px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition flex items-center space-x-1">\n                    <i class="fa-solid fa-volume-high text-xs text-blue-600"></i>\n                    <span>오디오 추적 (Audio Trace)</span>\n                </button>\n            </div>\n            <button id="btn-hide-bottom-panel" class="hover:text-slate-900 transition p-1">\n                <i class="fa-solid fa-chevron-down text-xs"></i>\n            </button>\n        </div>\n\n        <!-- TAB 1: VIRTUAL MATH KEYBOARD -->\n        <div id="keypad-tab-content" class="p-2 max-w-5xl mx-auto w-full grid grid-cols-12 gap-1.5 h-44 sm:h-48 text-sm">\n            <!-- Col 1-4: Variables & Math Symbols -->\n            <div class="col-span-4 grid grid-cols-4 gap-1">\n                <button class="key-btn" onclick="insertKey(\'x\')"><i>x</i></button>\n                <button class="key-btn" onclick="insertKey(\'y\')"><i>y</i></button>\n                <button class="key-btn" onclick="insertKey(\'^2\')"><i>a</i>²</button>\n                <button class="key-btn" onclick="insertKey(\'^\')"><i>a</i><sup><i>b</i></sup></button>\n\n                <button class="key-btn" onclick="insertKey(\'(\')">(</button>\n                <button class="key-btn" onclick="insertKey(\')\')">)</button>\n                <button class="key-btn" onclick="insertKey(\'<\')">&lt;</button>\n                <button class="key-btn" onclick="insertKey(\'>\')">&gt;</button>\n\n                <button class="key-btn" onclick="insertKey(\'|\')">|<i>a</i>|</button>\n                <button class="key-btn" onclick="insertKey(\',\')">,</button>\n                <button class="key-btn" onclick="insertKey(\'<=\')">≤</button>\n                <button class="key-btn" onclick="insertKey(\'>=\')">≥</button>\n\n                <button class="key-btn key-btn-dark" onclick="insertKey(\'a\')"><i>a</i></button>\n                <button class="key-btn key-btn-dark" onclick="insertKey(\'b\')"><i>b</i></button>\n                <button class="key-btn" onclick="insertKey(\'sqrt(\')">√</button>\n                <button class="key-btn" onclick="insertKey(\'pi\')">π</button>\n            </div>\n\n            <!-- Col 5-8: Standard Numpad -->\n            <div class="col-span-4 grid grid-cols-4 gap-1">\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'7\')">7</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'8\')">8</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'9\')">9</button>\n                <button class="key-btn key-btn-dark text-base" onclick="insertKey(\'/\')">÷</button>\n\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'4\')">4</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'5\')">5</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'6\')">6</button>\n                <button class="key-btn key-btn-dark text-base" onclick="insertKey(\'*\')">×</button>\n\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'1\')">1</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'2\')">2</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'3\')">3</button>\n                <button class="key-btn key-btn-dark text-base" onclick="insertKey(\'-\')">-</button>\n\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'0\')">0</button>\n                <button class="key-btn font-bold bg-white" onclick="insertKey(\'.\')">.</button>\n                <button class="key-btn key-btn-dark text-base" onclick="insertKey(\'=\')">=</button>\n                <button class="key-btn key-btn-dark text-base" onclick="insertKey(\'+\')">+</button>\n            </div>\n\n            <!-- Col 9-12: Functions & Actions -->\n            <div class="col-span-4 grid grid-cols-3 gap-1">\n                <button class="key-btn key-btn-dark" onclick="insertKey(\'sin(\')">sin</button>\n                <button class="key-btn key-btn-dark" onclick="moveCursor(-1)"><i class="fa-solid fa-arrow-left text-xs"></i></button>\n                <button class="key-btn key-btn-dark" onclick="moveCursor(1)"><i class="fa-solid fa-arrow-right text-xs"></i></button>\n\n                <button class="key-btn" onclick="insertKey(\'cos(\')">cos</button>\n                <button class="key-btn" onclick="insertKey(\'tan(\')">tan</button>\n                <button class="key-btn key-btn-dark" onclick="handleBackspace()"><i class="fa-solid fa-delete-left text-sm"></i></button>\n\n                <button class="key-btn" onclick="insertKey(\'log(\')">log</button>\n                <button class="key-btn" onclick="insertKey(\'ln(\')">ln</button>\n                <button class="key-btn key-btn-blue row-span-2" onclick="handleEnter()">↵</button>\n\n                <button class="key-btn" onclick="insertKey(\'e\')"><i>e</i></button>\n                <button class="key-btn" onclick="insertKey(\'abs(\')">abs</button>\n            </div>\n        </div>\n\n        <!-- TAB 2: COSMOS AUDIO TRACE PANEL -->\n        <div id="audio-tab-content" class="hidden p-3 w-full flex-col space-y-3 max-h-72 overflow-y-auto">\n            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">\n                \n                <!-- Section 1: Audio Playback Controls -->\n                <div class="flex flex-col space-y-2 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">\n                    <button id="btn-audio-play" onclick="toggleAudioPlayback()" class="w-full bg-[#2b72ee] hover:bg-blue-600 text-white font-semibold py-2 px-3 rounded flex items-center justify-center space-x-2 shadow transition">\n                        <i id="audio-play-icon" class="fa-solid fa-play text-xs"></i>\n                        <span id="audio-play-text">그래프 듣기</span>\n                    </button>\n                    \n                    <div class="grid grid-cols-2 gap-2 text-[11px]">\n                        <label class="flex flex-col gap-1 text-slate-600">볼륨 <span id="audio-vol-text" class="font-semibold text-slate-800">50%</span>\n                            <input id="audio-volume-range" type="range" min="0" max="1" step="0.01" value="0.5" class="w-full accent-blue-600" aria-label="오디오 볼륨">\n                        </label>\n                        <label class="flex flex-col gap-1 text-slate-600">재생 속도 <span id="audio-speed-text" class="font-semibold text-slate-800">1.00×</span>\n                            <input id="audio-speed-range" type="range" min="0.25" max="3" step="0.05" value="1" class="w-full accent-blue-600" aria-label="오디오 재생 속도">\n                        </label>\n                    </div>\n                    <div class="grid grid-cols-2 gap-2 text-[11px]">\n                        <label class="flex flex-col gap-1 text-slate-600">추적 대상\n                            <select id="audio-track-mode" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800">\n                                <option value="active">선택한 함수</option><option value="visible">표시 중인 함수 전체</option>\n                            </select>\n                        </label>\n                        <label class="flex flex-col gap-1 text-slate-600">음색\n                            <select id="audio-waveform" class="border border-slate-300 rounded px-2 py-1.5 bg-white text-slate-800">\n                                <option value="sine">부드러운 사인파</option><option value="triangle">삼각파</option><option value="sawtooth">톱니파</option><option value="square">사각파</option>\n                            </select>\n                        </label>\n                    </div>\n                    <div class="grid grid-cols-3 gap-2 text-[11px]">\n                        <label class="flex flex-col gap-1 text-slate-600">시작 x\n                            <input id="audio-x-start" type="number" value="-10" step="0.5" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 text-slate-800">\n                        </label>\n                        <label class="flex flex-col gap-1 text-slate-600">끝 x\n                            <input id="audio-x-end" type="number" value="10" step="0.5" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 text-slate-800">\n                        </label>\n                        <label class="flex flex-col gap-1 text-slate-600">재생 시간\n                            <select id="audio-duration" class="w-full min-w-0 border border-slate-300 rounded px-2 py-1 bg-white text-slate-800">\n                                <option value="8">8초</option><option value="15" selected>15초</option><option value="30">30초</option><option value="60">1분</option>\n                            </select>\n                        </label>\n                    </div>\n                    <div class="flex items-center gap-2">\n                        <button onclick="restartAudioTrace()" class="audio-btn px-2 py-1.5 flex-1"><i class="fa-solid fa-rotate-left mr-1"></i>처음부터</button>\n                        <button onclick="stopAudioTrace()" class="audio-btn px-2 py-1.5 flex-1"><i class="fa-solid fa-stop mr-1"></i>정지</button>\n                    </div>\n                    <label class="block text-[11px] text-slate-600">재생 위치 <span id="audio-progress-text" class="font-semibold text-slate-800">x = -10.00</span>\n                        <input id="audio-progress" type="range" min="0" max="1000" step="1" value="0" class="w-full accent-blue-600">\n                    </label>\n                    <div id="audio-note-readout" class="rounded bg-slate-50 border border-slate-200 px-2 py-1.5 text-[11px] text-slate-600">음높이: 대기 중 · 추적 점: 대기 중</div>\n                    <button id="btn-audio-trace-status" class="w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center">\n                        오디오 추적 꺼짐\n                    </button>\n                </div>\n\n                <!-- Section 2: Point & Curve Navigation -->\n                <div class="flex flex-col space-y-2 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">\n                    <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider text-center">내비게이션</span>\n                    \n                    <div class="grid grid-cols-3 gap-1 items-center text-center text-xs">\n                        <button onclick="navigatePoint(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-chevron-left"></i></button>\n                        <span class="font-medium text-slate-700">점</span>\n                        <button onclick="navigatePoint(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-chevron-right"></i></button>\n\n                        <button onclick="navigateInterest(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-angles-left"></i></button>\n                        <span class="font-medium text-slate-700">관심지점</span>\n                        <button onclick="navigateInterest(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-angles-right"></i></button>\n\n                        <button onclick="navigateCurve(-1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-caret-up"></i></button>\n                        <span class="font-medium text-slate-700">곡선</span>\n                        <button onclick="navigateCurve(1)" class="audio-btn py-1 px-2"><i class="fa-solid fa-caret-down"></i></button>\n                    </div>\n                </div>\n\n                <!-- Section 3: Screen Reader Speech Accessibility -->\n                <div class="flex flex-col space-y-1.5 bg-white p-2.5 rounded-lg border border-slate-300 shadow-sm">\n                    <div class="flex items-center justify-between">\n                        <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">스크린 리더</span>\n                        <i class="fa-solid fa-circle-info text-slate-400 text-xs" title="웹 음성합성 API 지원"></i>\n                    </div>\n\n                    <button onclick="speakDescription(\'point\')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">\n                        점 설명\n                    </button>\n                    <button onclick="speakDescription(\'curve\')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">\n                        곡선 설명\n                    </button>\n                    <button onclick="speakDescription(\'axis\')" class="audio-btn py-1.5 px-3 w-full justify-center font-medium">\n                        축 설명\n                    </button>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <!-- Toggle Bottom Panel Floating Button -->\n    <button id="btn-toggle-bottom" class="fixed bottom-2 left-2 z-40 bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 px-2.5 py-1.5 rounded-lg shadow-md flex items-center space-x-1.5 text-xs font-medium transition">\n        <i class="fa-solid fa-keyboard"></i>\n        <i class="fa-solid fa-caret-down text-[10px]"></i>\n    </button>\n\n    <!-- Color / Style Picker Popover Modal -->\n    <div id="color-popover" class="hidden absolute z-50 bg-white rounded-lg p-2.5 color-popover flex flex-col space-y-2">\n        <div class="flex items-center space-x-2">\n            <button onclick="setColorForSelected(\'#c74440\')" class="w-6 h-6 rounded-full bg-[#c74440] hover:scale-110 transition"></button>\n            <button onclick="setColorForSelected(\'#2d70b3\')" class="w-6 h-6 rounded-full bg-[#2d70b3] hover:scale-110 transition"></button>\n            <button onclick="setColorForSelected(\'#388c46\')" class="w-6 h-6 rounded-full bg-[#388c46] hover:scale-110 transition"></button>\n            <button onclick="setColorForSelected(\'#6042a6\')" class="w-6 h-6 rounded-full bg-[#6042a6] hover:scale-110 transition"></button>\n            <button onclick="setColorForSelected(\'#000000\')" class="w-6 h-6 rounded-full bg-black hover:scale-110 transition"></button>\n        </div>\n        <div class="h-[1px] bg-slate-200 w-full"></div>\n        <div class="flex items-center justify-between text-xs text-slate-600">\n            <button onclick="setStyleForSelected(\'solid\')" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium">실선</button>\n            <button onclick="setStyleForSelected(\'dashed\')" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium">점선</button>\n        </div>\n    </div>\n\n    <!-- MODAL DIALOGS -->\n    <div id="modal-backdrop" class="hidden fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">\n        \n        <!-- Login Modal -->\n        <div id="login-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-sm w-full p-6 flex flex-col space-y-4">\n            <div class="flex justify-between items-center">\n                <h3 class="text-lg font-bold text-slate-800">Cosmos 로그인</h3>\n                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>\n            </div>\n            <input type="email" placeholder="이메일 주소" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">\n            <input type="password" placeholder="비밀번호" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">\n            <button onclick="showToast(\'로그인 되었습니다.\'); closeModal();" class="w-full bg-[#2b72ee] text-white py-2 rounded font-semibold text-sm hover:bg-blue-600 transition">로그인</button>\n        </div>\n\n        <!-- Signup Modal -->\n        <div id="signup-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-sm w-full p-6 flex flex-col space-y-4">\n            <div class="flex justify-between items-center">\n                <h3 class="text-lg font-bold text-slate-800">계정 만들기</h3>\n                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>\n            </div>\n            <input type="text" placeholder="이름" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">\n            <input type="email" placeholder="이메일 주소" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">\n            <input type="password" placeholder="비밀번호 설정" class="w-full border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-blue-500">\n            <button onclick="showToast(\'계정이 생성되었습니다.\'); closeModal();" class="w-full bg-[#2b72ee] text-white py-2 rounded font-semibold text-sm hover:bg-blue-600 transition">회원가입</button>\n        </div>\n\n        <!-- Share Modal -->\n        <div id="share-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-4">\n            <div class="flex justify-between items-center">\n                <h3 class="text-lg font-bold text-slate-800">그래프 공유</h3>\n                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>\n            </div>\n            <p class="text-xs text-slate-500">그래프 주소를 복사하거나 링크를 공유하세요.</p>\n            <div class="flex items-center space-x-2">\n                <input id="share-url-input" readonly value="" placeholder="배포 후 공유 주소가 여기에 표시됩니다" class="flex-1 border border-slate-300 rounded px-3 py-2 text-xs bg-slate-50 font-mono">\n                <button onclick="copyShareUrl()" class="bg-slate-800 text-white px-3 py-2 rounded text-xs font-semibold hover:bg-slate-700 transition">복사</button>\n            </div>\n        </div>\n\n        <!-- Settings Modal -->\n        <div id="settings-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-4">\n            <div class="flex justify-between items-center">\n                <h3 class="text-lg font-bold text-slate-800">그래프 설정</h3>\n                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>\n            </div>\n            \n            <div class="space-y-3 text-sm">\n                <div class="flex justify-between items-center">\n                    <span class="text-slate-700 font-medium">각도 단위</span>\n                    <div class="flex border border-slate-300 rounded overflow-hidden">\n                        <button id="set-rad-btn" onclick="setAngleUnit(\'rad\')" class="px-3 py-1 bg-blue-600 text-white font-semibold text-xs">라디안 (Radians)</button>\n                        <button id="set-deg-btn" onclick="setAngleUnit(\'deg\')" class="px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs">각도 (Degrees)</button>\n                    </div>\n                </div>\n                <div class="flex justify-between items-center">\n                    <span class="text-slate-700 font-medium">그리드 표시</span>\n                    <input type="checkbox" id="chk-grid" checked onchange="toggleGrid(this.checked)" class="w-4 h-4 text-blue-600">\n                </div>\n                <div class="flex justify-between items-center">\n                    <span class="text-slate-700 font-medium">축 번호 표시</span>\n                    <input type="checkbox" id="chk-numbers" checked onchange="toggleNumbers(this.checked)" class="w-4 h-4 text-blue-600">\n                </div>\n            </div>\n        </div>\n\n        <!-- Help Modal -->\n        <div id="help-modal" class="hidden bg-white rounded-xl shadow-2xl max-w-md w-full p-6 flex flex-col space-y-3">\n            <div class="flex justify-between items-center">\n                <h3 class="text-lg font-bold text-slate-800">도움말 및 수식 안내</h3>\n                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>\n            </div>\n            <div class="text-xs text-slate-600 space-y-2 leading-relaxed">\n                <p>• <b>함수 입력예시:</b> <code class="bg-slate-100 px-1 py-0.5 rounded">y = sin(x)</code>, <code class="bg-slate-100 px-1 py-0.5 rounded">y = x^2 - 4</code>, <code class="bg-slate-100 px-1 py-0.5 rounded">y = 2*x + 1</code></p>\n                <p>• <b>변수 슬라이더:</b> 수식에 <code class="bg-slate-100 px-1 py-0.5 rounded">a</code> 또는 <code class="bg-slate-100 px-1 py-0.5 rounded">b</code>를 입력하면 슬라이더 조절바가 생성됩니다.</p>\n                <p>• <b>오디오 추적:</b> 오디오 추적 탭에서 [그래프 듣기]를 클릭하면 음고와 스테레오 사운드로 그래프를 청각화합니다.</p>\n            </div>\n        </div>\n    </div>\n\n    <!-- Toast Notification -->\n    <div id="toast-msg" class="fixed bottom-12 right-4 z-50 bg-slate-800 text-white text-xs px-3 py-2 rounded-lg shadow-xl opacity-0 transition-opacity duration-300 pointer-events-none">\n        알림 메시지\n    </div>\n\n    <!-- JAVASCRIPT APPLICATION LOGIC ENGINE -->\n    <script>\n        /**\n         * Core Application State\n         */\n        const state = {\n            scale: 60, // Screen pixels per math coordinate unit\n            offsetX: 0,\n            offsetY: 0,\n            isDragging: false,\n            dragStart: { x: 0, y: 0 },\n            \n            showGrid: true,\n            showNumbers: true,\n            angleUnit: \'rad\', // \'rad\' or \'deg\'\n\n            items: [], // Array of expressions / notes / tables\n            variables: { a: 1, b: 2 }, // Active slider variables\n            activeItemId: null,\n            colorPopoverItemId: null,\n            \n            history: [],\n            historyIdx: -1,\n\n            // Audio Engine & Trace State\n            audio: {\n                ctx: null,\n                masterGain: null,\n                tracks: [],\n                isPlaying: false,\n                vol: 0.5,\n                speed: 1,\n                duration: 15,\n                timer: null,\n                startedAt: 0,\n                elapsedBeforePause: 0,\n                currX: -10,\n                xStart: -10,\n                xEnd: 10,\n                waveform: \'sine\',\n                mode: \'active\',\n                lastFrameAt: 0\n            },\n\n            // Interactive Snap Points\n            snapPoints: [],\n            pinnedPoints: [],\n            activeHoverPoint: null,\n            navPointIdx: 0\n        };\n\n        const PALETTE = [\'#c74440\', \'#2d70b3\', \'#388c46\', \'#6042a6\', \'#000000\'];\n        let colorIndex = 0;\n        function getNextColor() {\n            return PALETTE[colorIndex++ % PALETTE.length];\n        }\n\n        /**\n         * DOM Elements Initialization\n         */\n        const canvas = document.getElementById(\'graph-canvas\');\n        const ctx = canvas.getContext(\'2d\');\n        const expressionsList = document.getElementById(\'expressions-list\');\n        const bottomPanel = document.getElementById(\'bottom-panel\');\n        const btnToggleBottom = document.getElementById(\'btn-toggle-bottom\');\n        const btnHideBottomPanel = document.getElementById(\'btn-hide-bottom-panel\');\n        const sidebarPanel = document.getElementById(\'sidebar-panel\');\n        const btnCollapseSidebar = document.getElementById(\'btn-collapse-sidebar\');\n        const btnExpandSidebar = document.getElementById(\'btn-expand-sidebar\');\n        const tooltip = document.getElementById(\'point-tooltip\');\n        const tooltipCoords = document.getElementById(\'tooltip-coords\');\n        const colorPopover = document.getElementById(\'color-popover\');\n\n        /**\n         * Canvas Auto-Resizer Engine\n         */\n        function resizeCanvas() {\n            const rect = canvas.parentElement.getBoundingClientRect();\n            const dpr = window.devicePixelRatio || 1;\n            canvas.width = Math.max(1, Math.round(rect.width * dpr));\n            canvas.height = Math.max(1, Math.round(rect.height * dpr));\n            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);\n            render();\n        }\n        window.addEventListener(\'resize\', resizeCanvas);\n\n        /**\n         * Coordinate Transformations\n         */\n        function mathToScreen(x, y) {\n            const width = canvas.width / window.devicePixelRatio;\n            const height = canvas.height / window.devicePixelRatio;\n            const centerX = width / 2 + state.offsetX;\n            const centerY = height / 2 + state.offsetY;\n            return {\n                x: centerX + x * state.scale,\n                y: centerY - y * state.scale\n            };\n        }\n\n        function screenToMath(px, py) {\n            const width = canvas.width / window.devicePixelRatio;\n            const height = canvas.height / window.devicePixelRatio;\n            const centerX = width / 2 + state.offsetX;\n            const centerY = height / 2 + state.offsetY;\n            return {\n                x: (px - centerX) / state.scale,\n                y: (centerY - py) / state.scale\n            };\n        }\n\n        /**\n         * Rendering Engine: Grid, Functions, Snap Points, Tables\n         */\n        function render() {\n            const width = canvas.width / window.devicePixelRatio;\n            const height = canvas.height / window.devicePixelRatio;\n\n            ctx.fillStyle = \'#ffffff\';\n            ctx.fillRect(0, 0, width, height);\n\n            if (state.showGrid) {\n                drawGrid(width, height);\n            }\n\n            state.snapPoints = []; // Reset snap points for current frame\n\n            // Render Function Curves & Tables\n            state.items.forEach(item => {\n                if (item.visible) {\n                    if (item.type === \'expression\' && item.compiled) {\n                        drawFunction(item, width, height);\n                    } else if (item.type === \'table\') {\n                        drawTablePoints(item);\n                    }\n                }\n            });\n\n            // Draw Computed Snap Points (Gray Dots)\n            drawSnapPoints();\n\n            // Draw Pinned Coordinate Labels\n            drawPinnedPoints();\n\n            // Audio trace playhead guide and active point\n            if (state.activeHoverPoint && state.activeHoverPoint.audioTrace) {\n                const width = canvas.width / (window.devicePixelRatio || 1);\n                const height = canvas.height / (window.devicePixelRatio || 1);\n                const guide = mathToScreen(state.activeHoverPoint.x, 0).x;\n                ctx.save();\n                ctx.strokeStyle = state.activeHoverPoint.color || \'#2b72ee\';\n                ctx.globalAlpha = 0.25;\n                ctx.setLineDash([4, 4]);\n                ctx.beginPath(); ctx.moveTo(guide, 0); ctx.lineTo(guide, height); ctx.stroke();\n                ctx.setLineDash([]); ctx.restore();\n            }\n            if (state.activeHoverPoint) drawActiveHoverMarker();\n        }\n\n        /**\n         * Cosmos coordinate grid renderer\n         */\n        function drawGrid(width, height) {\n            const centerX = width / 2 + state.offsetX;\n            const centerY = height / 2 + state.offsetY;\n\n            let unitStep = 1;\n            const targetPixelStep = 80;\n            const rawUnits = targetPixelStep / state.scale;\n            const magnitude = Math.pow(10, Math.floor(Math.log10(rawUnits)));\n            const residual = rawUnits / magnitude;\n\n            if (residual >= 5) unitStep = 5 * magnitude;\n            else if (residual >= 2) unitStep = 2 * magnitude;\n            else unitStep = 1 * magnitude;\n\n            const stepPixels = unitStep * state.scale;\n\n            // Minor Grid Lines\n            ctx.lineWidth = 0.5;\n            ctx.strokeStyle = \'#e2e8f0\';\n            ctx.beginPath();\n            const subStep = stepPixels / 5;\n            for (let x = (centerX % subStep) - subStep; x < width; x += subStep) {\n                ctx.moveTo(x, 0); ctx.lineTo(x, height);\n            }\n            for (let y = (centerY % subStep) - subStep; y < height; y += subStep) {\n                ctx.moveTo(0, y); ctx.lineTo(width, y);\n            }\n            ctx.stroke();\n\n            // Major Grid Lines\n            ctx.lineWidth = 1;\n            ctx.strokeStyle = \'#cbd5e1\';\n            ctx.beginPath();\n            for (let x = (centerX % stepPixels) - stepPixels; x < width; x += stepPixels) {\n                ctx.moveTo(x, 0); ctx.lineTo(x, height);\n            }\n            for (let y = (centerY % stepPixels) - stepPixels; y < height; y += stepPixels) {\n                ctx.moveTo(0, y); ctx.lineTo(width, y);\n            }\n            ctx.stroke();\n\n            // Main Axes Lines\n            ctx.lineWidth = 1.5;\n            ctx.strokeStyle = \'#334155\';\n            ctx.beginPath();\n            ctx.moveTo(centerX, 0); ctx.lineTo(centerX, height);\n            ctx.moveTo(0, centerY); ctx.lineTo(width, centerY);\n            ctx.stroke();\n\n            // Axis Number Labels\n            if (state.showNumbers) {\n                ctx.fillStyle = \'#64748b\';\n                ctx.font = \'12px Inter, sans-serif\';\n                ctx.textAlign = \'center\';\n                ctx.textBaseline = \'top\';\n\n                const firstMathX = Math.ceil(-centerX / stepPixels) * unitStep;\n                const lastMathX = Math.floor((width - centerX) / stepPixels) * unitStep;\n\n                for (let mathX = firstMathX; mathX <= lastMathX; mathX += unitStep) {\n                    if (Math.abs(mathX) < 1e-9) continue;\n                    const screen = mathToScreen(mathX, 0);\n                    const labelY = Math.min(Math.max(centerY + 6, 6), height - 20);\n                    ctx.fillText(Number(mathX.toFixed(4)).toString(), screen.x, labelY);\n                }\n\n                ctx.textAlign = \'right\';\n                ctx.textBaseline = \'middle\';\n                const firstMathY = Math.ceil((centerY - height) / stepPixels) * unitStep;\n                const lastMathY = Math.floor(centerY / stepPixels) * unitStep;\n\n                for (let mathY = firstMathY; mathY <= lastMathY; mathY += unitStep) {\n                    if (Math.abs(mathY) < 1e-9) continue;\n                    const screen = mathToScreen(0, mathY);\n                    const labelX = Math.min(Math.max(centerX - 8, 28), width - 8);\n                    ctx.fillText(Number(mathY.toFixed(4)).toString(), labelX, screen.y);\n                }\n            }\n        }\n\n        /**\n         * Mathematical Curve & Snap Point Evaluation\n         */\n        function drawFunction(item, width, height) {\n            ctx.strokeStyle = item.color;\n            ctx.lineWidth = 2.5;\n\n            if (item.lineStyle === \'dashed\') ctx.setLineDash([8, 6]);\n            else ctx.setLineDash([]);\n\n            ctx.beginPath();\n            let isDrawing = false;\n            const stepPx = 2;\n\n            let prevY = null;\n            let prevMathX = null;\n            let prevSlope = null;\n\n            const scope = { ...state.variables };\n\n            for (let px = 0; px <= width; px += stepPx) {\n                const mathX = screenToMath(px, 0).x;\n                scope.x = mathX;\n\n                try {\n                    let yVal = item.compiled.evaluate(scope);\n                    if (typeof yVal === \'object\' && yVal.re !== undefined) yVal = yVal.re;\n\n                    if (typeof yVal === \'number\' && !isNaN(yVal) && isFinite(yVal)) {\n                        const screen = mathToScreen(mathX, yVal);\n                        \n                        if (!isDrawing) {\n                            ctx.moveTo(screen.x, screen.y);\n                            isDrawing = true;\n                        } else {\n                            ctx.lineTo(screen.x, screen.y);\n                        }\n\n                        // Snap Points: X-Intercept\n                        if (prevY !== null) {\n                            const slope = (yVal - prevY) / (mathX - prevMathX);\n                            \n                            if ((prevY < 0 && yVal >= 0) || (prevY > 0 && yVal <= 0)) {\n                                state.snapPoints.push({ x: mathX, y: yVal, color: item.color, type: \'intercept\' });\n                            }\n                            // Min/Max Extrema\n                            if (prevSlope !== null && ((prevSlope > 0 && slope < 0) || (prevSlope < 0 && slope > 0))) {\n                                state.snapPoints.push({ x: prevMathX, y: prevY, color: item.color, type: \'extrema\' });\n                            }\n                            prevSlope = slope;\n                        }\n\n                        // Y-Intercept\n                        if (prevMathX !== null && prevMathX < 0 && mathX >= 0) {\n                            scope.x = 0;\n                            const yZero = item.compiled.evaluate(scope);\n                            state.snapPoints.push({ x: 0, y: yZero, color: item.color, type: \'y-intercept\' });\n                        }\n\n                        prevY = yVal;\n                        prevMathX = mathX;\n                    } else {\n                        isDrawing = false;\n                    }\n                } catch (e) {\n                    isDrawing = false;\n                }\n            }\n            ctx.stroke();\n            ctx.setLineDash([]);\n        }\n\n        /**\n         * Render Table Coordinates & Scatter Points\n         */\n        function drawTablePoints(item) {\n            item.rows.forEach(row => {\n                if (row.x !== \'\' && row.y !== \'\') {\n                    const mathX = parseFloat(row.x);\n                    const mathY = parseFloat(row.y);\n                    if (!isNaN(mathX) && !isNaN(mathY)) {\n                        const screen = mathToScreen(mathX, mathY);\n                        ctx.fillStyle = item.color;\n                        ctx.beginPath();\n                        ctx.arc(screen.x, screen.y, 5, 0, Math.PI * 2);\n                        ctx.fill();\n                        ctx.strokeStyle = \'#ffffff\';\n                        ctx.lineWidth = 1.5;\n                        ctx.stroke();\n                    }\n                }\n            });\n        }\n\n        /**\n         * Draw Snap Dots & Pinned Coordinates\n         */\n        function drawSnapPoints() {\n            state.snapPoints.forEach(pt => {\n                const screen = mathToScreen(pt.x, pt.y);\n                ctx.fillStyle = \'#94a3b8\';\n                ctx.beginPath();\n                ctx.arc(screen.x, screen.y, 4, 0, Math.PI * 2);\n                ctx.fill();\n            });\n        }\n\n        function drawPinnedPoints() {\n            state.pinnedPoints.forEach(pt => {\n                const screen = mathToScreen(pt.x, pt.y);\n                ctx.fillStyle = pt.color || \'#334155\';\n                ctx.beginPath();\n                ctx.arc(screen.x, screen.y, 5, 0, Math.PI * 2);\n                ctx.fill();\n\n                // Draw Coordinate Box\n                const text = `(${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`;\n                ctx.font = \'12px Inter, sans-serif\';\n                const textWidth = ctx.measureText(text).width;\n\n                ctx.fillStyle = \'rgba(255, 255, 255, 0.9)\';\n                ctx.strokeStyle = \'#cbd5e1\';\n                ctx.lineWidth = 1;\n                ctx.beginPath();\n                ctx.roundRect(screen.x - textWidth / 2 - 6, screen.y - 28, textWidth + 12, 20, 4);\n                ctx.fill();\n                ctx.stroke();\n\n                ctx.fillStyle = \'#1e293b\';\n                ctx.textAlign = \'center\';\n                ctx.textBaseline = \'middle\';\n                ctx.fillText(text, screen.x, screen.y - 18);\n            });\n        }\n\n        function drawActiveHoverMarker() {\n            const pt = state.activeHoverPoint;\n            if (!pt || !Number.isFinite(pt.x) || !Number.isFinite(pt.y)) return;\n            const screen = mathToScreen(pt.x, pt.y);\n            const width = canvas.width / (window.devicePixelRatio || 1);\n            const height = canvas.height / (window.devicePixelRatio || 1);\n            if (screen.x < -20 || screen.x > width + 20 || screen.y < -20 || screen.y > height + 20) return;\n            ctx.save();\n            ctx.shadowColor = pt.color || \'#2b72ee\';\n            ctx.shadowBlur = pt.audioTrace ? 18 : 8;\n            ctx.fillStyle = pt.color || \'#2b72ee\';\n            ctx.beginPath();\n            ctx.arc(screen.x, screen.y, pt.audioTrace ? 7 : 6, 0, Math.PI * 2);\n            ctx.fill();\n            ctx.shadowBlur = 0;\n            ctx.strokeStyle = \'#ffffff\';\n            ctx.lineWidth = 2;\n            ctx.stroke();\n            if (pt.audioTrace) {\n                ctx.strokeStyle = pt.color || \'#2b72ee\';\n                ctx.globalAlpha = 0.45;\n                ctx.lineWidth = 1.5;\n                ctx.beginPath(); ctx.arc(screen.x, screen.y, 13, 0, Math.PI * 2); ctx.stroke();\n            }\n            ctx.restore();\n        }\n\n        /**\n         * Expressions & Sidebar List Manager\n         */\n        function addExpression(rawText = \'\') {\n            saveHistory();\n            const item = {\n                id: \'item_\' + Date.now() + \'_\' + Math.random().toString(36).substr(2, 4),\n                type: \'expression\',\n                rawText: rawText,\n                compiled: null,\n                color: getNextColor(),\n                lineStyle: \'solid\',\n                visible: true,\n                error: false,\n                hasSlider: false,\n                varName: null\n            };\n            state.items.push(item);\n            state.activeItemId = item.id;\n            renderExpressionList();\n            if (rawText) updateExpression(item.id, rawText);\n        }\n\n        function addTableItem() {\n            saveHistory();\n            const item = {\n                id: \'item_\' + Date.now(),\n                type: \'table\',\n                color: getNextColor(),\n                visible: true,\n                rows: [\n                    { x: \'-2\', y: \'4\' },\n                    { x: \'-1\', y: \'1\' },\n                    { x: \'0\', y: \'0\' },\n                    { x: \'1\', y: \'1\' },\n                    { x: \'2\', y: \'4\' }\n                ]\n            };\n            state.items.push(item);\n            renderExpressionList();\n            render();\n        }\n\n        function addNoteItem() {\n            saveHistory();\n            const item = {\n                id: \'item_\' + Date.now(),\n                type: \'note\',\n                text: \'주석을 입력하세요...\'\n            };\n            state.items.push(item);\n            renderExpressionList();\n        }\n\n        function updateExpression(id, text) {\n            const item = state.items.find(it => it.id === id);\n            if (!item) return;\n\n            item.rawText = text;\n            if (!text.trim()) {\n                item.compiled = null;\n                item.error = false;\n                item.hasSlider = false;\n                render();\n                return;\n            }\n\n            try {\n                let expr = text;\n                if (expr.includes(\'=\')) {\n                    expr = expr.split(\'=\')[1].trim();\n                }\n\n                // Check for slider variables (e.g., \'a\' or \'b\')\n                if (text.includes(\'a\') && !state.variables.hasOwnProperty(\'a\')) state.variables.a = 1;\n                if (text.includes(\'b\') && !state.variables.hasOwnProperty(\'b\')) state.variables.b = 2;\n\n                item.compiled = math.compile(expr);\n                item.compiled.evaluate({ x: 1, ...state.variables });\n                item.error = false;\n            } catch (err) {\n                item.compiled = null;\n                item.error = true;\n            }\n\n            render();\n        }\n\n        function removeExpression(id) {\n            saveHistory();\n            state.items = state.items.filter(it => it.id !== id);\n            if (state.activeItemId === id) {\n                state.activeItemId = state.items.length > 0 ? state.items[0].id : null;\n            }\n            renderExpressionList();\n            render();\n        }\n\n        function toggleVisibility(id) {\n            const item = state.items.find(it => it.id === id);\n            if (item) {\n                item.visible = !item.visible;\n                renderExpressionList();\n                render();\n            }\n        }\n\n        function updateVariableSlider(varName, value) {\n            state.variables[varName] = parseFloat(value);\n            document.getElementById(`slider-val-${varName}`).textContent = value;\n            render();\n        }\n\n        function updateTableCell(itemId, rowIdx, col, val) {\n            const item = state.items.find(it => it.id === itemId);\n            if (item && item.rows[rowIdx]) {\n                item.rows[rowIdx][col] = val;\n                render();\n            }\n        }\n\n        /**\n         * Render Expression List in Sidebar\n         */\n        function renderExpressionList() {\n            expressionsList.innerHTML = \'\';\n\n            state.items.forEach((item, index) => {\n                const el = document.createElement(\'div\');\n                el.className = `p-3 space-y-2 border-b border-slate-100 transition ${state.activeItemId === item.id ? \'bg-blue-50/50\' : \'hover:bg-slate-50\'}`;\n                \n                if (item.type === \'expression\') {\n                    el.innerHTML = `\n                        <div class="flex items-center space-x-2">\n                            <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>\n                            \n                            <button onclick="toggleVisibility(\'${item.id}\')" \n                                    oncontextmenu="openColorPopover(event, \'${item.id}\')"\n                                    class="w-6 h-6 rounded-full flex items-center justify-center shrink-0 transition" \n                                    style="background-color: ${item.visible ? item.color : \'transparent\'}; border: 2px solid ${item.color}">\n                                ${item.visible ? \'<i class="fa-solid fa-check text-white text-[10px]"></i>\' : \'\'}\n                            </button>\n\n                            <input id="input-${item.id}" type="text" value="${item.rawText}" placeholder="수식 입력 (예: y = sin(x))" \n                                   onfocus="setActiveItem(\'${item.id}\')"\n                                   oninput="updateExpression(\'${item.id}\', this.value)"\n                                   class="flex-1 text-base font-serif italic bg-transparent focus:outline-none ${item.error ? \'text-rose-600\' : \'text-slate-800\'}">\n\n                            <button onclick="removeExpression(\'${item.id}\')" class="text-slate-300 hover:text-slate-600 p-1 rounded transition">\n                                <i class="fa-solid fa-xmark text-sm"></i>\n                            </button>\n                        </div>\n                    `;\n                } else if (item.type === \'table\') {\n                    let rowsHtml = \'\';\n                    item.rows.forEach((r, rIdx) => {\n                        rowsHtml += `\n                            <tr class="border-b border-slate-100">\n                                <td class="p-1"><input type="text" value="${r.x}" oninput="updateTableCell(\'${item.id}\', ${rIdx}, \'x\', this.value)" class="w-full text-center bg-slate-50 border rounded text-xs py-0.5"></td>\n                                <td class="p-1"><input type="text" value="${r.y}" oninput="updateTableCell(\'${item.id}\', ${rIdx}, \'y\', this.value)" class="w-full text-center bg-slate-50 border rounded text-xs py-0.5"></td>\n                            </tr>\n                        `;\n                    });\n\n                    el.innerHTML = `\n                        <div class="flex items-center justify-between">\n                            <div class="flex items-center space-x-2">\n                                <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>\n                                <span class="text-xs font-bold text-emerald-600">표 (Table)</span>\n                            </div>\n                            <button onclick="removeExpression(\'${item.id}\')" class="text-slate-300 hover:text-slate-600 p-1 rounded"><i class="fa-solid fa-xmark text-sm"></i></button>\n                        </div>\n                        <table class="w-full text-xs text-center border">\n                            <thead>\n                                <tr class="bg-slate-100 font-semibold">\n                                    <th class="p-1 border">x₁</th>\n                                    <th class="p-1 border">y₁</th>\n                                </tr>\n                            </thead>\n                            <tbody>${rowsHtml}</tbody>\n                        </table>\n                    `;\n                } else if (item.type === \'note\') {\n                    el.innerHTML = `\n                        <div class="flex items-center space-x-2">\n                            <span class="text-xs font-semibold text-slate-400 w-4 text-right">${index + 1}</span>\n                            <input type="text" value="${item.text}" oninput="item.text=this.value" class="flex-1 text-xs text-slate-600 bg-transparent focus:outline-none italic">\n                            <button onclick="removeExpression(\'${item.id}\')" class="text-slate-300 hover:text-slate-600 p-1 rounded"><i class="fa-solid fa-xmark text-sm"></i></button>\n                        </div>\n                    `;\n                }\n\n                expressionsList.appendChild(el);\n            });\n\n            // Dynamically Render Variable Sliders if \'a\' or \'b\' exist\n            [\'a\', \'b\'].forEach(v => {\n                if (state.variables.hasOwnProperty(v)) {\n                    const sliderDiv = document.createElement(\'div\');\n                    sliderDiv.className = \'p-3 bg-amber-50/60 border-b border-amber-200 flex flex-col space-y-1.5\';\n                    sliderDiv.innerHTML = `\n                        <div class="flex justify-between items-center text-xs text-amber-900 font-semibold">\n                            <span>슬라이더 변수 ${v} = <span id="slider-val-${v}">${state.variables[v]}</span></span>\n                        </div>\n                        <input type="range" min="-10" max="10" step="0.1" value="${state.variables[v]}" \n                               oninput="updateVariableSlider(\'${v}\', this.value)" class="w-full accent-amber-600">\n                    `;\n                    expressionsList.appendChild(sliderDiv);\n                }\n            });\n        }\n\n        function setActiveItem(id) {\n            state.activeItemId = id;\n            // When paused, rebuild tracks on the next Play so the newly selected curve is followed.\n            if (!state.audio.isPlaying) disposeAudioTracks();\n        }\n\n        /**\n         * Popover Menu Handlers\n         */\n        function openColorPopover(e, itemId) {\n            e.preventDefault();\n            state.colorPopoverItemId = itemId;\n            colorPopover.style.left = `${e.clientX}px`;\n            colorPopover.style.top = `${e.clientY}px`;\n            colorPopover.classList.remove(\'hidden\');\n        }\n\n        function setColorForSelected(color) {\n            if (state.colorPopoverItemId) {\n                const item = state.items.find(it => it.id === state.colorPopoverItemId);\n                if (item) {\n                    item.color = color;\n                    renderExpressionList();\n                    render();\n                }\n            }\n            colorPopover.classList.add(\'hidden\');\n        }\n\n        function setStyleForSelected(style) {\n            if (state.colorPopoverItemId) {\n                const item = state.items.find(it => it.id === state.colorPopoverItemId);\n                if (item) {\n                    item.lineStyle = style;\n                    render();\n                }\n            }\n            colorPopover.classList.add(\'hidden\');\n        }\n\n        function toggleAddMenu() {\n            document.getElementById(\'add-menu-popover\').classList.toggle(\'hidden\');\n        }\n        function hideAddMenu() {\n            document.getElementById(\'add-menu-popover\').classList.add(\'hidden\');\n        }\n\n        /**\n         * Virtual On-Screen Keypad Functions\n         */\n        function insertKey(key) {\n            if (!state.activeItemId) return;\n            const input = document.getElementById(`input-${state.activeItemId}`);\n            if (!input) return;\n\n            const start = input.selectionStart;\n            const end = input.selectionEnd;\n            const val = input.value;\n\n            input.value = val.substring(0, start) + key + val.substring(end);\n            input.focus();\n            input.setSelectionRange(start + key.length, start + key.length);\n\n            updateExpression(state.activeItemId, input.value);\n        }\n\n        function handleBackspace() {\n            if (!state.activeItemId) return;\n            const input = document.getElementById(`input-${state.activeItemId}`);\n            if (!input) return;\n\n            const start = input.selectionStart;\n            const end = input.selectionEnd;\n            const val = input.value;\n\n            if (start === end && start > 0) {\n                input.value = val.substring(0, start - 1) + val.substring(start);\n                input.setSelectionRange(start - 1, start - 1);\n            } else if (start !== end) {\n                input.value = val.substring(0, start) + val.substring(end);\n                input.setSelectionRange(start, start);\n            }\n            input.focus();\n            updateExpression(state.activeItemId, input.value);\n        }\n\n        function moveCursor(dir) {\n            if (!state.activeItemId) return;\n            const input = document.getElementById(`input-${state.activeItemId}`);\n            if (!input) return;\n\n            const pos = input.selectionStart + dir;\n            input.focus();\n            input.setSelectionRange(pos, pos);\n        }\n\n        function handleEnter() {\n            addExpression();\n        }\n\n        /**\n         * Cosmos Audio Trace Engine\n         * Each visible curve can have its own oscillator. X controls time/pan;\n         * Y controls pitch, while a moving marker follows the sampled graph point.\n         */\n        function initAudioEngine() {\n            if (!state.audio.ctx) {\n                const AudioContextCtor = window.AudioContext || window.webkitAudioContext;\n                if (!AudioContextCtor) {\n                    showToast(\'이 브라우저는 Web Audio API를 지원하지 않습니다.\');\n                    return false;\n                }\n                state.audio.ctx = new AudioContextCtor();\n                state.audio.masterGain = state.audio.ctx.createGain();\n                state.audio.masterGain.gain.value = state.audio.vol;\n                state.audio.masterGain.connect(state.audio.ctx.destination);\n            }\n            if (state.audio.ctx.state === \'suspended\') state.audio.ctx.resume();\n            return true;\n        }\n\n        function getAudioTargets() {\n            const valid = state.items.filter(it => it.type === \'expression\' && it.visible && it.compiled && !it.error);\n            if (state.audio.mode === \'visible\') return valid;\n            const active = valid.find(it => it.id === state.activeItemId);\n            return active ? [active] : (valid.length ? [valid[0]] : []);\n        }\n\n        function disposeAudioTracks() {\n            state.audio.tracks.forEach(track => {\n                try { track.osc.stop(); } catch (_) {}\n                try { track.osc.disconnect(); track.gain.disconnect(); if (track.panner) track.panner.disconnect(); } catch (_) {}\n            });\n            state.audio.tracks = [];\n        }\n\n        function buildAudioTracks() {\n            disposeAudioTracks();\n            const targets = getAudioTargets();\n            if (!targets.length) return false;\n            const ctx = state.audio.ctx;\n            targets.forEach((item, index) => {\n                const osc = ctx.createOscillator();\n                const gain = ctx.createGain();\n                const panner = ctx.createStereoPanner ? ctx.createStereoPanner() : null;\n                osc.type = state.audio.waveform;\n                osc.frequency.value = 440;\n                gain.gain.value = 0;\n                if (panner) {\n                    osc.connect(panner);\n                    panner.connect(gain);\n                } else {\n                    osc.connect(gain);\n                }\n                gain.connect(state.audio.masterGain);\n                osc.start();\n                state.audio.tracks.push({ item, osc, gain, panner, index, count: targets.length });\n            });\n            return true;\n        }\n\n        function readAudioSettings() {\n            const startInput = document.getElementById(\'audio-x-start\');\n            const endInput = document.getElementById(\'audio-x-end\');\n            const start = Number(startInput.value);\n            const end = Number(endInput.value);\n            if (!Number.isFinite(start) || !Number.isFinite(end) || end <= start) {\n                showToast(\'끝 x는 시작 x보다 커야 합니다.\');\n                return false;\n            }\n            state.audio.xStart = start;\n            state.audio.xEnd = end;\n            state.audio.duration = (Number(document.getElementById(\'audio-duration\').value) || 15) / Math.max(0.25, state.audio.speed);\n            state.audio.mode = document.getElementById(\'audio-track-mode\').value;\n            state.audio.waveform = document.getElementById(\'audio-waveform\').value;\n            return true;\n        }\n\n        function toggleAudioPlayback() {\n            if (state.audio.isPlaying) {\n                pauseAudioTrace();\n                return;\n            }\n            if (!initAudioEngine() || !readAudioSettings()) return;\n            if (!state.audio.tracks.length && !buildAudioTracks()) {\n                showToast(\'추적할 함수가 없습니다. 수식을 입력하고 표시 상태를 확인하세요.\');\n                return;\n            }\n            // A completed run starts over; a paused run resumes from its last progress.\n            if (state.audio.elapsedBeforePause >= state.audio.duration) {\n                state.audio.elapsedBeforePause = 0;\n                disposeAudioTracks();\n                if (!buildAudioTracks()) {\n                    showToast(\'추적할 함수가 없습니다.\');\n                    return;\n                }\n            }\n            state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;\n            state.audio.isPlaying = true;\n            const status = document.getElementById(\'btn-audio-trace-status\');\n            status.textContent = state.audio.mode === \'visible\' ? `전체 그래프 추적 중 · ${state.audio.tracks.length}개 레이어` : \'선택한 그래프 추적 중\';\n            status.className = \'w-full bg-blue-100 text-blue-700 text-xs py-1 rounded font-semibold text-center\';\n            document.getElementById(\'audio-play-text\').textContent = \'일시정지\';\n            document.getElementById(\'audio-play-icon\').className = \'fa-solid fa-pause text-xs\';\n            state.audio.masterGain.gain.setTargetAtTime(state.audio.vol, state.audio.ctx.currentTime, 0.03);\n            cancelAnimationFrame(state.audio.timer);\n            state.audio.timer = requestAnimationFrame(audioTraceFrame);\n        }\n\n        function pauseAudioTrace() {\n            if (!state.audio.isPlaying) return;\n            state.audio.isPlaying = false;\n            state.audio.elapsedBeforePause = Math.min(state.audio.duration, (performance.now() - state.audio.startedAt) / 1000);\n            cancelAnimationFrame(state.audio.timer);\n            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02);\n            document.getElementById(\'audio-play-text\').textContent = \'계속 재생\';\n            document.getElementById(\'audio-play-icon\').className = \'fa-solid fa-play text-xs\';\n            const status = document.getElementById(\'btn-audio-trace-status\');\n            status.textContent = \'오디오 추적 일시정지됨\';\n            status.className = \'w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center\';\n        }\n\n        function stopAudioTrace() {\n            state.audio.isPlaying = false;\n            cancelAnimationFrame(state.audio.timer);\n            state.audio.elapsedBeforePause = 0;\n            state.audio.currX = state.audio.xStart;\n            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02);\n            state.audio.tracks.forEach(t => t.gain.gain.setTargetAtTime(0, state.audio.ctx.currentTime, 0.02));\n            document.getElementById(\'audio-play-text\').textContent = \'그래프 듣기\';\n            document.getElementById(\'audio-play-icon\').className = \'fa-solid fa-play text-xs\';\n            document.getElementById(\'btn-audio-trace-status\').textContent = \'오디오 추적 꺼짐\';\n            document.getElementById(\'btn-audio-trace-status\').className = \'w-full bg-slate-200 text-slate-600 text-xs py-1 rounded font-medium text-center\';\n            document.getElementById(\'audio-progress\').value = 0;\n            document.getElementById(\'audio-progress-text\').textContent = `x = ${state.audio.xStart.toFixed(2)}`;\n            document.getElementById(\'audio-note-readout\').textContent = \'음높이: 대기 중 · 추적 점: 대기 중\';\n            if (state.activeHoverPoint && state.activeHoverPoint.audioTrace) state.activeHoverPoint = null;\n            disposeAudioTracks();\n            render();\n        }\n\n        function restartAudioTrace() {\n            stopAudioTrace();\n            if (readAudioSettings()) {\n                state.audio.currX = state.audio.xStart;\n                document.getElementById(\'audio-progress\').value = 0;\n            }\n            toggleAudioPlayback();\n        }\n\n        function midiToFrequency(midi) { return 440 * Math.pow(2, (midi - 69) / 12); }\n        function frequencyToNote(freq) {\n            if (!Number.isFinite(freq) || freq <= 0) return \'—\';\n            const names = [\'도\', \'도♯\', \'레\', \'레♯\', \'미\', \'파\', \'파♯\', \'솔\', \'솔♯\', \'라\', \'라♯\', \'시\'];\n            const midi = Math.round(69 + 12 * Math.log2(freq / 440));\n            return `${names[((midi % 12) + 12) % 12]}${Math.floor(midi / 12) - 1}`;\n        }\n\n        function evaluateAudioY(item, x) {\n            try {\n                const value = item.compiled.evaluate({ x, ...state.variables });\n                const y = typeof value === \'number\' ? value : (value && typeof value.re === \'number\' ? value.re : NaN);\n                return Number.isFinite(y) ? y : NaN;\n            } catch (_) { return NaN; }\n        }\n\n        function audioTraceFrame(now) {\n            if (!state.audio.isPlaying) return;\n            const elapsed = Math.max(0, (now - state.audio.startedAt) / 1000);\n            const progress = Math.min(1, elapsed / state.audio.duration);\n            const x = state.audio.xStart + (state.audio.xEnd - state.audio.xStart) * progress;\n            state.audio.currX = x;\n            const progressSlider = document.getElementById(\'audio-progress\');\n            progressSlider.value = String(Math.round(progress * 1000));\n            document.getElementById(\'audio-progress-text\').textContent = `x = ${x.toFixed(2)} · ${elapsed.toFixed(1)}s / ${state.audio.duration}s`;\n\n            let firstValid = null;\n            const nowAudio = state.audio.ctx.currentTime;\n            state.audio.tracks.forEach(track => {\n                const y = evaluateAudioY(track.item, x);\n                if (!Number.isFinite(y) || Math.abs(y) > 1e6) {\n                    track.gain.gain.setTargetAtTime(0, nowAudio, 0.025);\n                    return;\n                }\n                if (!firstValid) firstValid = { x, y, color: track.item.color, audioTrace: true };\n                // Map graph height to a bounded, musical MIDI range (36–84).\n                const midi = Math.max(36, Math.min(84, 60 + y * 3));\n                const freq = midiToFrequency(midi);\n                track.osc.frequency.setTargetAtTime(freq, nowAudio, 0.025);\n                // Each visible graph gets a slightly different stereo position.\n                const graphPan = track.count <= 1 ? Math.max(-1, Math.min(1, (x - state.audio.xStart) / (state.audio.xEnd - state.audio.xStart) * 2 - 1)) : -0.85 + 1.7 * track.index / Math.max(1, track.count - 1);\n                if (track.panner) track.panner.pan.setTargetAtTime(graphPan, nowAudio, 0.04);\n                const yGain = Math.max(0.18, Math.min(1, 0.35 + (y + 4) / 16));\n                const layerGain = yGain / Math.sqrt(track.count);\n                track.gain.gain.setTargetAtTime(layerGain, nowAudio, 0.035);\n                if (track.item.id === state.activeItemId || !firstValid) firstValid = { x, y, color: track.item.color, audioTrace: true, freq };\n            });\n\n            if (firstValid) {\n                state.activeHoverPoint = firstValid;\n                const freq = firstValid.freq || midiToFrequency(Math.max(36, Math.min(84, 60 + firstValid.y * 3)));\n                document.getElementById(\'audio-note-readout\').textContent = `y = ${firstValid.y.toFixed(3)} · ${freq.toFixed(1)} Hz (${frequencyToNote(freq)}) · ${state.audio.tracks.length}개 트랙`;\n            } else {\n                state.activeHoverPoint = null;\n                document.getElementById(\'audio-note-readout\').textContent = `x = ${x.toFixed(2)} · 이 위치에서는 함수값이 정의되지 않아 소리를 잠시 멈춥니다.`;\n                state.audio.tracks.forEach(t => t.gain.gain.setTargetAtTime(0, nowAudio, 0.02));\n            }\n            render();\n\n            if (progress >= 1) {\n                state.audio.elapsedBeforePause = state.audio.duration;\n                pauseAudioTrace();\n                document.getElementById(\'audio-play-text\').textContent = \'처음부터 재생\';\n                return;\n            }\n            state.audio.timer = requestAnimationFrame(audioTraceFrame);\n        }\n\n        function changeAudioVolume() {\n            // Kept as a compatibility hook for older buttons.\n            state.audio.vol = state.audio.vol >= 0.99 ? 0.2 : (state.audio.vol <= 0.21 ? 0.5 : 1);\n            const slider = document.getElementById(\'audio-volume-range\');\n            if (slider) slider.value = state.audio.vol;\n            document.getElementById(\'audio-vol-text\').textContent = `${Math.round(state.audio.vol * 100)}%`;\n            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(state.audio.isPlaying ? state.audio.vol : 0, state.audio.ctx.currentTime, 0.02);\n        }\n\n        function changeAudioSpeed() {\n            state.audio.speed = state.audio.speed >= 2.95 ? 0.5 : (state.audio.speed <= 0.51 ? 1 : 3);\n            const slider = document.getElementById(\'audio-speed-range\');\n            if (slider) slider.value = state.audio.speed;\n            document.getElementById(\'audio-speed-text\').textContent = `${state.audio.speed.toFixed(2)}×`;\n        }\n\n        function seekAudioTrace() {\n            if (!readAudioSettings()) return;\n            const ratio = Number(document.getElementById(\'audio-progress\').value) / 1000;\n            state.audio.elapsedBeforePause = ratio * state.audio.duration;\n            state.audio.currX = state.audio.xStart + ratio * (state.audio.xEnd - state.audio.xStart);\n            const previewTargets = state.audio.tracks.length ? state.audio.tracks.map(t => t.item) : getAudioTargets();\n            for (const item of previewTargets) {\n                const y = evaluateAudioY(item, state.audio.currX);\n                if (Number.isFinite(y)) {\n                    state.activeHoverPoint = { x: state.audio.currX, y, color: item.color, audioTrace: true };\n                    break;\n                }\n            }\n            document.getElementById(\'audio-progress-text\').textContent = `x = ${state.audio.currX.toFixed(2)} · ${state.audio.elapsedBeforePause.toFixed(1)}s / ${state.audio.duration.toFixed(1)}s`;\n            if (state.audio.isPlaying) state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;\n            render();\n        }\n\n        document.getElementById(\'audio-volume-range\').addEventListener(\'input\', event => {\n            state.audio.vol = Number(event.target.value);\n            document.getElementById(\'audio-vol-text\').textContent = `${Math.round(state.audio.vol * 100)}%`;\n            if (state.audio.masterGain && state.audio.ctx) state.audio.masterGain.gain.setTargetAtTime(state.audio.isPlaying ? state.audio.vol : 0, state.audio.ctx.currentTime, 0.02);\n        });\n        document.getElementById(\'audio-speed-range\').addEventListener(\'input\', event => {\n            const newSpeed = Number(event.target.value);\n            if (state.audio.isPlaying) {\n                state.audio.elapsedBeforePause = Math.max(0, (performance.now() - state.audio.startedAt) / 1000);\n                state.audio.startedAt = performance.now() - state.audio.elapsedBeforePause * 1000;\n            }\n            state.audio.speed = newSpeed;\n            state.audio.duration = (Number(document.getElementById(\'audio-duration\').value) || 15) / state.audio.speed;\n            document.getElementById(\'audio-speed-text\').textContent = `${newSpeed.toFixed(2)}×`;\n        });\n        document.getElementById(\'audio-progress\').addEventListener(\'input\', seekAudioTrace);\n        [\'audio-track-mode\', \'audio-waveform\'].forEach(id => {\n            document.getElementById(id).addEventListener(\'change\', () => {\n                if (state.audio.isPlaying) pauseAudioTrace();\n                readAudioSettings();\n                disposeAudioTracks();\n            });\n        });\n        [\'audio-x-start\', \'audio-x-end\', \'audio-duration\'].forEach(id => {\n            document.getElementById(id).addEventListener(\'change\', () => {\n                if (state.audio.isPlaying) pauseAudioTrace();\n                readAudioSettings();\n                state.audio.elapsedBeforePause = 0;\n                state.audio.currX = state.audio.xStart;\n                document.getElementById(\'audio-progress\').value = 0;\n            });\n        });\n\n        function navigatePoint(dir) {\n            if (state.snapPoints.length === 0) return;\n            state.navPointIdx = (state.navPointIdx + dir + state.snapPoints.length) % state.snapPoints.length;\n            const pt = state.snapPoints[state.navPointIdx];\n            state.activeHoverPoint = pt;\n            tooltipCoords.textContent = `(${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`;\n            render();\n            showToast(`점 이동: (${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`);\n        }\n\n        function navigateInterest(dir) { navigatePoint(dir); }\n        function navigateCurve(dir) { navigatePoint(dir); }\n\n        function speakDescription(type) {\n            if (!(\'speechSynthesis\' in window)) {\n                showToast(\'브라우저가 음성 합성을 지원하지 않습니다.\');\n                return;\n            }\n            let msg = \'\';\n            if (type === \'point\' && state.activeHoverPoint) {\n                msg = `현재 추적 점의 X좌표는 ${state.activeHoverPoint.x.toFixed(2)}, Y좌표는 ${state.activeHoverPoint.y.toFixed(2)}입니다.`;\n            } else if (type === \'curve\') {\n                const active = state.items.find(it => it.id === state.activeItemId && it.type === \'expression\');\n                msg = active ? `현재 선택된 함수는 ${active.rawText || \'수식이 입력되지 않은 함수\'}입니다.` : \'먼저 왼쪽 수식 목록에서 함수를 선택해 주세요.\';\n            } else {\n                msg = \'좌표평면의 수평 X축과 수직 Y축, 그리고 원점의 위치를 표시하고 있습니다.\';\n            }\n            const utterance = new SpeechSynthesisUtterance(msg);\n            utterance.lang = \'ko-KR\';\n            window.speechSynthesis.speak(utterance);\n            showToast(\'음성 설명 재생 중...\');\n        }\n\n        function switchBottomTab(tab) {\n            const keypadContent = document.getElementById(\'keypad-tab-content\');\n            const audioContent = document.getElementById(\'audio-tab-content\');\n            const tabKeypad = document.getElementById(\'tab-btn-keypad\');\n            const tabAudio = document.getElementById(\'tab-btn-audio\');\n\n            if (tab === \'keypad\') {\n                keypadContent.classList.remove(\'hidden\');\n                audioContent.classList.add(\'hidden\');\n                tabKeypad.className = \'px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition\';\n                tabAudio.className = \'px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition flex items-center space-x-1\';\n            } else {\n                keypadContent.classList.add(\'hidden\');\n                audioContent.classList.remove(\'hidden\');\n                audioContent.classList.add(\'flex\');\n                tabAudio.className = \'px-3 py-1 font-semibold rounded bg-white text-slate-800 shadow-sm transition flex items-center space-x-1\';\n                tabKeypad.className = \'px-3 py-1 font-semibold rounded hover:bg-slate-200/80 text-slate-700 transition\';\n            }\n        }\n\n        /**\n         * Canvas Mouse Interactions (Pan, Zoom, Snap Pinning)\n         */\n        canvas.addEventListener(\'mousedown\', (e) => {\n            state.isDragging = true;\n            state.dragStart = { x: e.clientX, y: e.clientY };\n        });\n\n        window.addEventListener(\'mouseup\', () => {\n            state.isDragging = false;\n        });\n\n        canvas.addEventListener(\'mousemove\', (e) => {\n            const rect = canvas.getBoundingClientRect();\n            const mouseX = e.clientX - rect.left;\n            const mouseY = e.clientY - rect.top;\n\n            if (state.isDragging) {\n                state.offsetX += e.clientX - state.dragStart.x;\n                state.offsetY += e.clientY - state.dragStart.y;\n                state.dragStart = { x: e.clientX, y: e.clientY };\n                render();\n            } else {\n                // Detect Snap Point Hovering\n                let hovered = null;\n                for (let pt of state.snapPoints) {\n                    const screen = mathToScreen(pt.x, pt.y);\n                    if (Math.hypot(mouseX - screen.x, mouseY - screen.y) < 12) {\n                        hovered = pt;\n                        break;\n                    }\n                }\n\n                if (hovered) {\n                    state.activeHoverPoint = hovered;\n                    tooltipCoords.textContent = `(${hovered.x.toFixed(2)}, ${hovered.y.toFixed(2)})`;\n                    tooltip.style.left = `${e.clientX}px`;\n                    tooltip.style.top = `${e.clientY}px`;\n                    tooltip.classList.remove(\'hidden\');\n                } else {\n                    state.activeHoverPoint = null;\n                    tooltip.classList.add(\'hidden\');\n                }\n                render();\n            }\n        });\n\n        canvas.addEventListener(\'click\', (e) => {\n            if (state.activeHoverPoint) {\n                // Pin point label on canvas\n                state.pinnedPoints.push(state.activeHoverPoint);\n                render();\n            }\n        });\n\n        canvas.addEventListener(\'wheel\', (e) => {\n            e.preventDefault();\n            const factor = e.deltaY < 0 ? 1.1 : 0.9;\n            state.scale *= factor;\n            render();\n        }, { passive: false });\n\n        /**\n         * View Zoom & Reset Actions\n         */\n        function zoomIn() { state.scale *= 1.25; render(); }\n        function zoomOut() { state.scale /= 1.25; render(); }\n        function resetView() {\n            state.scale = 60;\n            state.offsetX = 0;\n            state.offsetY = 0;\n            state.pinnedPoints = [];\n            render();\n            showToast(\'그래프 보기가 초기화되었습니다.\');\n        }\n\n        /**\n         * History & State Management\n         */\n        function saveHistory() {\n            state.history = state.history.slice(0, state.historyIdx + 1);\n            state.history.push(JSON.stringify(state.items));\n            state.historyIdx++;\n        }\n\n        function undo() {\n            if (state.historyIdx > 0) {\n                state.historyIdx--;\n                state.items = JSON.parse(state.history[state.historyIdx]);\n                renderExpressionList();\n                render();\n            }\n        }\n\n        function redo() {\n            if (state.historyIdx < state.history.length - 1) {\n                state.historyIdx++;\n                state.items = JSON.parse(state.history[state.historyIdx]);\n                renderExpressionList();\n                render();\n            }\n        }\n\n        function saveGraphState() {\n            localStorage.setItem(\'cosmos_saved_graph\', JSON.stringify(state.items));\n            showToast(\'그래프가 브라우저에 저장되었습니다!\');\n        }\n\n        /**\n         * Modal Windows Management\n         */\n        function openModal(id) {\n            document.getElementById(\'modal-backdrop\').classList.remove(\'hidden\');\n            [\'login-modal\', \'signup-modal\', \'share-modal\', \'settings-modal\', \'help-modal\'].forEach(m => {\n                document.getElementById(m).classList.add(\'hidden\');\n            });\n            if (id === \'share-modal\') {\n                const shareInput = document.getElementById(\'share-url-input\');\n                shareInput.value = (window.location.protocol === \'http:\' || window.location.protocol === \'https:\')\n                    ? window.location.href : \'\';\n            }\n            document.getElementById(id).classList.remove(\'hidden\');\n        }\n\n        function closeModal() {\n            document.getElementById(\'modal-backdrop\').classList.add(\'hidden\');\n        }\n\n        function showToast(msg) {\n            const toast = document.getElementById(\'toast-msg\');\n            toast.textContent = msg;\n            toast.classList.remove(\'opacity-0\');\n            setTimeout(() => toast.classList.add(\'opacity-0\'), 2500);\n        }\n\n        function copyShareUrl() {\n            const input = document.getElementById(\'share-url-input\');\n            const currentUrl = window.location.href;\n            if (window.location.protocol === \'http:\' || window.location.protocol === \'https:\') {\n                input.value = currentUrl;\n                input.select();\n                if (navigator.clipboard && navigator.clipboard.writeText) {\n                    navigator.clipboard.writeText(currentUrl).then(() => showToast(\'Cosmos 주소를 복사했습니다.\')).catch(() => {\n                        document.execCommand(\'copy\'); showToast(\'주소 복사를 시도했습니다.\');\n                    });\n                } else {\n                    document.execCommand(\'copy\'); showToast(\'주소 복사를 시도했습니다.\');\n                }\n            } else {\n                showToast(\'로컬 파일로 실행 중입니다. 공유하려면 HTML 파일 자체를 전달하세요.\');\n            }\n        }\n\n        function toggleAngleMode() {\n            state.angleUnit = state.angleUnit === \'rad\' ? \'deg\' : \'rad\';\n            document.getElementById(\'btn-lang-toggle\').textContent = state.angleUnit === \'rad\' ? \'Rad\' : \'Deg\';\n            showToast(`각도 단위: ${state.angleUnit.toUpperCase()}`);\n        }\n\n        function setAngleUnit(unit) {\n            state.angleUnit = unit;\n            document.getElementById(\'set-rad-btn\').className = unit === \'rad\' ? \'px-3 py-1 bg-blue-600 text-white font-semibold text-xs\' : \'px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs\';\n            document.getElementById(\'set-deg-btn\').className = unit === \'deg\' ? \'px-3 py-1 bg-blue-600 text-white font-semibold text-xs\' : \'px-3 py-1 bg-slate-100 text-slate-600 font-semibold text-xs\';\n        }\n\n        function toggleGrid(checked) { state.showGrid = checked; render(); }\n        function toggleNumbers(checked) { state.showNumbers = checked; render(); }\n\n        /**\n         * UI Sidebar and Keypad Toggles\n         */\n        btnToggleBottom.addEventListener(\'click\', () => {\n            bottomPanel.classList.toggle(\'hidden\');\n        });\n        btnHideBottomPanel.addEventListener(\'click\', () => {\n            bottomPanel.classList.add(\'hidden\');\n        });\n\n        btnCollapseSidebar.addEventListener(\'click\', () => {\n            sidebarPanel.classList.add(\'-ml-[380px]\');\n            btnExpandSidebar.classList.remove(\'hidden\');\n            setTimeout(resizeCanvas, 200);\n        });\n        btnExpandSidebar.addEventListener(\'click\', () => {\n            sidebarPanel.classList.remove(\'-ml-[380px]\');\n            btnExpandSidebar.classList.add(\'hidden\');\n            setTimeout(resizeCanvas, 200);\n        });\n\n        /**\n         * Page Entry Point\n         */\n        window.onload = function() {\n            resizeCanvas();\n            // Initial Sine Graph matching screenshot\n            addExpression(\'y = sin(x)\');\n        };\n    </script>\n</body>\n</html>'

st.markdown("""<style>
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding-top:0.5rem; max-width:100%;}
</style>""", unsafe_allow_html=True)
workspace = st.radio(
    "Cosmos 작업 공간",
    ["Cosmos 음악 스튜디오 (기존 기능 전체)", "그래프 오디오 추적 (추적 점·실시간 음높이)"],
    horizontal=True,
    label_visibility="collapsed",
)
selected_html = HTML if workspace.startswith("Cosmos 음악") else TRACE_HTML
components.html(selected_html, height=1100, scrolling=False)
