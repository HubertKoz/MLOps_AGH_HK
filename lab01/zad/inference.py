import os
from pathlib import Path
import urllib.request
import zipfile
from cleantext import clean
import joblib
from sentence_transformers import SentenceTransformer

TARGET_NAMES = ["negative", "neutral", "positive"]


def download_model():
    # pobiera i rozpakowuje model
    url = "https://drive.usercontent.google.com/download?id=1NRZdYq5jweVRUzAZG518LMhs4E56IgxG&export=download&confirm=t"
    urllib.request.urlretrieve(url, "model.zip")
    os.makedirs("models", exist_ok=True)
    with zipfile.ZipFile("model.zip", "r") as zip_ref:
        zip_ref.extractall("models")


def load_model(models_dir: str = "models"):
    # ładuje modele
    path = Path(models_dir)
    if not path.exists():
        download_model()

    # plik klasyfikatora
    clf_files = (
        list(path.glob("*.joblib"))
        + list(path.glob("*.pkl"))
        + list(path.glob("**/*.joblib"))
    )
    clf_path = clf_files[0] if clf_files else path / "model.joblib"

    # folder transformera
    transformer_dirs = [
        p for p in path.iterdir() if p.is_dir() and (p / "config.json").exists()
    ]
    transformer_path = (
        transformer_dirs[0]
        if transformer_dirs
        else (
            path if (path / "config.json").exists() else path / "sentence_transformer"
        )
    )

    transformer = SentenceTransformer(str(transformer_path))
    classifier = joblib.load(clf_path)
    return transformer, classifier


def predict(models, text: str) -> str:
    # predykcja
    transformer, classifier = models
    cleaned = clean(
        text, no_urls=True, no_emails=True, no_phone_numbers=True, lower=True
    )
    embeddings = transformer.encode([cleaned])
    pred = classifier.predict(embeddings)[0]
    return TARGET_NAMES[int(pred)]


if __name__ == "__main__":
    download_model()
