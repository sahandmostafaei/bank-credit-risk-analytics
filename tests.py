"""
Basic tests for Bank Credit Risk Analytics
"""

from analysis import load_data

DATA_PATH = "data/credit_data.csv"


def test_dataset_load():

    df = load_data(DATA_PATH)

    assert len(df) > 0

    assert len(df.columns) > 0

    print("Dataset loaded successfully.")


if __name__ == "__main__":
    test_dataset_load()
