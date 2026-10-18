import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    # wczytanie danych
    iris = load_iris()
    x = iris.data
    y = iris.target
    return x, y


def train_model(x, y):
    # trening
    model = LogisticRegression(max_iter=200)
    model.fit(x, y)
    return model


def save_model(model, filepath: str = "model.joblib") -> None:
    # zapis modelu
    joblib.dump(model, filepath)
    print(f"Model zapisany w: {filepath}")


if __name__ == "__main__":
    x, y = load_data()
    model = train_model(x, y)
    save_model(model)
