#!/usr/bin/env python3
from typing import Tuple
import csv
import math
from typing import List
"""
This module contains the function 'index_range'.
"""


def index_range(page, page_size) -> Tuple[int, int]:
    """
    The function should return a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        allows you to obtain a specific page of data from a data set, using the
        page number (page) and page size (page_size) provided as parameters.
        """
        assert isinstance(page, int), "page must be an integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page > 0, "page must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"

        dataset = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
         Returns a dictionary with pagination information
         and the data for the requested page.
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        next__page = page + 1 if page < total_pages else None
        prev_page = page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next__page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
