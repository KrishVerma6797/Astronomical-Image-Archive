import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
PROMPT="""
You are an astronomy expert.

Analyze this astronomical image.

Describe:

1. Object type
2. Visible structures
3. Scientific observations

Maximum 60 words.

Do not hallucinate.
If uncertain, say "appears to".
"""

def generate_caption(image_path):
    image=Image.open(image_path)
    response=client.models.generate_content(model="gemini-3.5-flash",contents=[PROMPT,image])
    return response.text
