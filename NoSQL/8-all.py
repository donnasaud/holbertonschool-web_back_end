#!/usr/bin/env python3
"""List all documents in a MongoDB collection."""
from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, Any]]:
    """
    Return all documents in the given collection.

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of documents; returns [] if the collection is empty.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())

