import streamlit as st
from ui import apply_global_style

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_global_style()

st.markdown(
    '<div class="main-title">📦 COD Reconciliation Portal</div>',
    unsafe_allow_html=True
)

st.write("")

c1, c2 = st.columns(2)

with c1:
    if st.button("📦 Bluedart COD Reconciliation",
                 use_container_width=True):
        st.switch_page("pages/1_Bluedart.py")

with c2:
    if st.button("🚚 Delhivery COD Reconciliation",
                 use_container_width=True):
        st.switch_page("pages/2_Delhivery.py")

st.success("✅ Unified Finance Reconciliation System")