#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection."""
from typing import Any


def insert_school(mongo_collection, **kwargs: Any):
    """
    Insert a document in the given collection using kwargs.

    Args:
        mongo_collection: A PyMongo collection object.
        **kwargs: Fields for the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

