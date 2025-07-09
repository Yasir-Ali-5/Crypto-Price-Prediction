# Crypto-Price-Prediction
A machine learning-powered web API built using FastAPI to predict the closing price of a cryptocurrency based on its open, high, and low prices.

It includes:

A trained model using 1-year crypto price data.

A RESTful API endpoint to get predictions.

A minimal HTML frontend to test predictions manually.

📖 Project Overview
This project solves a real-world use case: predicting the close price of a cryptocurrency using just the Open, High, and Low values of the same day.

✅ Use Cases
Financial forecasting

Trading strategy simulation

Integration into crypto dashboards or bots

🧠 How it Works
A scikit-learn model is pre-trained and saved using joblib.

The FastAPI backend receives price data via a POST request.

The API uses the model to predict the closing price.

The result is returned as a JSON response or shown in the frontend.

📁 Project Structure
php
Copy
Edit
crypto-price-predictor/
│
├── main.py                  # FastAPI backend app
│
├── models/
│   └── crypto_1Y.pkl        # Pre-trained machine learning model
│
├── static/
│   └── index.html           # Simple frontend for predictions
│
├── requirements.txt         # Required Python libraries
│
└── README.md                # You are here!
🔧 Installation & Setup
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/crypto-price-predictor.git
cd crypto-price-predictor
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the FastAPI app
bash
Copy
Edit
uvicorn main:app --reload
Visit: http://127.0.0.1:8000

🌐 API Documentation
FastAPI automatically generates interactive API docs at:

🔍 Swagger UI: http://127.0.0.1:8000/docs

📘 ReDoc: http://127.0.0.1:8000/redoc

🛠️ API Endpoints
GET /
Serves the static HTML file (index.html) from the static/ folder.

🔹 Response:
An HTML page with a form to submit Open, High, and Low values.

POST /predict
Predicts the close price based on input data.

🔹 Input JSON:
json
Copy
Edit
{
  "open": 28000,
  "high": 28500,
  "low": 27500
}
🔹 Output JSON:
json
Copy
Edit
{
  "predicted_close": 28120.47
}
🔹 Python Class Used:
python
Copy
Edit
class PriceInput(BaseModel):
    open: float
    high: float
    low: float
🧪 Sample cURL Request
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"open": 28000, "high": 28500, "low": 27500}'
📦 Requirements
requirements.txt
txt
Copy
Edit
fastapi
uvicorn
pydantic
numpy
joblib
Install with:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Deployment Suggestions
You can deploy this project to:

🔹 Render.com, Railway, or Deta

🔹 Docker container

🔹 AWS EC2 / Lightsail, VPS, or GCP Cloud Run

Let me know if you want a Dockerfile, Render deployment guide, or API key protection.

📄 License
This project is under the MIT License — free to use and modify.

👨‍💻 Author
Yasir Ali
