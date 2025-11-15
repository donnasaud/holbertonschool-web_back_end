#!/usr/bin/env python3
"""Module containing safe first element function."""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Safe first element function."""
    if lst:
        return lst[0]
    else:
        return None
