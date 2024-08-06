# MLOPS_Group12_Assignment_1
This Repository is used for working on foundation, process, tooling, model experimentation, packing, deployment, and orchestration.

# Project Title: MLOPS Tools and Procedure 

## M1 - MLOPS Foundation

### Description
This project develops a predictive model for housing prices based on features such as size, number of rooms, and location. It includes model training, hyperparameter tuning using Optuna, and a Flask application to serve the model predictions.

### System Requirements
1. Python 3.8+
2. pip (Python package installer)

### Installation

#### Clone the Repository
To get started, clone this repository to your local machine:
```sh
git clone https://github.com/vishnuc999/MLOps_Group12_Assignment1.git
cd MLOps_Group12_Assignment1
```

#### Install Dependencies
Install the required Python packages from requirements.txt:
```sh
pip install -r requirements.txt
```

#### Configuration

##### Environment Variables
Set necessary environment variables:
```sh
export FLASK_APP=app.py
export FLASK_ENV=development
```

### Usage

#### Training the Model
To train the model and perform hyperparameter tuning:
```sh
python train_model.py
```

### Starting the Flask Server
To start the Flask application to serve predictions:
```sh
flask run
```

This will start the server on http://localhost:5000 where you can send POST requests to /predict.

### Testing

#### Run Tests
Execute unit tests using:
```sh
pytest
```

### Additional Tools

#### Linting
Run Flake8 to check for style and programming errors:
```sh
flake8 .
```

#### Experiment Tracking
Access MLflow UI to view experiment results:
```sh
mlflow ui
```

### Files in the Repository
1. **train_model.py**: Script for training and tuning the machine learning model.
2. **app.py**: Flask application for serving the model predictions.
3. **requirements.txt**: List of dependencies.
4. **tests/**: Directory containing test scripts for the application.


## M2 - Process and Tooling

### Overview
This project demonstrates how to:
1. Use MLflow to track experiments for a machine learning project.
2. Record metrics, parameters, and results of at least three different model training runs.
3. Use DVC (Data Version Control) to version control a dataset used in the project.
4. Show how to revert to a previous version of the dataset.

### Setup

#### Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- pip
- Git
- DVC

#### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd project
    ```

2. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Initialize DVC:
    ```sh
    dvc init
    ```

4. Add the dataset to DVC:
    ```sh
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc .gitignore
    git commit -m "Add Olympic results dataset"
    ```

### Running Experiments with MLflow

1. **Experiment Tracking Script**
    The `track_experiments.py` script logs experiments using MLflow, including recording metrics and parameters.

2. **Run the Experiment Tracking Script**
    Execute the script to log three different model training runs:
    ```sh
    python experiments/track_experiments.py
    ```

3. **View MLflow UI**
    Start the MLflow UI to view the experiment logs:
    ```sh
    mlflow ui
    ```
    Navigate to `http://localhost:5000` in your web browser to see the tracked experiments.

### Data Versioning with DVC

1. **Initialize DVC**
    Initialize DVC in your project directory (already done in setup):
    ```sh
    dvc init
    ```

2. **Track the Dataset**
    Add your `olympic_results.csv` dataset to DVC (already done in setup):
    ```sh
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc .gitignore
    git commit -m "Add Olympic results dataset"
    ```

3. **Make Changes and Track Versions**
    Make changes to your dataset and track the new version:
    ```sh
    # Make some changes to data/olympic_results.csv
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc
    git commit -m "Update Olympic results dataset"
    ```

4. **Revert to a Previous Version**
    To revert to a previous version of the dataset:
    ```sh
    git checkout <commit_id>
    dvc checkout
    ```

### Deliverables

1. **MLflow Experiment Logs**
    The experiment logs can be viewed in the MLflow UI, showing the results of different model training runs.

2. **DVC Repository**
    The DVC repository tracks the dataset with different versions, demonstrating the ability to revert to previous versions.

### Summary
By following these steps, we have successfully:
- Set up MLflow to track experiments, including metrics, parameters, and results of multiple model training runs.
- Used DVC to version control the dataset, with the ability to revert to previous versions.

---

## M3 - Model Experimentation and Packaging

### Objective
Train a machine learning model, perform hyperparameter tuning, and package the model for deployment.

### Tasks

#### 1. Hyperparameter Tuning
- **Tool Used**: Scikit-learn’s GridSearchCV
- **Model**: RandomForestClassifier
- **Dataset**: Iris dataset
- **Parameter Grid**: Various values for `n_estimators`, `max_depth`, `min_samples_split`, and `min_samples_leaf`
- **Best Parameters Found**:
  - `max_depth`: 10
  - `min_samples_leaf`: 1
  - `min_samples_split`: 2
  - `n_estimators`: 100

#### 2. Model Packaging
- **Tools Used**: Docker and Flask
- **Dockerfile**: Created to set up the environment and run the Flask application
- **Flask Application**: Created to serve the model and provide predictions via a REST API

### Deliverables

#### 1. Report on Hyperparameter Tuning Results
The hyperparameter tuning was performed using Scikit-learn’s GridSearchCV on the RandomForestClassifier model using the Iris dataset. The best parameters found were:
- `max_depth`: 10
- `min_samples_leaf`: 1
- `min_samples_split`: 2
- `n_estimators`: 100

#### 2. Dockerfile and Flask Application Code
The Dockerfile and Flask application were created to package the best-performing model and serve it via a REST API. The Flask application provides predictions along with additional information such as class probabilities, model parameters, and a timestamp.

##### File Names
- `Dockerfile`
- `app.py`
- `requirements.txt`
- `grid_search.py`
- `model.joblib`
- `test_file.py`

### Running the Application

#### Prerequisites
- Docker installed on your machine

#### Steps to Run the Application

1. **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd my-ml-model
    ```

2. **Build the Docker Image**
    ```sh
    docker build -t mlops_group12_assignment1 .
    ```

3. **Run the Docker Container**
    ```sh
    docker run -p 5000:5000 mlops_group12_assignment1
    ```

4. **Test the Flask Application**
    Use `curl` to send a POST request to the `/predict` endpoint with JSON data:
    ```sh
    curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"input": [5.1, 3.5, 1.4, 0.2]}'
    ```

5. **Expected JSON Response**
    ```json
    {
        "input": [5.1, 3.5, 1.4, 0.2],
        "prediction": 0,
        "predicted_class": "Setosa",
        "probabilities": {
            "Setosa": 1.0,
            "Versicolor": 0.0,
            "Virginica": 0.0
        },
        "model_parameters": {
            "bootstrap": true,
            "ccp_alpha": 0.0,
            "class_weight": null,
            "criterion": "gini",
            "max_depth": 10,
            "max_features": "sqrt",
            "max_leaf_nodes": null,
            "max_samples": null,
            "min_impurity_decrease": 0.0,
            "min_samples_leaf": 1,
            "min_samples_split": 2,
            "min_weight_fraction_leaf": 0.0,
            "monotonic_cst": null,
            "n_estimators": 100,
            "n_jobs": null,
            "oob_score": false,
            "random_state": null,
            "verbose": 0,
            "warm_start": false
        },
        "timestamp": "2024-08-06T04:56:39.641470"
    }
    ```

### Conclusion
All tasks have been completed successfully. The machine learning model has been trained, hyperparameter tuned, and packaged using Docker and Flask for deployment. The model can be served via a REST API and returns comprehensive prediction results.
```