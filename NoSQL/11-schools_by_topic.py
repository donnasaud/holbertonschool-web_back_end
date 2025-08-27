#!/usr/bin/env python3
"""Return schools that include a specific topic."""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Dict[str, Any]]:
    """
    Find all school documents whose `topics` array contains the given topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic: Topic name to match (exact string match within the array).

    Returns:
        A list of matching documents.
    """
    return list(mongo_collection.find({"topics": topic}))

