"""
Visualization Module
Author: Sahand Mostafaei
"""

import matplotlib.pyplot as plt


def plot_missing_values(missing_values):
    plt.figure(figsize=(10,5))
    missing_values[missing_values > 0].plot(kind="bar")
    plt.title("Missing Values by Feature")
    plt.xlabel("Features")
    plt.ylabel("Missing Values")
    plt.tight_layout()
    plt.savefig("figures/missing_values.png")
    plt.close()


def plot_numeric_distributions(df):
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        df[col].hist(bins=30)
        plt.title(col)
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(f"figures/{col}.png")
        plt.close()
