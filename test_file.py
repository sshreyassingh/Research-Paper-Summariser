from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded API Key:", os.getenv("OPENAI_API_KEY")[:8] + "...")