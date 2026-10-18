from fastapi import FastAPI
from pydantic import BaseModel
from inference import load_model, predict as inf_predict

app = FastAPI()

model = load_model()


class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictResponse(BaseModel):
    prediction: str


@app.get("/")
def welcome_root():
    return {"message": "asdf"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = inf_predict(model, request.model_dump())
    return PredictResponse(prediction=prediction)
