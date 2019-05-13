# Uses python3
import sys
from numbers import Number
from typing import List


def no_more_options(start: Number, end: Number) -> bool:
    start_is_numeric = any([isinstance(start, int), isinstance(start, float)])
    end_is_numeric = any([isinstance(end, int), isinstance(end, float)])
    start_equals_end = start == end

    return start_equals_end and end_is_numeric and start_is_numeric


def binary_search(list_to_search: List[Number], searched_value: Number, start: int = None, end: int = None) -> int:
    if no_more_options(start, end):
        return -1

    if not start and not end:
        start = 0
        end = len(list_to_search)

    middle_index = (end + start) // 2
    middle_value = list_to_search[middle_index]

    if middle_value > searched_value:
        end = middle_index
        searched_value_index = binary_search(list_to_search, searched_value, start, end)
    elif middle_value < searched_value:
        start = middle_index + 1
        searched_value_index = binary_search(list_to_search, searched_value, start, end)
    else:
        searched_value_index = middle_index

    return searched_value_index


def linear_search(list_to_search: List[Number], searched_value: Number) -> int:
    searched_value_index = -1

    for i, value in enumerate(list_to_search):
        if value == searched_value:
            searched_value_index = i
            break

    return searched_value_index


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]

    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
