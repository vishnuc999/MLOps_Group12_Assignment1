import mlflow
import pandas as pd
import re


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def analyze_data(data):
    event_counts = data['event_title'].value_counts()
    return event_counts


def sanitize_name(name):
    # Replace invalid characters with underscores
    sanitized_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', name)
    return sanitized_name


def main():
    mlflow.start_run()

    # Load data
    data = load_data('data/olympic_results.csv')

    # Analyze data
    event_counts = analyze_data(data)

    # Log analysis results
    mlflow.log_param("dataset", "olympic_results.csv")
    for event, count in event_counts.items():
        sanitized_event = sanitize_name(event)
        mlflow.log_metric(sanitized_event, count)

    mlflow.end_run()


if __name__ == "__main__":
    main()
