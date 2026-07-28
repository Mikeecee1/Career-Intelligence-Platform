from pathlib import Path

import os
from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Required environment variable '{name}' is not set.")
    return value


MONGO_URI: str = get_required_env("MONGO_URI")
MONGO_DATABASE: str = get_required_env("MONGO_DATABASE")
MONGO_COLLECTION: str = get_required_env("MONGO_COLLECTION")

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "jobs_raw.csv"

# Cleaning options
CLEANING_OPTIONS = {
    "remove_duplicates": True,
    "standardise_columns": True,
    "drop_empty_rows": False,
    "convert_dates": True,
    "convert_salary": True,
}