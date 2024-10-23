import requests
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/ask")
def ask(prompt: str) -> Response:
    res = requests.post(
        "http://ollama:11434/api/generate",
        json={"prompt": prompt, "stream": False, "model": "llama3.2:1b"},
    )

    return Response(content=res.text, media_type="application/json")
