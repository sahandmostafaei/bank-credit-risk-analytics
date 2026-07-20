"""
Credit Risk Analysis Module

Author: Sahand Mostafaei
"""

import pandas as pd


def load_data(filepath):
    """Load credit risk dataset."""
    return pd.read_csv(filepath)


def summarize_data(df):
    """Return summary statistics."""
    return df.describe()


def missing_values(df):
    """Return missing value counts."""
    return df.isnull().sum()


if __name__ == "__main__":
    print("Credit Risk Analysis Module Ready")
