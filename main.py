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

DATA_PATH = "data/credit_data.csv"


def main():

    print("=" * 60)
    print("BANK CREDIT RISK ANALYTICS")
    print("=" * 60)

    # Load dataset
    df = load_data(DATA_PATH)

    # Exploratory Data Analysis
    dataset_summary(df)

    # Credit risk statistics
    default_rate(df)

    loan_statistics(df)

    correlation_matrix(df)

    # Predictive model
    train_model(df)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
