import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client()
city = "Paris"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give a short description of the city " + city,
)
print(interaction.output_text)
