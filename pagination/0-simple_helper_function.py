#!/usr/bin/env python3
""" Learning Pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    In this method we will calculate the start index and end index
    to reach a specific page with a limited page size.

    Args:
        page (int): the page number we want to reach (starting from 1).
        page_size (int): the size of each page.

    Returns:
        tuple: combination of the start_index and the end_index.

    Formula:
        n: (number of page)
        p: (page size)
        start_index = (n-1) * p
        end_index = n * p
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
