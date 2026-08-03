"""Analytical queries for the Career Intelligence Platform."""

from typing import Any

from src.database.connection import get_collection
from src.config import SALARY_BIN_SIZE, MAX_ANALYSIS_SALARY, SALARY_CHART_MAX


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

def jobs_by_location(
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return job counts grouped by town."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

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

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

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
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return job counts grouped by contract type."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

    pipeline = [
        {
            "$match": {
                "employment.contract_type": {"$exists": True, "$ne": None, "$ne": ""},
            }
        },
        {
            "$group": {
                "_id": "$employment.contract_type",
                "jobs": {"$sum": 1},
            }
        },
        {
            "$sort": {"jobs": -1, "_id": 1},
        },
    ]

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

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
            "employment.salary.minimum": {
                "$exists": True,
                "$ne": None,
            }
        }
    },
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1},
            "min_salary": {"$min": "$employment.salary.minimum"},
            "max_salary": {"$max": "$employment.salary.maximum"},
            "average_salary": {"$avg": "$employment.salary.minimum"},
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


def salary_distribution(
    bin_size: int = SALARY_BIN_SIZE,
    max_bin: int = SALARY_CHART_MAX,
    maximum_salary: int = MAX_ANALYSIS_SALARY,
    collection_name: str | None = None,
) -> list[dict]:
    """Return salary distribution in specified bins with one capped upper bin."""
    collection = get_collection(collection_name)

    # Sentinel bucket id for all values >= max_bin and <= maximum_salary
    capped_bin_id = (maximum_salary // bin_size) + 1

    pipeline = [
        {
            "$match": {
                "employment.salary.minimum": {
                    "$exists": True,
                    "$ne": None,
                    "$gte": 0,
                    "$lte": maximum_salary,
                },
            }
        },
        {
            "$project": {
                "salary_bin": {
                    "$cond": [
                        {"$gte": ["$employment.salary.minimum", max_bin]},  # changed from $gt
                        capped_bin_id,
                        {"$floor": {"$divide": ["$employment.salary.minimum", bin_size]}},
                    ]
                }
            }
        },
        {
            "$group": {
                "_id": "$salary_bin",
                "jobs": {"$sum": 1},
            }
        },
        {"$sort": {"_id": 1}},
    ]

    result = list(collection.aggregate(pipeline))
    distribution = []

    for row in result:
        salary_bin = row["_id"]
        jobs = row["jobs"]

        if salary_bin == capped_bin_id:
            salary_range_start = max_bin
            salary_range_end = maximum_salary
        else:
            salary_range_start = salary_bin * bin_size
            salary_range_end = min(salary_range_start + bin_size - 1, max_bin - 1)

        distribution.append(
            {
                "salary_range": f"£{salary_range_start//1000}k–£{salary_range_end//1000}k",
                "jobs": jobs,
            }
        )

    return distribution


#Helper function to check outliers in salary values - less than 0 or greater than MAX_ANALYSIS_SALARY & missing values
def salary_outliers(
    collection_name: str | None = None,
) -> dict[str, Any]:
    """Return jobs with extreme or missing salary values."""
    collection = get_collection(collection_name)

    pipeline = [
        {
            "$group": {
                "_id": None,
                "below_minimum": {
                    "$sum": {
                        "$cond": [
                            {
                                "$and": [
                                    {"$ne": ["$employment.salary.minimum", None]},
                                    {"$lt": ["$employment.salary.minimum", 0]},
                                ]
                            },
                            1,
                            0,
                        ]
                    }
                },
                "above_maximum": {
                    "$sum": {
                        "$cond": [
                            {
                                "$or": [
                                    {
                                        "$gt": [
                                            "$employment.salary.minimum",
                                            MAX_ANALYSIS_SALARY,
                                        ]
                                    },
                                    {
                                        "$gt": [
                                            "$employment.salary.maximum",
                                            MAX_ANALYSIS_SALARY,
                                        ]
                                    },
                                ]
                            },
                            1,
                            0,
                        ]
                    }
                },
                "missing_salary": {
                    "$sum": {
                        "$cond": [
                            {
                                "$or": [
                                    {"$eq": ["$employment.salary.minimum", None]},
                                    {"$eq": ["$employment.salary.maximum", None]},
                                ]
                            },
                            1,
                            0,
                        ]
                    }
                },
            }
        },
    ]

    result = list(collection.aggregate(pipeline))
    if not result:
        return {
            "below_minimum": {"jobs": 0},
            "above_maximum": {"jobs": 0},
            "missing_salary": {"jobs": 0},
        }

    summary = result[0]
    return {
        "below_minimum": {"jobs": summary.get("below_minimum", 0)},
        "above_maximum": {"jobs": summary.get("above_maximum", 0)},
        "missing_salary": {"jobs": summary.get("missing_salary", 0)},
    }

# List jobs with outlier salaries above MAX_ANALYSIS_SALARY - print job title, job_id, maximum salary, pay scheme
def list_salary_outliers(
    limit: int | None = 25,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """
    Return details of jobs with maximum salaries above MAX_ANALYSIS_SALARY.
    """
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

    pipeline = [
        {
            "$match": {
                "employment.salary.maximum": {"$gt": MAX_ANALYSIS_SALARY},
            }
        },
        {
            "$project": {
                "_id": 0,
                "title": "$job.title",
                "job_id": "$job.id",
                "maximum": "$employment.salary.maximum",
                "pay_scheme": "$employment.salary.pay_scheme",
            }
        },
        {
            "$sort": {
                "maximum": -1
            }
        },
    ]

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))

    return [
        {
            "title": row.get("title"),
            "job_id": row.get("job_id"),
            "maximum": row.get("maximum"),
            "pay_scheme": row.get("pay_scheme"),
        }
        for row in result
    ]
