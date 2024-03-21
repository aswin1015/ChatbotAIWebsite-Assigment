from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
from fastapi.responses import HTMLResponse
import os
import time 
import google.generativeai as genai
from IPython.display import Markdown

gemini_api_key = "AIzaSyC7CeQMX_MxSauwtwfGLN1mwuKpvBRhqT4"
genai.configure(api_key = gemini_api_key)

# Load environment variables from .env file (if any)
load_dotenv()

class Response(BaseModel):
    result: str | None

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict", response_class=HTMLResponse)
def predict(param1: str = None) -> Any:
    if not param1:
        return {"error": "param1 must not be empty"}
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(param1)

    content = f"""
    <html>
        <body>
            <h1>Hello, world!</h1>
            <p>param1: {response.text}</p>
        </body>
    </html>
    """
    return content