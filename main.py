from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Serve static files (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the trained model (adjust path as needed)
model = joblib.load("models\crypto_1Y.pkl")

# Define input schema
class PriceInput(BaseModel):
    open: float
    high: float
    low: float

# Home route (serves index.html)
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r") as file:
        html = file.read()
    return HTMLResponse(content=html, status_code=200)

# Prediction route
@app.post("/predict")
async def predict_price(data: PriceInput):
    input_array = np.array([[data.open, data.high, data.low]])
    predicted = model.predict(input_array)[0]
    return JSONResponse({"predicted_close": round(predicted, 2)})
