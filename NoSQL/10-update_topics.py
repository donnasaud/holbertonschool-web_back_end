#!/usr/bin/env python3
"""Update the topics array for school documents by name."""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Replace the `topics` list for all documents with the given school name.

    Args:
        mongo_collection: A PyMongo collection object.
        name: School name used to match documents.
        topics: New list of topics to set on the document(s).
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

