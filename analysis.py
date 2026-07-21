"""
Credit Risk Analysis Module
Author: Sahand Mostafaei
"""

import pandas as pd


def load_data(filepath):
    return pd.read_csv(filepath)


def dataset_summary(df):
    print("\nDataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nSummary Statistics")
    print(df.describe(include="all"))

    print("\nMissing Values")
    print(df.isnull().sum())


def default_rate(df):
    for col in ["loan_status", "Loan_Status", "default", "Default"]:
        if col in df.columns:
            rate = df[col].value_counts(normalize=True) * 100
            print("\nDefault Rate (%)")
            print(rate)
            return

    print("\nNo default-status column found.")


def numeric_summary(df):
    print("\nAverage values")

    for col in df.select_dtypes(include="number").columns:
        print(f"{col}: {df[col].mean():.2f}")


if __name__ == "__main__":
    print("Credit Risk Analysis Module Ready")
