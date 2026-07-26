# Validator functions for data validation


def validate_document(document: dict) -> tuple[bool, list[str], list[str]]:
    """
    Validate a job document.

    Args:
        document (dict): A dictionary representing a job document.

    Returns:
        tuple: A tuple containing a boolean indicating if the document is valid,
               a list of error messages, and a list of warnings.
    """

    errors: list[str] = []
    warnings: list[str] = []

    # Validate required top-level sections
    required_sections = [
        "job",
        "organisation",
        "employment",
        "location",
        "dates",
        "metadata",
        "ai",
    ]

    for section in required_sections:
        if section not in document:
            errors.append(f"Missing section: {section}")

    # Validate job section
    job = document.get("job", {})
    if not job.get("id"):
        errors.append("Job ID is missing.")
    if not job.get("title"):
        errors.append("Job title is missing.")
    if not job.get("description"):
        errors.append("Job description is missing.")

    # Validate organisation section
    organisation = document.get("organisation", {})
    if not organisation.get("name"):
        warnings.append("Organisation name is missing.")

    # Validate employment section
    employment = document.get("employment", {})
    salary = employment.get("salary", {})

    minimum = salary.get("minimum")
    maximum = salary.get("maximum")

    if minimum is None or maximum is None:
        warnings.append("Salary range is incomplete.")
    elif minimum > maximum:
        errors.append("Minimum salary exceeds maximum salary.")

    # Validate location section
    location = document.get("location", {})
    if not location.get("town"):
        errors.append("Location town is missing.")
    if not location.get("postcode"):
        warnings.append("Location postcode is missing.")

    # Validate dates section
    dates = document.get("dates", {})
    if not dates.get("published"):
        warnings.append("Published date is missing.")
    if not dates.get("closing"):
        warnings.append("Closing date is missing.")

    return (len(errors) == 0, errors, warnings)

def validate_documents(documents: list[dict]) -> list[dict]:
    """
    Validate a list of job documents.

    Args:
        documents (list): A list of dictionaries representing job documents.

    Returns:
        list: A list of dictionaries containing validation results for each document.
    """
    results: list[dict] = []

    for i, document in enumerate(documents):
        valid, errors, warnings = validate_document(document)
        results.append({
            "index": i,
            "valid": valid,
            "errors": errors,
            "warnings": warnings
        })

    return results

def get_valid_documents(documents: list[dict]) -> list[dict]:
    """
    Filter and return only valid job documents from a list.
    """

    return [
        document
        for document in documents
        if validate_document(document)[0]
    ]