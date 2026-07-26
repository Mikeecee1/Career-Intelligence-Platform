

def build_job_document(row: dict) -> dict:
    """
    Map a cleaned dataset row to a Career Intelligence document.
    """

    return {

        "job": {
            "id": row.get("job_reference"),
            "title": row.get("job_title"),
            "description": row.get("full_description"),
            "requirements": [],
        },

        "organisation": {
            "name": row.get("employer"),
            "department": row.get("department"),
        },

        "employment": {
            "contract_type": row.get("job_type"),
            "working_pattern": row.get("working_pattern"),
            "salary": {
                "minimum": row.get("json_salary_min"),
                "maximum": row.get("json_salary_max"),
                "pay_band": row.get("pay_band"),
                "pay_scheme": row.get("pay_scheme"),
            },
        },

        "location": {
            "town": row.get("location"),
            "postcode": row.get("json_address_postcode"),
            "latitude": row.get("json_lat"),
            "longitude": row.get("json_lng"),
        },

        "dates": {
            "published": row.get("json_date_posted"),
            "closing": row.get("json_closing_date"),
        },

        "metadata": {
            "source": "NHS Jobs",
            "scrape_date": row.get("scrape_dt"),
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