from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Gemini
def readme_generator(prompt: str) -> str:
    try:
        client = genai.Client()

        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
        )

        if not response or not response.text:
                raise ValueError("Empty response from Gemini")

        return response.text.strip()

    except Exception as e:
        print(f"[Gemini error] {e}")
        return "" 