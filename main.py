import pandas as pd

from analysis import (
    load_data,
    dataset_summary,
    default_rate,
    numeric_summary,
)

DATA_PATH = "data/credit_data.csv"


def main():

    print("="*60)
    print("BANK CREDIT RISK ANALYTICS")
    print("="*60)

    df = load_data(DATA_PATH)

    dataset_summary(df)

    default_rate(df)

    numeric_summary(df)

    print("\nAnalysis Complete.")


if __name__ == "__main__":
    main()
