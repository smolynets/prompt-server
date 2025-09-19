from fastapi import FastAPI

from app.gemini import get_gemini_response

app = FastAPI()

@app.get("/health_check")
def read_root():
    return {"message": "working fine!"}


@app.post("/")
async def ask_llm(
    prompt: str
):
    return get_gemini_response(prompt)
