from fastapi import FastAPI
from .models import TripRequest

import os
from dotenv import load_dotenv
from google import genai

app = FastAPI()
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/getDescription")
def create_trip(request: TripRequest):
    children_string = (
        f'and children of age {",".join(map(str, request.children_ages))}'
        if len(request.children_ages) > 0
        else ""
    )
    input_string = (
        f'Give a short description of the city {request.city}, '
        f'in the country {request.country_code} for a '
        f'trip with {request.adults} adults {children_string}'
    )
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=input_string,
    )
    return {"description": interaction.output_text}
