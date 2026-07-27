from src.database.connection import get_collection

collection = get_collection()

print("Connected successfully")
print(f"Collection: {collection.name}")
print(f"Documents: {collection.count_documents({})}")