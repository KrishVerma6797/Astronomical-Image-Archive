import os
import json
from dotenv import load_dotenv
from google import genai

from backend.ai.prompt import PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_filters(user_query):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=PROMPT + user_query
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
