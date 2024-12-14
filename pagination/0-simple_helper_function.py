#!/usr/bin/env python3
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
