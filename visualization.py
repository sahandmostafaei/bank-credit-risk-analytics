"""
Visualization Module
Author: Sahand Mostafaei
"""

import os
import matplotlib.pyplot as plt


def create_output_folder():
    os.makedirs("figures", exist_ok=True)


def save_histograms(df):

    create_output_folder()

    numeric = df.select_dtypes(include="number")

    for column in numeric.columns:

        plt.figure(figsize=(7,4))

        df[column].hist(bins=30)

        plt.title(column)

        plt.xlabel(column)

        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(f"figures/{column}_histogram.png")

        plt.close()


def save_missing_values(df):

    create_output_folder()

    missing = df.isnull().sum()

    plt.figure(figsize=(10,5))

    missing.plot(kind="bar")

    plt.title("Missing Values by Feature")

    plt.tight_layout()

    plt.savefig("figures/missing_values.png")

    plt.close()
