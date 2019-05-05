# Uses python3
import sys
from typing import List, Union


def no_more_options(start: Union[int, float, None], end: Union[int, float, None]) -> bool:
    start_is_numeric = any([isinstance(start, int), isinstance(start, float)])
    end_is_numeric = any([isinstance(end, int), isinstance(end, float)])
    start_equals_end = start == end

    return start_equals_end and end_is_numeric and start_is_numeric


def binary_search(list_to_search: List[float], searched_value: float, start: int = None, end: int = None) -> int:
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


def linear_search(list_to_search: List[float], searched_value: float) -> int:
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
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
