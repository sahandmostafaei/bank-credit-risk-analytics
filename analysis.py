"""
Credit Risk Analysis Module
Author: Sahand Mostafaei
"""

import pandas as pd


def load_data(filepath):
    """Load the dataset."""
    return pd.read_csv(filepath)


def dataset_summary(df):
    print("\n==============================")
    print("DATASET SUMMARY")
    print("==============================")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nSummary Statistics")
    print(df.describe(include="all"))


def default_rate(df):
    """Calculate default rate if a target column exists."""
    target_columns = [
        "loan_status",
        "Loan_Status",
        "default",
        "Default",
        "cb_person_default_on_file"
    ]

    for col in target_columns:
        if col in df.columns:
            print("\n==============================")
            print("DEFAULT ANALYSIS")
            print("==============================")
            print(df[col].value_counts())
            print("\nPercentage")
            print(df[col].value_counts(normalize=True) * 100)
            return

    print("\nDefault column not found.")


def loan_statistics(df):

    print("\n==============================")
    print("NUMERIC FEATURES")
    print("==============================")

    numeric = df.select_dtypes(include="number")

    for column in numeric.columns:
        print(f"\n{column}")
        print(f"Mean   : {numeric[column].mean():.2f}")
        print(f"Median : {numeric[column].median():.2f}")
        print(f"Min    : {numeric[column].min():.2f}")
        print(f"Max    : {numeric[column].max():.2f}")


def correlation_matrix(df):

    print("\n==============================")
    print("CORRELATION MATRIX")
    print("==============================")

    numeric = df.select_dtypes(include="number")

    print(numeric.corr().round(2))
