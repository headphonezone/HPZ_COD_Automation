import streamlit as st

# -------------------------------------------------
# GLOBAL STYLE
# -------------------------------------------------

def apply_global_style():

    st.markdown("""
    <style>

    /* ---------- REMOVE STREAMLIT UI ---------- */
    header {visibility:hidden;}
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}

    [data-testid="stSidebar"] {display:none !important;}
    [data-testid="collapsedControl"] {display:none !important;}

    /* ---------- FULL WIDTH ---------- */
    .block-container{
        max-width:100% !important;
        padding-top:2rem;
        padding-left:3rem;
        padding-right:3rem;
    }

    /* ---------- DARK THEME ---------- */
    .stApp{
        background-color:#0E1117;
        color:white;
    }

    /* ---------- TITLE ---------- */
    .main-title{
        text-align:center;
        font-size:44px;
        font-weight:700;
        margin-bottom:30px;
        color:white;
    }

    /* ---------- BUTTON STYLE ---------- */
    div.stButton > button{
        height:80px;
        font-size:20px;
        border-radius:12px;
        background:#161B22;
        border:1px solid #2a2f3a;
        color:white;
        transition:0.3s;
    }

    div.stButton > button:hover{
        background:#238636;
        transform:scale(1.02);
    }

    /* ---------- METRIC CARD ---------- */
    div[data-testid="metric-container"]{
        background:#161B22;
        border-radius:12px;
        padding:15px;
        border:1px solid #2a2f3a;
    }

    </style>
    """, unsafe_allow_html=True)


# -------------------------------------------------
# PAGE HEADER
# -------------------------------------------------

def page_header(title):

    left, center, right = st.columns([2,8,2])

    with left:
        if st.button("🏠 Home"):
            st.switch_page("app.py")

    with center:
        st.markdown(
            f'<div class="main-title">{title}</div>',
            unsafe_allow_html=True
        )