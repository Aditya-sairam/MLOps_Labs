from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('/model/wine_model.pkl')
target_names = joblib.load('/model/target_names.pkl')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]
    prediction_name = target_names[prediction]
    
    return jsonify({
        "prediction": int(prediction),
        "wine_class": prediction_name
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)