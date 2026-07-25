import pandas as pd


def load_data(filepath):
    """Load the NHS jobs dataset."""

    try:
        df = pd.read_csv(filepath)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found: {filepath}")