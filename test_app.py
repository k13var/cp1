from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_welcome():
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"Message": "Bonjour, ceci est la beta d'un algorithme d'analyse de sentiment"}


def test_sentiment_bad_token():
    response = client.post("/sentiment", headers={"token": "bad token"}, json={"text": "sample text"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Token invalide!"}


def test_sentiment_prediction():
    response = client.post("/sentiment", headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"},
                           json={"text": "très bien"})
    assert response.status_code == 200
    assert response.json() == {"text": "très bien", "sentiment": "Positif"}
