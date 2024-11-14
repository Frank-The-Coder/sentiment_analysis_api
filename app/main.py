import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_sentiment
from app.preprocess import clean_text


app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


@app.post("/predict")
async def predict(request: SentimentRequest):
    clean_text_input = clean_text(request.text)
    if not clean_text_input:
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    result = predict_sentiment(clean_text_input)
    return result


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
