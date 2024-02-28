from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

load_dotenv()

app = FastAPI()
ui_path = Path("C:/Users/georg/VScode programs/wwwroot/")
app.mount("/ui", StaticFiles(directory=ui_path), name="ui")

"""
import openai
from openai import OpenAI
# Set up OpenAI API credentials
openai.api_type = "azure"
openai.api_base = "https://oai-genai-case.openai.azure.com/"
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
"""
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}

class ChatRequest(BaseModel):
    model: str = "gpt-4"
    messages: List[dict]
    #prompt:str
    
@app.post("/chat")
async def generate_chat(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
        model=request.model,
        messages=request.messages,
        max_tokens=100,
        temperature=0.8
)
        return {"response": completion.choices[0].message}#completion["choices"][0]["text"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#expose ton fakelo me to ui


class PromptRequest(BaseModel):
    model: str = "gpt-4"
    prompt:str
    
@app.post("/prompt")
async def generate_chat_2(request: PromptRequest):
    try:
        completion = client.chat.completions.create(
        model="gpt-4",
        messages =  [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": request.prompt}
    ],
        max_tokens=100,
        temperature=0.8
)
        return {"response": completion.choices[0].message}#completion["choices"][0]["text"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))