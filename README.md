# Sentiment Analysis API

This project is a sentiment analysis API built with FastAPI and deployed on Google Cloud Run. It uses a pre-trained `DistilBERT` model from Hugging Face's Transformers library to analyze the sentiment of text inputs.

## Project Overview

The Sentiment Analysis API allows users to submit text and receive a sentiment prediction based on the input text. This project demonstrates the use of FastAPI for building RESTful APIs, Docker for containerization, and Google Cloud Run for serverless deployment.

## Features

- **Predict Sentiment**: Classifies input text as positive, neutral, or negative sentiment.
- **Scalable Deployment**: Deployed on Google Cloud Run, it scales automatically based on traffic.
- **Cost-Effective**: Configured to scale to zero when idle, minimizing costs when the API is not in use.

## Endpoints

### POST `/predict`

Predicts the sentiment of the provided text.

- **URL**: `https://sentiment-analysis-api-469205853326.us-central1.run.app/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "text": "Hello, I went to Disneyland today!"
  }
  ```
- **Response**:
  ```json
  {
    "label": "POSITIVE",
    "score": 0.9995439648628235
  }
  ```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

To start the API locally:

1. **Run the API**:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

2. **Test the endpoint**:

   ```bash
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"text\": \"Hello, I went to Disneyland today!\"}"
   ```

   _Note_: You can replace `http://localhost:8000/predict` with `https://sentiment-analysis-api-469205853326.us-central1.run.app/predict` since the API has been deployed on Google Cloud Run.

### Docker Deployment

1. **Build the Docker image**:

   ```bash
   docker build -t sentiment-analysis-api .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 sentiment-analysis-api
   ```

### Google Cloud Run Deployment

1. **Push the Docker image to Google Container Registry**:

   ```bash
   docker tag sentiment-analysis-api gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api
   docker push gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api
   ```

2. **Deploy on Google Cloud Run**:
   ```bash
   gcloud run deploy sentiment-analysis-api \
     --image gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --memory 1Gi \
     --timeout 300
   ```

## Technologies Used

- **FastAPI** - Web framework for building APIs in Python
- **Docker** - Containerization for deployment
- **Google Cloud Run** - Serverless platform for containerized applications
- **Hugging Face Transformers** - Pre-trained NLP models

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
