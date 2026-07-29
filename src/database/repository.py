### Handles database operations for the application, including CRUD operations and data retrieval.
###
from pymongo.errors import PyMongoError

from src.database.connection import get_collection


# Version 1:
# Documents are considered duplicates if they share the same canonical job.id.
# Future versions may use AI-assisted matching across multiple data sources.
# Unused functions are retained for potential future use.
def document_exists(
    document: dict,
    collection_name: str | None = None,
) -> bool:
    """
    Return True if the document already exists.
    """
    collection = get_collection(collection_name)
    return collection.find_one({"job.id": document.get("job", {}).get("id")}) is not None     
     
#gets ids from the database to check if they already exist in the database
def get_existing_ids(
    collection_name: str | None = None,
) -> set[str]:
    """
    Return all existing canonical job IDs.
    """
    collection = get_collection(collection_name)

    return {
        document["job"]["id"]
        for document in collection.find(
            {},
            {"job.id": 1, "_id": 0},
        )
    }

def insert_documents(
    documents: list[dict],
    collection_name: str | None = None,
) -> int:
    """
    Insert multiple documents into MongoDB.

    Args:
        documents: Documents to insert.
        collection_name: Optional collection name. Uses the configured
                         default collection when not provided.

    Returns:
        Number of documents inserted.
    """
    if not documents:
        return 0

    collection = get_collection(collection_name)
    existing_ids = get_existing_ids(collection_name)

    try:
        inserted = 0

        for document in documents:

            job_id = document.get("job", {}).get("id")

            if job_id in existing_ids:
                continue

            collection.insert_one(document)
            existing_ids.add(job_id)
            inserted += 1

        return inserted

    except PyMongoError as exc:
        raise RuntimeError(
            f"Failed to insert documents into MongoDB: {exc}"
        ) from exc

def count_documents(collection_name: str | None = None) -> int:
    """
    Return the number of documents in a MongoDB collection.
    """
    collection = get_collection(collection_name)
    return collection.count_documents({})

def find_documents(
    limit: int = 10,
    collection_name: str | None = None,
) -> list[dict]:
    """
    Return a limited number of documents from MongoDB.
    """
    collection = get_collection(collection_name)

    return list(collection.find({}).limit(limit))

def find_by_id(
    document_id: str,
    collection_name: str | None = None,
) -> dict | None:
    """
    Find a Career Intelligence document by its job ID.

    Args:
        document_id: The canonical job ID to find.
        collection_name: Optional collection name. Uses the configured
                         default collection when not provided.

    Returns:
        The document if found, otherwise None.
    """
    collection = get_collection(collection_name)

    return collection.find_one({"job.id": document_id})


def delete_document(
    document_id: str,
    collection_name: str | None = None,
) -> int:
    """
    Delete a Career Intelligence document by its job ID.

    Args:
        document_id: The canonical job ID of the document to delete.
        collection_name: Optional collection name. Uses the configured
                         default collection when not provided.

    Returns:
        The number of documents deleted.
    """
    collection = get_collection(collection_name)

    result = collection.delete_one({"job.id": document_id})
    return result.deleted_count


def delete_all_documents(collection_name: str | None = None) -> int:
    """
    Delete all documents in a MongoDB collection.

    Args:
        collection_name: Optional collection name. Uses the configured
                         default collection when not provided.

    Returns:
        The number of documents deleted.
    """
    collection = get_collection(collection_name)

    result = collection.delete_many({})
    return result.deleted_count