import streamlit as st
import pandas as pd
from io import BytesIO
from ui import apply_global_style, page_header

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
apply_global_style()
page_header("📦 DTDC COD Reconciliation")

# --------------------------------------------------
# FILE READER (CSV + EXCEL)
# --------------------------------------------------

def read_file(file):
    name = file.name.lower()
    if name.endswith(".csv"):
        return pd.read_csv(file, dtype=str)
    else:
        return pd.read_excel(file, dtype=str)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "processed" not in st.session_state:
    st.session_state.processed = False

# --------------------------------------------------
# UPLOAD SECTION
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    dtdc_file = st.file_uploader(
        "Upload DTDC File",
        type=["xlsx", "xls", "csv"]
    )

with col2:
    sales_file = st.file_uploader(
        "Upload Sales File",
        type=["xlsx", "xls", "csv"]
    )

st.divider()

# --------------------------------------------------
# RECON BUTTON
# --------------------------------------------------

if st.button("🚀 Run DTDC Reconciliation", use_container_width=True):

    if not dtdc_file or not sales_file:
        st.warning("⚠ Please upload both files")
        st.stop()

    # LOADER
    with st.spinner("Reconciling DTDC COD data... Please wait ⏳"):

        # READ FILES
        dtdc = read_file(dtdc_file)
        sales = read_file(sales_file)

        dtdc.columns = dtdc.columns.str.strip()
        sales.columns = sales.columns.str.strip()

        # FILTER REMITTED
        dtdc = dtdc[dtdc["Remittance Status"] == "Remitted"]

        # FORMAT KEYS
        dtdc["CN Number"] = dtdc["CN Number"].astype(str).str.strip()
        sales["AWB num"] = sales["AWB num"].astype(str).str.strip()

        # MERGE
        merged = pd.merge(
            dtdc,
            sales,
            left_on="CN Number",
            right_on="AWB num",
            how="left"
        )

        # MATCH STATUS
        merged["Match Status"] = merged["Customer Email"].apply(
            lambda x: "Matched" if pd.notna(x) else "Unmatched"
        )

        # EXCEPTION
        exception = merged[merged["Match Status"] == "Unmatched"]

        # --------------------------------------------------
        # TALLY FORMAT
        # --------------------------------------------------

        tally = pd.DataFrame()

        tally["Date"] = pd.to_datetime(
            merged["Remittance Date"],
            errors="coerce"
        ).dt.strftime("%d-%m-%Y")

        tally["Credit"] = merged["Customer Email"].fillna("N/A")
        tally["Debit"] = "DTDC EXPRESS Receivable"

        tally["Debit Reference No"] = (
            merged["Sale Order Number"]
            .astype(str)
            .str.replace("#", "", regex=False)
            .replace("nan", "N/A")
        )

        tally.loc[
            merged["Match Status"] == "Unmatched",
            "Debit Reference No"
        ] = "N/A"

        tally["Gross Total"] = pd.to_numeric(
            merged["COD Amount"],
            errors="coerce"
        )

        tally["Narration"] = merged["CN Number"]

        # --------------------------------------------------
        # SORT TALLY BY DATE
        # --------------------------------------------------

        tally["Date"] = pd.to_datetime(tally["Date"], format="%d-%m-%Y", errors="coerce")
        tally = tally.sort_values(by="Date")
        tally["Date"] = tally["Date"].dt.strftime("%d-%m-%Y")

        # --------------------------------------------------
        # UTR SPLIT
        # --------------------------------------------------

        utr_buffer = BytesIO()

        with pd.ExcelWriter(utr_buffer, engine="openpyxl") as writer:
            for utr, df in merged.groupby("UTR Number"):
                sheet_name = str(utr)[:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        utr_buffer.seek(0)

        # SAVE SESSION RESULTS
        st.session_state.lookup = merged
        st.session_state.exception = exception
        st.session_state.tally = tally
        st.session_state.utr = utr_buffer
        st.session_state.processed = True

# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------

if st.session_state.processed:

    st.success("✅ DTDC Reconciliation Completed")

    st.subheader("📊 Reconciliation Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total DTDC Records", len(st.session_state.lookup))
    col2.metric(
        "Matched",
        (st.session_state.lookup["Match Status"] == "Matched").sum()
    )
    col3.metric(
        "Unmatched",
        (st.session_state.lookup["Match Status"] == "Unmatched").sum()
    )

    st.divider()

    def to_excel(df):
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)
        return buffer

    d1, d2 = st.columns(2)

    with d1:
        st.download_button(
            "⬇ Lookup File",
            to_excel(st.session_state.lookup),
            file_name="DTDC_Lookup.xlsx"
        )

        st.download_button(
            "⬇ Exception Report",
            to_excel(st.session_state.exception),
            file_name="DTDC_Exception.xlsx"
        )

    with d2:
        st.download_button(
            "⬇ Tally Import File",
            to_excel(st.session_state.tally),
            file_name="DTDC_Tally.xlsx"
        )

        st.download_button(
            "⬇ UTR Wise Split",
            st.session_state.utr,
            file_name="DTDC_UTR_Split.xlsx"
        )