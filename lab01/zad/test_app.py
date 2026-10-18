from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    # test endpointu root
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "asdf"}


def test_health():
    # test health checka
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_ok():
    # test poprawnego zapytania
    response = client.post(
        "/predict", json={"text": "What a great MLOps lecture, I am very satisfied"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_predict_empty():
    # test walidacji dla pustego tekstu
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422


def test_predict_invalid():
    # test niepoprawnego formatu
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_predict_samples():
    # test przykładowych tekstów
    for text in ["fajne buty", "normalna pizza", "słaby kawałek"]:
        response = client.post("/predict", json={"text": text})
        assert response.status_code == 200
        assert response.json()["prediction"] in ["positive", "neutral", "negative"]
