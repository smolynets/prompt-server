import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from app.gemini import get_gemini_response

API_TOKEN = os.getenv("API_TOKEN", "changeme")

security = HTTPBearer()

app = FastAPI()


class Item(BaseModel):
    prompt: str


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return True


@app.get("/health_check")
def read_root(authorized: bool = Depends(verify_token)):
    return {"message": "working fine!"}


@app.post("/")
async def ask_llm(
    requrest: Item, authorized: bool = Depends(verify_token)
):
    return get_gemini_response(requrest.prompt)
