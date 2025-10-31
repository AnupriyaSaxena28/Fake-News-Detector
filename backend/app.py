# app.py — Flask API
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from utils import clean_text, extract_text_from_url

app = Flask(__name__)
CORS(app)

MODEL_PATH = os.path.join('model', 'model.pkl')
VEC_PATH = os.path.join('model', 'vectorizer.pkl')

if not os.path.exists(MODEL_PATH) or not os.path.exists(VEC_PATH):
    print('WARNING: model files not found in backend/model/. Run train.py or add model.pkl and vectorizer.pkl')

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VEC_PATH)
    print('Model loaded')
except Exception as e:
    model = None
    vectorizer = None
    print('Model load error:', e)

@app.route('/')
def home():
    return jsonify({'status': 'ok', 'message': 'Fake News Detector API'})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not found. Train model or place model files in backend/model/'}), 500
    data = request.get_json(force=True)
    text = data.get('text', '')
    url = data.get('url', '')
    if url and not text:
        text = extract_text_from_url(url)
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    proba = None
    try:
        if hasattr(model, 'predict_proba'):
            proba = float(model.predict_proba(vec)[0].max())
    except Exception:
        proba = None
    label = 'Real' if int(pred) == 1 else 'Fake'
    return jsonify({'prediction': label, 'confidence': proba})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
