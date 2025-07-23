# 📑 AI Research Paper Summariser

A Streamlit-based web app that allows you to upload a research paper (PDF) and generate a concise, customizable summary using OpenAI’s **GPT-4o**.

Ideal for researchers, students, and professionals looking to quickly understand lengthy academic papers.

---

## 🚀 Features
- Upload PDF research papers directly through the web interface.
- Choose summary length: short, medium, or long.
- Choose summary format: paragraph, pointers, or Q&A.
- Choose language style: simple or academic.
- Generates summaries using GPT-4o.
- Supports PDFs with content up to ~8000 tokens (~6000 words)for accurate summarization.

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sshreyassingh/Research-Paper-Summariser.git
cd Research-Paper-Summariser
```

---

### 2️⃣ Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows
```

---

### 3️⃣ Install required packages
Install packages manually:
```bash
pip install streamlit pymupdf python-dotenv openai
```


### 4️⃣ Add your OpenAI API key
This app requires your **own OpenAI API key**.  
Create a `.env` file in the project directory and add:

```
OPENAI_API_KEY=your_openai_api_key_here
```


### 5️⃣ Run the Streamlit app
```bash
streamlit run summariser.py
```
This will open the app in your default browser at `http://localhost:8501`.

---

## Important
- This project **does not include any API key**. You must add your own in `.env`.
- Summarization uses GPT-4o. Ensure your OpenAI account has access.
- Supports PDF inputs up to ~8000 tokens (~6000 words) for best results.

---

## Credits
Built by Shreya Singh, Saina Suhag, and Saisha Angra as a part of Generative AI Capstone Project under IGDTUW.

---

## This project is intended for educational and research purposes only.
