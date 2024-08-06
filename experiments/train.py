import mlflow.sklearn
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load dataset
data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Parameters for experiment tracking
parameters = [
    {"n_estimators": 100, "max_depth": 3},
    {"n_estimators": 200, "max_depth": 5},
    {"n_estimators": 150, "max_depth": 4},
]

for params in parameters:
    with mlflow.start_run():
        # Train model
        model = RandomForestRegressor(n_estimators=params["n_estimators"], max_depth=params["max_depth"])
        model.fit(X_train, y_train)

        # Predict and evaluate
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # Log parameters and metrics
        mlflow.log_param("n_estimators", params["n_estimators"])
        mlflow.log_param("max_depth", params["max_depth"])
        mlflow.log
