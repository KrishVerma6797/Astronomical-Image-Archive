import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
PROMPT = """
You are an expert astronomer working at an astronomical observatory.

Analyze this astronomical image and generate a concise scientific caption.

Rules:
- Do NOT use numbered lists.
- Do NOT use bullet points.
- Write in one or two well-structured paragraphs.
- Use professional scientific language.
- Mention the probable astronomical object.
- Describe any visible structures.
- Mention any important observational characteristics.
- If uncertain, use phrases like "appears to" or "likely".
- Keep the response under 80 words.

Example:

This image appears to show a spiral galaxy with a bright central bulge and faint, well-defined spiral arms extending outward. The object is isolated against a dark background, suggesting a deep-space observation. The compact and symmetric morphology indicates a distant galaxy observed under good imaging conditions.

Only return the caption.
"""

def generate_caption(image_path):
    image=Image.open(image_path)
    response=client.models.generate_content(model="gemini-3.5-flash",contents=[PROMPT,image])
    return response.text
