import pandas as pd

#helper functions
# Handles normalisation of values from the pandas dataframe to ensure they are JSON-safe and consistent.
def normalise_value(value):
    """
    Convert pandas values into JSON-safe Python values.
    """

    if pd.isna(value):
        return None

    if isinstance(value, str):
        return value.strip()

    return value

#Wrapper function to get a value from a row and normalise it.
def get_value(row: dict, field: str):
    return normalise_value(row.get(field))

#document mapping functions

def build_job_document(row: dict) -> dict:
    """
    Map a cleaned dataset row to a Career Intelligence document.
    """

    return {

        "job": {
            "id": get_value(row, "job_reference"),
            "title": get_value(row, "job_title"),
            "description": get_value(row, "full_description"),
            "requirements": [],
        },

        "organisation": {
            "name": get_value(row, "employer"),
            "department": get_value(row, "department"),
        },

        "employment": {
            "contract_type": get_value(row, "job_type"),
            "working_pattern": get_value(row, "working_pattern"),
            "salary": {
                "minimum": get_value(row, "json_salary_min"),
                "maximum": get_value(row, "json_salary_max"),
                "pay_band": get_value(row, "pay_band"),
                "pay_scheme": get_value(row, "pay_scheme"),
            },
        },

        "location": {
            "town": get_value(row, "location"),
            "postcode": get_value(row, "json_address_postcode"),
            "latitude": get_value(row, "json_lat"),
            "longitude": get_value(row, "json_lng"),
        },

        "dates": {
            "published": get_value(row, "json_date_posted"),
            "closing": get_value(row, "json_closing_date"),
        },
        # Metadata is currently hard-coded for the initial NHS implementation.
        # As the platform evolves, these values will be derived from the active
        # data source configuration, allowing the same pipeline to process
        # multiple recruitment providers without code changes.
        "metadata": {
            "source": "NHS Jobs",
            "dataset": "NHS Jobs March 2019",
            "source_id": get_value(row, "job_reference"),
            "scrape_date": get_value(row, "scrape_dt"),
            "schema_version": 1,
        },

        "ai": {
            "skills": [],
            "embedding": None,
        },
    }

def build_documents(dataframe) -> list[dict]:
    """
    Map a list of rows to a list of job documents.

    Args:
        dataframe (pandas.DataFrame): A DataFrame representing rows of data.

    Returns:
        list: A list of dictionaries representing job documents.
    """
    rows = dataframe.to_dict(orient="records")

    return [build_job_document(row) for row in rows]