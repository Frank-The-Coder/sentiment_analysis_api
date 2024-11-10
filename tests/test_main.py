# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] in ["POSITIVE", "NEGATIVE"]

def test_predict_empty():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
