from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('Rock_vs_Mine.joblib')

# Load sonar dataset for reference
sonar_data = pd.read_csv('sonar.csv', header=None)
X = sonar_data.drop(columns=60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        input_data = request.form.getlist('input_data[]')
        
        # Convert input data to numpy array and reshape it
        input_data_as_array = np.asarray(input_data, dtype=np.float64)
        arr_reshaped = input_data_as_array.reshape(1, -1)
        
        # Perform the prediction
        prediction = model.predict(arr_reshaped)
        
        # Return the result to the frontend
        return jsonify({'prediction': str(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
