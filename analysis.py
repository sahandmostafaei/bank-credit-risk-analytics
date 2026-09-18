"""
Credit Risk Analysis Module
Author: Sahand Mostafaei
"""

import pandas as pd


def load_data(filepath):
    """Load the credit-risk dataset."""
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
    """
    Calculate the observed loan-default rate.

    The primary target is `loan_status`.
    `cb_person_default_on_file` is treated as a historical
    borrower characteristic and is not used as the target.
    """

    if "loan_status" not in df.columns:
        print("\nTarget column 'loan_status' not found.")
        return

    print("\n==============================")
    print("DEFAULT ANALYSIS")
    print("==============================")

    counts = df["loan_status"].value_counts()

    print("\nLoan Status Counts")
    print(counts)

    print("\nLoan Status Percentages")
    print(counts / len(df) * 100)


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
