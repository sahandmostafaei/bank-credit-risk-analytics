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
    roc_auc_score,
    confusion_matrix,
)


def train_model(df):

    target = None

    possible_targets = [
        "loan_status",
        "Loan_Status",
        "default",
        "Default"
    ]

    for col in possible_targets:
        if col in df.columns:
            target = col
            break

    if target is None:
        print("\nTarget column not found.")
        return

    X = df.drop(columns=[target])

    X = pd.get_dummies(X, drop_first=True)

    X = X.fillna(X.mean(numeric_only=True))
    X = X.fillna(0)

    y = df[target]

    if y.dtype == object:
        y = pd.factorize(y)[0]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\n==============================")
    print("MODEL PERFORMANCE")
    print("==============================")

    print(f"Accuracy : {accuracy_score(y_test, predictions):.3f}")
    print(f"Precision: {precision_score(y_test, predictions):.3f}")
    print(f"Recall   : {recall_score(y_test, predictions):.3f}")
    print(f"F1 Score : {f1_score(y_test, predictions):.3f}")
    print(f"ROC AUC  : {roc_auc_score(y_test, probabilities):.3f}")

    print("\nConfusion Matrix")

    print(confusion_matrix(y_test, predictions))
