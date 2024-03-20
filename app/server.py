# app/server.py

from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('trained_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return 'Welcome to the Flask app!'


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [data['features']]
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
