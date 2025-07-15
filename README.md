# 📑 AI Research Paper Summariser

This is a Streamlit-based web app that lets you upload a research paper (PDF) and generates a summary using OpenAI’s GPT-4.  
It helps researchers, students, and professionals quickly grasp lengthy papers by producing concise summaries.

---

## 🚀 Features
- Upload PDF research papers directly through the web interface.
- Choose summary length: short, medium, or long.
- Generates summaries using GPT-4.

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
- Summarization uses GPT-4. Ensure your OpenAI account has access.

---

## Credits
Built by Shreya Singh, Saina Suhag, and Saisha Angra as a Generative AI Capstone Project under IGDTUW.

---

## This project is intended for educational and research purposes only.
