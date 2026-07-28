from src.database.repository import (
    insert_documents,
    count_documents,
    find_documents,
    find_by_id,
    delete_document,
    #delete_all_documents,
)


test_document = {
    "job": {
        "id": "TEST001",
        "title": "Test Data Engineer",
        "description": "Test document for MongoDB repository.",
    },
    "organisation": {
        "name": "Test Organisation",
    },
    "employment": {},
    "location": {
        "town": "Bristol",
    },
    "dates": {},
    "metadata": {
        "source": "test",
    },
    "ai": {},
}


# Insert
inserted = insert_documents([test_document])
print(f"Inserted: {inserted}")

# Count
print(f"Document count: {count_documents()}")

# Find documents
documents = find_documents(limit=10)
print(f"Documents returned: {len(documents)}")

# Find by canonical job ID
document = find_by_id("TEST001")
print(f"Found: {document is not None}")

# Delete
deleted = delete_document("TEST001")
print(f"Deleted: {deleted}")

# Confirm deletion
print(f"Final document count: {count_documents()}")