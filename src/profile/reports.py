"""Analyse raw data and generate reports to inform the data cleaning process."""

import pandas as pd


def generate_profile(df: pd.DataFrame) -> None:
    """
    Generate a summary report for the raw NHS jobs dataset.

    Args:
        df: Raw pandas DataFrame.
    """

    print("\n" + "=" * 60)
    print("NHS JOBS DATA PROFILE")
    print("=" * 60)

    print(f"Rows:                {df.shape[0]:,}")
    print(f"Columns:             {df.shape[1]}")
    print(f"Duplicate rows:      {df.duplicated().sum():,}")

    print("\n" + "-" * 60)
    print("COLUMN DATA TYPES")
    print("-" * 60)
    print(df.dtypes)

    print("\n" + "-" * 60)
    print("MISSING VALUES")
    print("-" * 60)

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values found.")
    else:
        print(missing.sort_values(ascending=False))

    print("\n" + "=" * 60)