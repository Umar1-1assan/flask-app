# backend/app/app.py
from flask import Flask, request, jsonify
from predictor import moving_average_predict

app = Flask(__name__)

# In real app read from MySQL. For demo use a simple in-memory dataset.
demo_prices = {
    "AAPL": [170.0, 171.5, 169.8, 172.3, 173.0],
    "MSFT": [300.0, 301.2, 299.0, 302.0, 303.5]
}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json() or {}
    ticker = data.get("ticker")
    window = int(data.get("window", 3))
    if ticker is None:
        return jsonify({"error":"ticker required"}), 400
    prices = demo_prices.get(ticker)
    if not prices or len(prices) < window:
        return jsonify({"error":"insufficient data"}), 400
    pred = moving_average_predict(prices, window)
    return jsonify({"ticker": ticker, "prediction": float(pred)})

