# Sentiment Analysis API

This project is a sentiment analysis API built with FastAPI, containerized with Docker, and deployed on both **Google Cloud Run** and **Google Kubernetes Engine (GKE)**. It uses a pre-trained `DistilBERT` model from Hugging Face's Transformers library to analyze the sentiment of text inputs.

## Project Overview

The Sentiment Analysis API allows users to submit text and receive a sentiment prediction. It demonstrates the use of FastAPI for building RESTful APIs, Docker for containerization, and deployment on both Google Cloud Run and Kubernetes.

## Features

- **Predict Sentiment**: Classifies input text as positive, neutral, or negative sentiment.
- **Scalable Deployment**: Deployed on both Google Cloud Run and Google Kubernetes Engine (GKE), supporting auto-scaling based on traffic.
- **Cost-Effective**: Cloud Run scales to zero when idle, minimizing costs. GKE provides flexible scaling options with high availability.

## Endpoints

### POST `/predict`

Predicts the sentiment of the provided text.

- **URLs**:
  - **Google Cloud Run**: `https://sentiment-analysis-api-469205853326.us-central1.run.app/predict`
  - **Google Kubernetes Engine**: `http://34.71.154.204/predict`
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
    "score": 0.9995
  }
  ```

### Accessing the API

#### Google Cloud Run Access

- Access the API on Cloud Run using:

```bash
curl -X POST "https://sentiment-analysis-api-469205853326.us-central1.run.app/predict" -H "Content-Type: application/json" -d "{\"text\": \"Hello, I went to Disneyland today!\"}"
```

#### Google Kubernetes Engine Access

- Access the API on GKE using:

```bash
curl -X POST "http://34.71.154.204/predict" -H "Content-Type: application/json" -d "{\"text\": \"Hello, I went to Disneyland today!\"}"
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker

### Local Setup

1. **Clone the Repository** and navigate into the project folder.
2. **Set up a Virtual Environment** and install dependencies listed in `requirements.txt`.
3. **Run the API Locally**: Start the FastAPI server using Uvicorn on `localhost`, accessible at `http://localhost:8000/predict`.

### Docker Deployment

1. **Build the Docker Image**:
   ```bash
   docker build -t sentiment-analysis-api .
   ```
2. **Run the Docker container locally**:

   ```bash
   docker run -p 8000:8000 sentiment-analysis-api
   ```

3. **Push the Image to Google Container Registry** if deploying to Google Cloud Run or GKE:
   ```bash
   docker tag sentiment-analysis-api gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api
   docker push gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api
   ```

### Google Cloud Run Deployment

1. **Deploy to Google Cloud Run**:

   ```bash
   gcloud run deploy sentiment-analysis-api \
     --image gcr.io/sentiment-analysis-api-441320/sentiment-analysis-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --memory 1Gi \
     --timeout 300
   ```

   Google Cloud Run will provide the public URL where your API is accessible.

### Kubernetes Deployment on Google Kubernetes Engine (GKE)

1. **Create a Kubernetes Cluster** on GKE:

   ```bash
   gcloud container clusters create sentiment-cluster --num-nodes=1 --region us-central1
   ```

2. **Apply Kubernetes Configurations**:

   - Use a `Deployment` configuration to manage your API container, specifying the Docker image and replica count.
   - Use a `Service` configuration of type `LoadBalancer` to expose the API externally with an IP.

3. **Get the External IP**:
   - The GKE service is accessible at `http://34.71.154.204/predict`.

## Technologies Used

- **FastAPI** - Framework for building APIs in Python
- **Docker** - Containerization for deployment
- **Google Cloud Run** - Serverless deployment for containerized applications
- **Google Kubernetes Engine (GKE)** - Managed Kubernetes for scalable containerized deployments
- **Hugging Face Transformers** - Pre-trained NLP models

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
