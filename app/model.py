# app/model.py
from transformers import pipeline
from app.config import MODEL_NAME

# Load the model and create a pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)


def predict_sentiment(text):
    """
    Predicts the sentiment of the provided text.
    Returns a dictionary with the label and score.
    """
    result = sentiment_pipeline(text)
    return result[0]
