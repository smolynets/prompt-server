import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.gemini import get_gemini_response

API_TOKEN = os.getenv("API_TOKEN", "changeme")

security = HTTPBearer()

app = FastAPI()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return True


@app.get("/health_check")
def read_root(authorized: bool = Depends(verify_token)):
    return {"message": "working fine!"}


@app.post("/")
async def ask_llm(
    prompt: str, authorized: bool = Depends(verify_token)
):
    return get_gemini_response(prompt)
