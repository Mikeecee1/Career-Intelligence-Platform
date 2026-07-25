"""Clean the raw NHS jobs dataset."""

import pandas as pd

from config import CLEANING_OPTIONS


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the NHS jobs dataset.

    Args:
        df: Raw pandas DataFrame.

    Returns:
        Cleaned pandas DataFrame.
    """

    # Work on a copy
    df = df.copy()

    # Standardise column names
    if CLEANING_OPTIONS["standardise_columns"]:
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

    # Remove duplicate records
    if CLEANING_OPTIONS["remove_duplicates"]:
        df = df.drop_duplicates()

    # Drop rows containing missing values
    if CLEANING_OPTIONS["drop_empty_rows"]:
        df = df.dropna()

    # Placeholder for future cleaning steps
    if CLEANING_OPTIONS["convert_dates"]:
        pass

    if CLEANING_OPTIONS["convert_salary"]:
        pass

    return df