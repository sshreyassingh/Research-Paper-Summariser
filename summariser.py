import fitz
from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

# PDF READER
def readpdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    nopages = doc.page_count
    content = []
    for i in range(0,nopages):
        page = doc.load_page(i)
        text = page.get_text()
        actual = text.replace("\t"," ")
        content.append(actual)
    return " ".join(content)

#   SETTING UP OPENAI
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    project=os.getenv("OPENAI_PROJECT_ID")
)

def summarize_text(text,length,format,language):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert research paper summariser. Follow the user's preferred format and language style to generate a well rounded summary."},
            {"role": "user", "content": f"Summarize the following research paper in a {format.lower()} format, {language.lower()} language, and {length.lower()} length:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content

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

MAX_TOKENS = 8000
MAX_CHARS = MAX_TOKENS * 4 

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
