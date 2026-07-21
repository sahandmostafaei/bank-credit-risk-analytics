"""
Bank Credit Risk Analytics
Author: Sahand Mostafaei
"""

from analysis import (
    load_data,
    dataset_summary,
    default_rate,
    loan_statistics,
    correlation_matrix,
)

from model import train_model

from visualization import (
    save_histograms,
    save_missing_values,
)

DATA_PATH = "data/credit_data.csv"


def main():

    print("=" * 60)
    print("BANK CREDIT RISK ANALYTICS")
    print("=" * 60)

    df = load_data(DATA_PATH)

    dataset_summary(df)

    default_rate(df)

    loan_statistics(df)

    correlation_matrix(df)

    save_missing_values(df)

    save_histograms(df)

    train_model(df)

    print("\nFigures saved in the figures folder.")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
