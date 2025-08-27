#!/usr/bin/env python3
"""Return all students sorted by average score (as `averageScore`)."""
from typing import List, Dict, Any


def top_students(mongo_collection) -> List[Dict[str, Any]]:
    """
    Compute each student's average over `topics.score` and sort descending.

    Args:
        mongo_collection: PyMongo collection object containing student docs
            shaped like:
            {
              "name": <str>,
              "topics": [{"title": <str>, "score": <number>}, ...]
            }

    Returns:
        List of documents with at least: `_id`, `name`, `averageScore`,
        sorted by `averageScore` (highest first).
    """
    pipeline = [
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))