#---------------------------------------------------------------------
# Recruitment trends
# ---------------------------------------------------------------------

def jobs_by_publish_date(
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return jobs grouped by publication date."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

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

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

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
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the employers with the most vacancies."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

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
    ]

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

    return [
        {
            "organisation": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

def top_locations(
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the locations with the most vacancies."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

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

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

    return [
        {
            "location": row["_id"],
            "jobs": row["jobs"],
        }
        for row in result
    ]

def top_specialties(
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Return the most common specialties."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

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
    ]

    if max_limit is not None:
        pipeline.append({"$limit": max_limit})

    result = list(collection.aggregate(pipeline))
    #if max_limit is not None:
    #    result = result[:max_limit]

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
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search job titles by keyword."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

    cursor = collection.find(
        {
            "job.title": {
                "$regex": keyword,
                "$options": "i",
            }
        },
        {"_id": 0},
    )

    if max_limit is not None:
        try:
            cursor = cursor.limit(max_limit)
        except AttributeError:
            pass

    result = list(cursor)
    #if max_limit is not None:
    #    result = result[:max_limit]
    return result

def search_organisation(
    organisation: str,
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search by organisation name."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

    cursor = collection.find(
        {
            "organisation.name": {
                "$regex": organisation,
                "$options": "i",
            }
        },
        {"_id": 0},
    )

    if max_limit is not None:
        try:
            cursor = cursor.limit(max_limit)
        except AttributeError:
            pass

    result = list(cursor)
    #if max_limit is not None:
    #    result = result[:max_limit]
    return result

def search_location(
    town: str,
    limit: int | None = 10,
    collection_name: str | None = None,
) -> list[dict[str, Any]]:
    """Search by town."""
    collection = get_collection(collection_name)
    max_limit = None if limit is None else max(limit, 0)

    cursor = collection.find(
        {
            "location.town": {
                "$regex": town,
                "$options": "i",
            }
        },
        {"_id": 0},
    )

    if max_limit is not None:
        try:
            cursor = cursor.limit(max_limit)
        except AttributeError:
            pass

    result = list(cursor)
    #if max_limit is not None:
    #    result = result[:max_limit]
    return result

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