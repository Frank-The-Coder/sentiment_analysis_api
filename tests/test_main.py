from fastapi.testclient import TestClient
from app.main import app  # Adjust import based on your project structure

client = TestClient(app)


def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] == "POSITIVE"
    assert isinstance(result["score"], float)  # Check score type


def test_predict_negative():
    response = client.post("/predict", json={"text": "This is terrible!"})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] == "NEGATIVE"
    assert isinstance(result["score"], float)


def test_predict_empty():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400  # Check for error on empty input
