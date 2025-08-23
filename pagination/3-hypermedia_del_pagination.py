#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient pagination"""
        assert index is not None and 0 <= index < len(self.__indexed_dataset)

        data = []
        collected = 0
        current_index = index
        max_index = max(self.__indexed_dataset.keys())

        while collected < page_size and current_index <= max_index:
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                collected += 1
            current_index += 1

        # current_index now points to next index to query
        next_index = current_index
        # skip any deleted indexes for next_index
        while (next_index <= max_index and
               next_index not in self.__indexed_dataset):
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
