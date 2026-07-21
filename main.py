from analysis import *

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

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
