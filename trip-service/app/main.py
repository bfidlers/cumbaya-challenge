from fastapi import FastAPI
from .models import TripRequest
import requests
import json

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/createTrip")
def create_trip(request: TripRequest):
    print(request)
    response = requests.post('http://ai-service:8000/getDescription', json=request.model_dump())
    json_response = json.loads(response.text)
    return {"city": request.city,
            "country_code": request.country_code,
            "description": json_response["description"],
            }

