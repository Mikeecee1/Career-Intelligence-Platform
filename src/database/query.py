"""Analytical queries for the Career Intelligence Platform."""

from typing import Any

from src.database.connection import get_collection


# ---------------------------------------------------------------------
# General statistics
# ---------------------------------------------------------------------

def total_jobs(collection_name: str | None = None) -> int:
    """Return the total number of jobs."""
    collection = get_collection(collection_name)
    return collection.count_documents({})

'''
def jobs_by_source(collection_name: str | None = None) -> list[dict[str, Any]]:
    """Return job counts grouped by data source."""
    pass
'''

def jobs_by_location(collection_name: str | None = None) -> list[dict[str, Any]]:
    """Return job counts grouped by town."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "location.town": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$location.town",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "location": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

'''
def jobs_by_organisation(collection_name: str | None = None) -> list[dict[str, Any]]:
    """Return job counts grouped by organisation."""
    pass
'''

# ---------------------------------------------------------------------
# Employment analysis
# ---------------------------------------------------------------------

def jobs_by_contract_type(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return job counts grouped by contract type."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "employment.contract_type": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$employment.type",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "contract_type": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]
'''
def jobs_by_working_pattern(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return job counts grouped by working pattern."""


def jobs_by_pay_band(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return job counts grouped by NHS pay band."""
'''

def salary_statistics(
    collection_name: str | None = None,
) -> dict[str, Any]:
    """Return salary summary statistics."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "salary.minimum": {"$exists": True, "$ne": None},
            }
        },
        {
            "$group": {
                "_id": None,
                "count": {"$sum": 1},
                "min_salary": {"$min": "$employment.salary"},
                "max_salary": {"$max": "$employment.salary"},
                "average_salary": {"$avg": "$employment.salary"},
            }
        },
    ]

    result = list(collection.aggregate(pipeline))
    if not result:
        return {
            "count": 0,
            "min_salary": None,
            "max_salary": None,
            "average_salary": None,
        }

    summary = result[0]
    return {
        "count": summary.get("count", 0),
        "min_salary": summary.get("min_salary"),
        "max_salary": summary.get("max_salary"),
        "average_salary": summary.get("average_salary"),
    }


# ---------------------------------------------------------------------
# Recruitment trends
# ---------------------------------------------------------------------

def jobs_by_publish_date(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return jobs grouped by publication date."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "dates.published": {"$exists": True, "$ne": None},
            }
        },
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": "%Y-%m-%d",
                        "date": "$dates.published",
                    }
                },
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"_id": 1},
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "published_date": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]
'''
def jobs_by_closing_date(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return jobs grouped by closing date."""


def jobs_closing_soon(
    days: int = 7,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return jobs closing within a specified number of days."""
'''

# ---------------------------------------------------------------------
# Top-N queries
# ---------------------------------------------------------------------

def top_employers(
    limit: int = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the employers with the most vacancies."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "organisation.name": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$organisation.name",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
        {
            "$limit": max(limit, 0),
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "organisation": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

def top_locations(
    limit: int = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the locations with the most vacancies."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "location.town": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$location.town",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
        {
            "$limit": max(limit, 0),
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "location": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

def top_specialties(
    limit: int = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the most common specialties."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$match": {
                "job.specialty": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$job.specialty",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
        {
            "$limit": max(limit, 0),
        },
    ]

    result = list(collection.aggregate(pipeline))

    return [
        {
            "specialty": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

# ---------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------

def search_job_title(
    keyword: str,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search job titles by keyword."""
    collection = get_collection(collection_name)

    return list(
        collection.find(
            {
                "job.title": {
                    "$regex": keyword,
                    "$options": "i",
                }
            },
            {"_id": 0},
        )
    )

def search_organisation(
    organisation: str,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search by organisation name."""
    collection = get_collection(collection_name)

    return list(
        collection.find(
            {
                "organisation.name": {
                    "$regex": organisation,
                    "$options": "i",
                }
            },
            {"_id": 0},
        )
    )

def search_location(
    town: str,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search by town."""
    collection = get_collection(collection_name)

    return list(
        collection.find(
            {
                "location.town": {
                    "$regex": town,
                    "$options": "i",
                }
            },
            {"_id": 0},
        )
    )

# ---------------------------------------------------------------------
# Future AI queries
# ---------------------------------------------------------------------
'''
def find_similar_jobs(
    job_id: str,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return similar jobs (future semantic search)."""


def duplicate_candidates(
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return potential duplicate vacancies across providers."""
'''