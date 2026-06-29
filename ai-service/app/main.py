from fastapi import FastAPI
from .models import TripRequest

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/getDescription")
async def create_trip(request: TripRequest):
    print(request)
    return {"description": "test"}
