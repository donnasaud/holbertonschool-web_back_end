#!/usr/bin/env python3
"""Simple helper for pagination: compute start/end indices for a page."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple (start_index, end_index) for the given page parameters.

    Page numbers are 1-indexed.
    Example:
        page=1, page_size=7  -> (0, 7)
        page=3, page_size=15 -> (30, 45)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

