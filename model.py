"""
Credit Risk Prediction Model
Author: Sahand Mostafaei
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def train_model(df):

    target = None

    for col in [
        "loan_status",
        "Loan_Status",
        "default",
        "Default",
    ]:
        if col in df.columns:
            target = col
            break

    if target is None:
        print("\nNo target column found.")
        return

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
        test_size=0.20,
        random_state=42,
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\n==============================")
    print("MODEL PERFORMANCE")
    print("==============================")

    print(f"Accuracy : {accuracy_score(y_test, predictions):.3f}")
    print(f"Precision: {precision_score(y_test, predictions, average='weighted'):.3f}")
    print(f"Recall   : {recall_score(y_test, predictions, average='weighted'):.3f}")
    print(f"F1 Score : {f1_score(y_test, predictions, average='weighted'):.3f}")

    print("\nConfusion Matrix")

    print(confusion_matrix(y_test, predictions))
