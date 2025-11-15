#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence if it exists, else None"""
    if lst:
        return lst[0]
    return None

