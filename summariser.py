import os
from openai import OpenAI
from dotenv import load_dotenv

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