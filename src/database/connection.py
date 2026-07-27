from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from src.config import (
    MONGO_URI,
    MONGO_DATABASE,
    MONGO_COLLECTION,
)


def get_database() -> Database:
    client = MongoClient(MONGO_URI)
    return client[MONGO_DATABASE]


def get_collection(collection_name: str | None = None) -> Collection:
    db = get_database()
    return db[collection_name or MONGO_COLLECTION]