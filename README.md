# MLOps_Group12_Assignment1
This Repository is used for working on foundation , process , tooling, model experimentation, packing, deployment and orchestration

## Project Title: Machine Learning Model for Predicting Housing Prices

### Description
This project develops a predictive model for housing prices based on features such as size, number of rooms, and location. It includes model training, hyperparameter tuning using Optuna, and a Flask application to serve the model predictions.

### System Requirements
1. Python 3.8+
2. pip (Python package installer)

### Installation
#### Clone the Repository
To get started, clone this repository to your local machine:
```
git clone https://github.com/vishnuc999/MLOps_Group12_Assignment1.git
cd MLOps_Group12_Assignment1
```

#### Install Dependencies
Install the required Python packages from requirements.txt:
```
pip install -r requirements.txt
```

#### Configuration
##### Environment Variables
Set necessary environment variables:
```
export FLASK_APP=app.py
export FLASK_ENV=development
```

### Usage
#### Training the Model
To train the model and perform hyperparameter tuning:
```
python train_model.py
```

### Starting the Flask Server
To start the Flask application to serve predictions:
```
flask run
```

This will start the server on http://localhost:5000 where you can send POST requests to /predict.

### Testing
#### Run Tests
Execute unit tests using:
```
pytest
```

### Additional Tools
### Linting
Run Flake8 to check for style and programming errors:
```
flake8 .
```

### Experiment Tracking
Access MLflow UI to view experiment results:
```
mlflow ui
```

### Files in the Repository
1. **train_model.py**: Script for training and tuning the machine learning model.
2. **app.py**: Flask application for serving the model predictions.
3. **requirements.txt**: List of dependencies.
4. **tests_ (or) _tests**: Directory containing test scripts for the application.