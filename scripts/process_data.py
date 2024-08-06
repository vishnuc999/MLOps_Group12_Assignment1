import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def main():
    data = load_data('data/olympic_results.csv')
    print(data.head())


if __name__ == "__main__":
    main()
