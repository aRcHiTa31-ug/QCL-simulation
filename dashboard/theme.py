# dashboard/theme.py

import streamlit as st


def apply_theme():

    st.set_page_config(
        page_title="Quantum Cascade Laser Simulator",
        page_icon="⚛️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
<style>

/* =========================================================
REMOVE DEFAULT STREAMLIT UI
========================================================= */

header{
    visibility:hidden;
    height:0px;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

[data-testid="stHeader"]{
    display:none !important;
}

[data-testid="stToolbar"]{
    display:none !important;
}

[data-testid="stDecoration"]{
    display:none !important;
}

/* Remove white gap */

.block-container{

    padding-top:0.5rem !important;

    padding-bottom:2rem;

    padding-left:2rem;

    padding-right:2rem;

}

section.main > div{

    padding-top:0rem !important;

}

[data-testid="stAppViewContainer"]{

    margin-top:0rem !important;

}

/* =========================================================
APP BACKGROUND
========================================================= */

.stApp{

    background:linear-gradient(
        135deg,
        #071426,
        #0C2347,
        #10305F
    );

    color:white;

}

/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"]{

    background:linear-gradient(
        180deg,
        #08111F,
        #10284A
    );

    border-right:2px solid #2FD3FF;

    box-shadow:8px 0px 30px rgba(0,0,0,.45);

}

/* Everything inside sidebar */

[data-testid="stSidebar"] *{

    color:white !important;

}

/* Sidebar title */

[data-testid="stSidebar"] h1{

    color:white !important;

    font-size:32px;

    font-weight:800;

}

/* Sidebar caption */

[data-testid="stSidebar"] p{

    color:#C8DCF9 !important;

    font-size:14px;

}

/* =========================================================
EXPANDERS
========================================================= */

details{
    background:#172C52 !important;
    border-radius:14px;
    border:1px solid rgba(47,211,255,.25);
    overflow:hidden;
}

summary{
    background:#214A80 !important;
    color:white !important;
    font-weight:700;
    font-size:17px;
    padding:12px;
}

summary *{
    color:white !important;
}

summary:hover{
    background:#2C5A99 !important;
}
/* =========================================================
HEADINGS
========================================================= */

h1{

    color:white;

    font-weight:800;

}

h2{

    color:white;

    font-weight:700;

}

h3{

    color:#74E2FF;

    font-weight:700;

}

/* =========================================================
BUTTONS
========================================================= */

.stButton>button{

    width:100%;

    height:52px;

    border:none;

    border-radius:14px;

    background:linear-gradient(
        90deg,
        #2563EB,
        #22D3EE
    );

    color:white;

    font-size:16px;

    font-weight:700;

    transition:.30s;

    box-shadow:0 6px 18px rgba(0,180,255,.28);

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0 12px 30px rgba(0,180,255,.45);

}

/* =========================================================
INPUTS
========================================================= */
/* =========================================================
INPUTS
========================================================= */

/* Labels */

label{
    color:white !important;
    font-weight:600 !important;
}

/* Number Input */

.stNumberInput input{
    background:#102445 !important;
    color:white !important;
    border:1px solid #2FD3FF !important;
    border-radius:10px !important;
}

/* Text Input */

.stTextInput input{
    background:#102445 !important;
    color:white !important;
    border:1px solid #2FD3FF !important;
    border-radius:10px !important;
}

/* Selectbox */

div[data-baseweb="select"] > div{
    background:#102445 !important;
    color:white !important;
    border:1px solid #2FD3FF !important;
    border-radius:10px !important;
}

/* Selected value */

div[data-baseweb="select"] span{
    color:white !important;
}

/* Dropdown */

div[role="listbox"]{
    background:#102445 !important;
    border:1px solid #2FD3FF !important;
}

div[role="option"]{
    background:#102445 !important;
    color:white !important;
}

div[role="option"]:hover{
    background:#1D4ED8 !important;
}

/* Dropdown arrow */

div[data-baseweb="select"] svg{
    fill:white !important;
}

/* Slider */

.stSlider *{
    color:white !important;
}

/* =========================================================
TABS
========================================================= */

.stTabs [role="tab"]{

    background:#173764;

    color:white;

    border-radius:10px 10px 0px 0px;

    padding:10px 18px;

    font-weight:600;

}

.stTabs [aria-selected="true"]{

    background:linear-gradient(
        90deg,
        #2563EB,
        #22D3EE
    );

    color:white;

}

/* =========================================================
METRICS
========================================================= */

div[data-testid="metric-container"]{

    background:rgba(255,255,255,.06);

    backdrop-filter:blur(10px);

    border:1px solid rgba(47,211,255,.18);

    border-radius:15px;

    padding:18px;

    box-shadow:0 8px 22px rgba(0,0,0,.30);

}

/* =========================================================
TABLES
========================================================= */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

    box-shadow:0 10px 25px rgba(0,0,0,.30);

}

/* =========================================================
ALERTS
========================================================= */

.stSuccess,
.stWarning,
.stInfo{

    border-radius:12px;

}

/* =========================================================
IMAGES
========================================================= */

img{

    border-radius:18px;

    box-shadow:0 10px 30px rgba(0,0,0,.35);

}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#08111F;

}

::-webkit-scrollbar-thumb{

    background:#2FD3FF;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#67E8F9;

}

/* =========================================================
FIX SIDEBAR COMPONENTS
========================================================= */

[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div{
    color:white !important;
}

/* Metric text */

[data-testid="metric-container"] *{
    color:white !important;
}

/* Expander arrow */

summary svg{
    fill:white !important;
}

/* =========================================================
METRIC TEXT COLOR FIX
========================================================= */

div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(47,211,255,.18);
    border-radius: 15px;
}

div[data-testid="metric-container"] label {
    color: #DCEBFF !important;
    font-weight: 600 !important;
}

div[data-testid="metric-container"] p {
    color: white !important;
}

div[data-testid="metric-container"] div {
    color: white !important;
}

div[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

div[data-testid="stMetricLabel"] {
    color: #BFDFFF !important;
}

</style>
""", unsafe_allow_html=True)