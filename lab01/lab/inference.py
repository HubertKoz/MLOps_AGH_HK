import joblib

TARGET_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(filepath: str = "model.joblib"):
    # ładuje model
    return joblib.load(filepath)


def predict(model, data: dict) -> str:
    # predykcja
    features = [
        [
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
        ]
    ]
    prediction_index = int(model.predict(features)[0])
    return TARGET_NAMES[prediction_index]
