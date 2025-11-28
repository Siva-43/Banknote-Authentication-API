Banknote Authentication API (FastAPI)

This project is a machine learning API built using FastAPI to predict whether a banknote is authentic or fake using variance, skewness, curtosis, and entropy.

🚀 Features

     --FastAPI machine learning prediction API

     --Trained model (model.pkl)

     --/predict POST endpoint

     --Example usage with JSON

     --Lightweight and fast

📂 Project Structure
├── main.py
├── model.pkl
├── BankNote_Authentication.csv
├── model.ipynb
├── requirements.txt
└── README.md

⚙️ How to Run Locally

1️⃣ Install dependencies

   pip install -r requirements.txt

2️⃣ Start the FastAPI server

   uvicorn main:app --reload

3️⃣ Open your browser

   http://127.0.0.1:8000/docs


This opens the interactive Swagger UI where you can test the API.

📌 API Endpoint
POST /predict
Sample Request:
{
  "variance": 2.3,
  "skewness": 6.7,
  "curtosis": -1.2,
  "entropy": 0.9
}

Sample Response:
{
  "prediction": "Fake note"
}

🧠 Model

The model was trained using the Banknote Authentication dataset and saved as model.pkl. The FastAPI loads and uses it to make predictions.
