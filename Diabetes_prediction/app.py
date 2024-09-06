from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

# Load the trained model
model = joblib.load('Daibetes_detection.joblib')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['input']
    input_data = np.asarray(input_data).reshape(1, -1)
    
    prediction = model.predict(input_data)
    result = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'
    
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
