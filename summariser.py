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
client = OpenAI() 

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert research paper summariser. Provide a clear, concise summary of the following research paper."},
            {"role": "user", "content": f"Summarise the following research paper:\n\n{text}"}
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

length_option = st.radio(
    "Choose Summary Length:",
    options=["short", "medium", "long"],
    index=1,
    horizontal=True
)

if uploaded_file:
    st.success("✅ File uploaded!")
    if st.button("Generate Summary"):
        with st.spinner("Reading PDF and generating summary..."):
            text = readpdf(uploaded_file)
            summary = summarize_text(text)
            st.subheader("Summary:")
            st.markdown(
                f"<div style='background-color:#f8f9fa; padding: 1rem; border-radius: 10px; color: #222;'>{summary}</div>",
                unsafe_allow_html=True
            )
