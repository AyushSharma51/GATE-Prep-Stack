import streamlit as st
import os


st.title("GATE Previous Year Papers")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_PATH = os.path.join(BASE_DIR, "papers", "cse")

# Check folder exists

if not os.path.exists(PAPERS_PATH):
    st.error(f"Folder not found: {PAPERS_PATH}")
    st.stop()

# Get PDF files

files = os.listdir(PAPERS_PATH)
pdf_files = [f for f in files if f.endswith(".pdf")]

if not pdf_files:
    st.warning("No PDF files found")
    st.stop()

# Clean filenames

papers = [f.replace(".pdf", "").strip() for f in pdf_files if f.strip()]
papers.sort()

# Format labels for UI

def format_label(name):
    if "-" in name:
        parts = name.split("-")
        if len(parts) == 2:
            year, shift = parts
            return f"{year} Shift {shift}"
    return name  # IMPORTANT

# Dropdown

selected = st.selectbox(
"Select Year / Shift",
options=papers,
format_func=format_label
)

# Button logic


if st.button("Open Paper"):
    file_path = os.path.join(PAPERS_PATH, f"{selected}.pdf")

    if os.path.exists(file_path):
        # 🔹 Show PDF directly
        st.pdf(file_path)

        # 🔹 Download option
        with open(file_path, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name=f"{selected}.pdf",
                mime="application/pdf"
            )
    else:
        st.error("File not found")