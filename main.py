"""
Bank Credit Risk Analytics
Author: Sahand Mostafaei
"""

import pandas as pd

DATA_PATH = "data/credit_data.csv"


def main():
    print("=" * 60)
    print("BANK CREDIT RISK ANALYTICS")
    print("=" * 60)

    try:
        df = pd.read_csv(DATA_PATH)

        print("\nDataset loaded successfully.")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")

        print("\nColumns")
        print(df.columns.tolist())

        print("\nFirst five rows")
        print(df.head())

        print("\nSummary Statistics")
        print(df.describe(include="all"))

        print("\nMissing Values")
        print(df.isnull().sum())

    except FileNotFoundError:
        print("Dataset not found.")
        print("Expected location:", DATA_PATH)


if __name__ == "__main__":
    main()
