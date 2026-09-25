from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel


class GenerateRequest(BaseModel):
    text: str

def generate_response(text: str):
    return "Artificial Intelligence (AI) is a technology that enables computers to perform tasks that normally require human intelligence, such as understanding language, recognizing images, and making decisions."

@app.post("/generate")
def generate(request: GenerateRequest):
    response = generate_response(request.text)

    return {
        "input": request.text,
        "response": response
    }


