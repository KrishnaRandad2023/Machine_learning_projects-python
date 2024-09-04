from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('music-recommender.joblib')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data['age']
    gender = data['gender']

    # Make prediction using the model
    prediction = model.predict([[age, gender]])

    # Return the result as JSON
    return jsonify({'genre': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
