from fastapi import FastAPI
from .models import TripRequest
import requests

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/createTrip")
def create_trip(request: TripRequest):
    print(request)
    response = requests.get('http://ai-service:8000/getDescription', json=request.model_dump())
    # TODO still convert to JSON and get description out
    return {"city": request.city,
            "country_code": request.country_code,
            "description": response.text,
            }

