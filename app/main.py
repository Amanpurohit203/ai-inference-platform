from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="ML Inference Platform", version="1.0")

# Load the model once at startup, not per-request
sentiment_model = pipeline("sentiment-analysis")


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    label: str
    score: float


@app.get("/health")
def health_check():
    """Used by Kubernetes liveness/readiness probes later."""
    return {"status": "healthy"}


@app.post("/sentiment", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    result = sentiment_model(request.text)[0]
    return SentimentResponse(label=result["label"], score=result["score"])