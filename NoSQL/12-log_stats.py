#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""

from typing import List
from pymongo import MongoClient


def main() -> None:
    """Print collection-wide counts and per-method stats."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    coll = client.logs.nginx

    total = coll.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = coll.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_count = coll.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()

