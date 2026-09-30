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
            "id": None,
            "title": get_value(row, "job_title"),
            "description": get_value(row, "job_description"),
            "requirements": [],
        },

        "organisation": {
            "name": get_value(row, "company_name"),
            #"department": get_value(row, "department"), No department for reed data
        },

        "employment": {
            "contract_type": get_value(row, "job_type"),
            #"working_pattern": get_value(row, "working_pattern"),Not applicable for reed data
            "salary":  get_value(row, "salary_offered"),
            
            
        },

        "location": {
            "town": get_value(row, "city"),
            #"postcode": get_value(row, "json_address_postcode"),
            #"latitude": get_value(row, "json_lat"),
            #"longitude": get_value(row, "json_lng"),
            ## For the Reed dataset, we only have the city information. Postcode, latitude, and longitude are not available.
        },

        "dates": {
            "published": get_value(row, "post_date"),
            
        },
        # Metadata is currently hard-coded for the initial reed implementation.
        # As the platform evolves, these values will be derived from the active
        # data source configuration, allowing the same pipeline to process
        # multiple recruitment providers without code changes.
        "metadata": {
            "source": "Reed",
            "dataset": "Reed UK 50,000 Job Board Records",
            "source_id": None,
            "scrape_date": None,
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