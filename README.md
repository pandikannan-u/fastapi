# GenAI Day 1 - FastAPI AI API

## Description

This project demonstrates how an AI capability can be exposed through a REST API using FastAPI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## API Endpoint

### POST /generate

The `/generate` endpoint accepts a text input and returns a response in JSON format.

## How It Works

1. The user sends a text input to the `/generate` endpoint.
2. FastAPI receives the request.
3. The Python function processes the input.
4. The API returns the response as JSON.

## Example Request

```json
{
  "text": "Explain artificial intelligence in simple terms"
}
