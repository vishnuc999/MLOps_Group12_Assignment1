from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

# Define the class names (adjust these based on your model)
class_names = ['Setosa', 'Versicolor', 'Virginica']


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)[0]
    predicted_class = class_names[prediction[0]]

    response = {
        'input': data['input'],
        'prediction': int(prediction[0]),
        'predicted_class': predicted_class,
        'probabilities': {class_name: float(prob) for class_name, prob in zip(class_names, probabilities)},
        'model_parameters': model.get_params(),
        'timestamp': datetime.now().isoformat()
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
