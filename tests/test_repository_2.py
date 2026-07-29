from src.database.repository import (
    insert_documents,
    count_documents,
    delete_all_documents,
    find_documents,
)

# ---------------------------------------------------------
# Reset collection
# ---------------------------------------------------------

print("\nResetting collection...")

deleted = delete_all_documents()

print(f"Deleted {deleted} existing documents.")

# ---------------------------------------------------------
# Test data
# ---------------------------------------------------------

test_documents = [
    {
        "job": {
            "id": "TEST001",
            "title": "Data Engineer",
            "description": "Repository test document.",
            "requirements": [],
        },
        "organisation": {
            "name": "OpenAI",
            "department": "Engineering",
        },
        "employment": {},
        "location": {},
        "dates": {},
        "metadata": {
            "source": "Test",
        },
        "ai": {
            "skills": [],
            "embedding": None,
        },
    }
]

# ---------------------------------------------------------
# First insert
# ---------------------------------------------------------

print("\nFirst insert...")

inserted = insert_documents(test_documents)

print(f"Inserted: {inserted}")
print(f"Documents in collection: {count_documents()}")

# ---------------------------------------------------------
# Duplicate insert
# ---------------------------------------------------------

print("\nAttempting duplicate insert...")

inserted = insert_documents(test_documents)

print(f"Inserted: {inserted}")
print(f"Documents in collection: {count_documents()}")

# ---------------------------------------------------------
# Display stored documents
# ---------------------------------------------------------

print("\nStored documents:")

documents = find_documents()

for document in documents:
    print(document["job"]["id"], "-", document["job"]["title"])