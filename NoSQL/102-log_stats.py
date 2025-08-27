#!/usr/bin/env python3
"""Extended Nginx log stats: adds Top 10 IPs."""

from typing import List
from pymongo import MongoClient


def main() -> None:
    """Print collection-wide counts, per-method stats, /status count, and Top 10 IPs."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    coll = client.logs.nginx

    total = coll.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = coll.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_count = coll.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    # Top 10 IPs by occurrence
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]
    for doc in coll.aggregate(pipeline):
        ip = doc["_id"]
        cnt = doc["count"]
        print(f"\t{ip}: {cnt}")


if __name__ == "__main__":
    main()

