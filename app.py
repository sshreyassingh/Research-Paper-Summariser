import streamlit as st
from pdf import readpdf
from summariser1 import summarize_text

# WEB BROWSER
st.set_page_config(page_title="Research Paper Summarizer", layout="centered")

# STYLING
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #8e44ad, #3498db);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# PAGE CONTENT
st.markdown("<h1>AI Research Paper Summarizer</h1>", unsafe_allow_html=True)
st.write("Upload a research paper (PDF) and get a summary based on your preferred length.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

length = st.radio(
    "Choose Summary Length:",
    options=["short", "medium", "long"],
    index=1,
    horizontal=True
)

format = st.radio(
    "Choose Summary Format:",
    options=["Paragraph","Pointers","Q&A"],
    index = 0,
    horizontal=True
)

language = st.radio(
    "Choose Language Style:",
    options=["Simple","Academic"],
    index = 0,
    horizontal=True
)

maxtokens = 8000
maxtokens = maxtokens * 4 

if uploaded_file:
    st.success("✅ File uploaded!")
    text = readpdf(uploaded_file)
    if len(text) > MAX_CHARS:
        st.warning("⚠️ The uploaded document is too long. Please upload a shorter file or summarize a section.")
    else:
        if st.button("Generate Summary"):
            with st.spinner("Reading PDF and generating summary..."):
                summary = summarize_text(text, length, format, language)
                st.subheader("Summary:")
                st.markdown(
                    f"<div style='background-color:#f8f9fa; padding: 1rem; border-radius: 10px; color: #222;'>{summary}</div>",
                    unsafe_allow_html=True
                )