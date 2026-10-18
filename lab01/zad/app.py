from fastapi import FastAPI
from pydantic import BaseModel, Field
from inference import load_model, predict as inf_predict

app = FastAPI()

try:
    model = load_model()
except Exception:
    model = None


class PredictRequest(BaseModel):
    text: str = Field(min_length=1)


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
    prediction = inf_predict(model, request.text)
    return PredictResponse(prediction=prediction)
