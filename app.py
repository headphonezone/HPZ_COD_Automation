import streamlit as st
from ui import apply_global_style

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_global_style()

# CLEAR PAGE STATES WHEN HOME LOADS
for key in list(st.session_state.keys()):
    if "processed" in key:
        st.session_state[key] = False

st.markdown(
    '<div class="main-title">🖥 COD Reconciliation Portal</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🔄 Bluedart COD Reconciliation",
                 use_container_width=True):
        st.switch_page("pages/1_Bluedart.py")

with c2:
    if st.button("🔄 Delhivery COD Reconciliation",
                 use_container_width=True):
        st.switch_page("pages/2_Delhivery.py")

with c3:
    if st.button("🔄 DTDC COD Reconciliation",
                 use_container_width=True):
        st.switch_page("pages/3_DTDC.py")

st.success("✅ Unified Finance Reconciliation System")