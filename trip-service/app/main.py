from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/communicate")
def health():
    x = requests.get('http://ai-service:8000/health')
    print(x.text)
    return {"status": x.text}
