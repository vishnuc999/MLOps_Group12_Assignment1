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


# ML Experiment Tracking and Data Versioning

## Overview

This project demonstrates how to:
1. Use MLflow to track experiments for a machine learning project.
2. Record metrics, parameters, and results of at least three different model training runs.
3. Use DVC (Data Version Control) to version control a dataset used in the project.
4. Show how to revert to a previous version of the dataset.

## Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip
- Git
- DVC

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd project
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Initialize DVC:
    ```bash
    dvc init
    ```

4. Add the dataset to DVC:
    ```bash
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc .gitignore
    git commit -m "Add Olympic results dataset"
    ```

## Running Experiments with MLflow

1. **Experiment Tracking Script**

    The `track_experiments.py` script logs experiments using MLflow, including recording metrics and parameters.

2. **Run the Experiment Tracking Script**

    Execute the script to log three different model training runs:
    ```bash
    python experiments/track_experiments.py
    ```

3. **View MLflow UI**

    Start the MLflow UI to view the experiment logs:
    ```bash
    mlflow ui
    ```
    Navigate to `http://localhost:5000` in your web browser to see the tracked experiments.

## Data Versioning with DVC

1. **Initialize DVC**

    Initialize DVC in your project directory (already done in setup):
    ```bash
    dvc init
    ```

2. **Track the Dataset**

    Add your `olympic_results.csv` dataset to DVC (already done in setup):
    ```bash
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc .gitignore
    git commit -m "Add Olympic results dataset"
    ```

3. **Make Changes and Track Versions**

    Make changes to your dataset and track the new version:
    ```bash
    # Make some changes to data/olympic_results.csv
    dvc add data/olympic_results.csv
    git add data/olympic_results.csv.dvc
    git commit -m "Update Olympic results dataset"
    ```

4. **Revert to a Previous Version**

    To revert to a previous version of the dataset:
    ```bash
    git checkout <commit_id>
    dvc checkout
    ```

## Deliverables

1. **MLflow Experiment Logs**

    The experiment logs can be viewed in the MLflow UI, showing the results of different model training runs.

2. **DVC Repository**

    The DVC repository tracks the dataset with different versions, demonstrating the ability to revert to previous versions.

### Summary

By following these steps, we have successfully:
- Set up MLflow to track experiments, including metrics, parameters, and results of multiple model training runs.
- Used DVC to version control the dataset, with the ability to revert to previous versions.

