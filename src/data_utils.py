"""Dataset loading and preprocessing helpers used across notebooks."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from project_config import RANDOM_SEED, TEST_SIZE, VALIDATION_SIZE


@dataclass
class DatasetSplit:
    X_train_raw: pd.DataFrame
    X_val_raw: pd.DataFrame
    X_test_raw: pd.DataFrame
    X_train_scaled: pd.DataFrame
    X_val_scaled: pd.DataFrame
    X_test_scaled: pd.DataFrame
    y_train: pd.Series
    y_val: pd.Series
    y_test: pd.Series
    scaler: StandardScaler
    target_names: list[str]


def load_breast_cancer_dataframe() -> tuple[pd.DataFrame, pd.Series, list[str]]:
    """Return the sklearn Breast Cancer dataset as pandas objects."""
    dataset = load_breast_cancer(as_frame=True)
    X = dataset.data.copy()
    y = dataset.target.copy()
    return X, y, list(dataset.target_names)


def create_stratified_splits(
    test_size: float = TEST_SIZE,
    validation_size: float = VALIDATION_SIZE,
    random_state: int = RANDOM_SEED,
) -> DatasetSplit:
    """Create train/validation/test splits and scale features from train statistics."""
    X, y, target_names = load_breast_cancer_dataframe()

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
    )

    adjusted_val_size = validation_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=adjusted_val_size,
        stratify=y_train_val,
        random_state=random_state,
    )

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X.columns,
        index=X_train.index,
    )
    X_val_scaled = pd.DataFrame(
        scaler.transform(X_val),
        columns=X.columns,
        index=X_val.index,
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=X.columns,
        index=X_test.index,
    )

    return DatasetSplit(
        X_train_raw=X_train,
        X_val_raw=X_val,
        X_test_raw=X_test,
        X_train_scaled=X_train_scaled,
        X_val_scaled=X_val_scaled,
        X_test_scaled=X_test_scaled,
        y_train=y_train,
        y_val=y_val,
        y_test=y_test,
        scaler=scaler,
        target_names=target_names,
    )


def summarize_dataframe(X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    """Produce a compact dataset summary table."""
    summary = {
        "num_samples": [len(X)],
        "num_features": [X.shape[1]],
        "positive_class_ratio": [float(y.mean())],
        "missing_values": [int(X.isna().sum().sum())],
        "duplicate_rows": [int(X.duplicated().sum())],
    }
    return pd.DataFrame(summary)


def class_distribution(y: pd.Series, target_names: list[str]) -> pd.DataFrame:
    """Return class counts and proportions."""
    counts = y.value_counts().sort_index()
    proportions = y.value_counts(normalize=True).sort_index()
    return pd.DataFrame(
        {
            "class_id": counts.index,
            "class_name": [target_names[idx] for idx in counts.index],
            "count": counts.values,
            "ratio": proportions.values,
        }
    )


def split_summary(split: DatasetSplit) -> pd.DataFrame:
    """Return sample counts and class balance for each split."""
    rows = []
    for split_name, X_part, y_part in [
        ("train", split.X_train_raw, split.y_train),
        ("validation", split.X_val_raw, split.y_val),
        ("test", split.X_test_raw, split.y_test),
    ]:
        rows.append(
            {
                "split": split_name,
                "samples": len(X_part),
                "positive_ratio": float(y_part.mean()),
            }
        )
    return pd.DataFrame(rows)


def scaled_feature_check(split: DatasetSplit, n_features: int = 5) -> pd.DataFrame:
    """Inspect whether training split scaling centers features around zero."""
    columns = split.X_train_scaled.columns[:n_features]
    means = split.X_train_scaled[columns].mean()
    stds = split.X_train_scaled[columns].std(ddof=0)
    return pd.DataFrame(
        {
            "feature": columns,
            "train_mean_after_scaling": means.values,
            "train_std_after_scaling": stds.values,
        }
    )


def top_target_correlations(X: pd.DataFrame, y: pd.Series, n: int = 10) -> pd.DataFrame:
    """Return features with the strongest absolute correlation to the target."""
    correlations = X.assign(target=y).corr(numeric_only=True)["target"].drop("target")
    ordered = correlations.abs().sort_values(ascending=False).head(n).index
    return pd.DataFrame(
        {
            "feature": ordered,
            "correlation_with_target": correlations.loc[ordered].values,
            "absolute_correlation": correlations.loc[ordered].abs().values,
        }
    )
