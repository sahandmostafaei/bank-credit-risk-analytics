"""
Credit Risk Prediction Model
Author: Sahand Mostafaei
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_model(df):

    # Find target column
    target = None

    for col in [
        "loan_status",
        "Loan_Status",
        "default",
        "Default"
    ]:
        if col in df.columns:
            target = col
            break

    if target is None:
        print("No target column found.")
        return

    # Keep numeric features only
    numeric = df.select_dtypes(include="number")

    if target in numeric.columns:
        X = numeric.drop(columns=[target])
    else:
        X = numeric

    y = df[target]

    X = X.fillna(X.mean())

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\n==============================")
    print("MODEL RESULTS")
    print("==============================")
    print(f"Accuracy: {accuracy:.3f}")
