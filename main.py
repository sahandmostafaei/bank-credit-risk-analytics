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
TARGET_COLUMN = "loan_status"


def prepare_model_data(df):
    """
    Prepare features and target for the credit-risk model.
    """

    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"Required target column '{TARGET_COLUMN}' "
            "was not found in the dataset."
        )

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    numerical_columns = X.select_dtypes(
        exclude=["object", "category"]
    ).columns.tolist()

    return (
        X,
        y,
        numerical_columns,
        categorical_columns,
    )


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

    (
        X,
        y,
        numerical_columns,
        categorical_columns,
    ) = prepare_model_data(df)

    train_model(
        X=X,
        y=y,
        numerical_columns=numerical_columns,
        categorical_columns=categorical_columns,
    )

    print("\nFigures saved in the figures folder.")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
