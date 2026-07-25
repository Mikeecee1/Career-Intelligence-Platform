


def build_job_document(row: dict) -> dict:
    """
    Map a row of data to a job document.

    Args:
        row (dict): A dictionary representing a row of data.

    Returns:
        dict: A dictionary representing a job document.
    """

    return {

        "job": {
            "id": row.get("id"),
            "title": row.get("job_title"),
            "description": row.get("job_description"),
            "requirements": [],
        },

        "organisation": {
            "name": row.get("organisation"),
            "department": row.get("department"),
        },

        "employment": {
            "contract_type": row.get("contract_type"),
            "salary": {
                "minimum": row.get("salary_from"),
                "maximum": row.get("salary_to"),
                "pay_band": row.get("pay_band"),
            },
        },

        "location": {
            "town": row.get("town"),
            "postcode": row.get("postcode"),
        },

        "dates": {
            "published": row.get("date_posted"),
            "closing": row.get("closing_date"),
        },

        "metadata": {
            "source": "NHS Jobs",
        },

        "ai": {
            "skills": [],
            "embedding": None,
        }
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