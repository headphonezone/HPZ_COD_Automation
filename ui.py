import streamlit as st
import base64
from pathlib import Path

# -------------------------------------------------
# GLOBAL STYLE
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
def get_base64_logo(logo):
    logo_path = BASE_DIR / "assets" / logo

    with open(logo_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def apply_global_style():

    st.markdown("""
    <style>

    /* -------- REMOVE STREAMLIT DEFAULT UI -------- */
    header {visibility:hidden;}
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}

    section[data-testid="stSidebar"]{
        display:none !important;
    }

    div[data-testid="collapsedControl"]{
        display:none !important;
    }

    div[data-testid="stToolbar"]{
        display:none !important;
    }

    /* -------- PAGE LAYOUT -------- */
    .block-container{
        max-width:1200px;
        margin:auto;
        padding-top:2rem;
    }

    /* -------- WHITE THEME -------- */
    .stApp{
        background-color:#F6F8FA;
        color:#111;
    }

    /* -------- TITLE -------- */
    .main-title{
        text-align:center;
        font-size:40px;
        font-weight:700;
        margin-bottom:30px;
        color:#111;
    }

    /* -------- BUTTON STYLE -------- */
    div.stButton > button{
        height:80px;
        font-size:18px;
        border-radius:10px;
        background:white;
        border:1px solid #d0d7de;
        color:#111;
        box-shadow:0px 2px 6px rgba(0,0,0,0.05);
        transition:0.2s;
    }

    div.stButton > button:hover{
        background:#0969DA;
        color:white;
        transform:scale(1.02);
    }

    /* -------- FILE UPLOADER -------- */
    [data-testid="stFileUploader"]{
        background:white;
        padding:20px;
        border-radius:10px;
        border:1px solid #d0d7de;
    }

    /* -------- METRIC CARD -------- */
    div[data-testid="metric-container"]{
        background:white;
        border-radius:10px;
        padding:15px;
        border:1px solid #d0d7de;
        box-shadow:0px 2px 6px rgba(0,0,0,0.05);
    }

    </style>
    """, unsafe_allow_html=True)


# -------------------------------------------------
# PAGE HEADER
# -------------------------------------------------

def page_header(title, logo):

    col1, col2 = st.columns([1, 12])

    # Home Button
    with col1:
        if st.button("🏠", key="home"):
            st.switch_page("app.py")

    # Logo + Title aligned
    with col2:
        st.markdown(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:15px;
            ">
                <img src="data:image/png;base64,{get_base64_logo(logo)}"
                     width="60">
                <h1 style="margin:0;">{title}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )