# Uses python3
import sys
from typing import List, Tuple


def split(elements: List[float]) -> Tuple[List[float], List[float]]:
    middle_index = len(elements) // 2

    return elements[:middle_index], elements[middle_index:]


def merge(left: List[float], right: List[float]) -> Tuple[int, List[float]]:
    sorted_elements = list()
    n_inversions = 0

    while left or right:
        if not left:
            sorted_elements += right
            right = []
        elif not right:
            sorted_elements += left
            left = []
        elif left[0] > right[0]:
            sorted_elements.append(right.pop(0))
            n_inversions += len(left)
        else:
            sorted_elements.append(left.pop(0))

    return n_inversions, sorted_elements


def merge_sort(elements: List[float]) -> Tuple[int, List[float]]:
    if len(elements) <= 1:
        return 0, elements

    left, right = split(elements)
    n_inversions_left, left = merge_sort(left)
    n_inversions_right, right = merge_sort(right)
    n_inversions_node, result = merge(left, right)

    n_inversions_total = n_inversions_left + n_inversions_right + n_inversions_node

    return n_inversions_total, result


def get_number_of_inversions(elements: List[float]) -> int:
    n_inversions, _ = merge_sort(elements)
    return n_inversions


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a = list(map(int, input_data.split()))
    print(get_number_of_inversions(a))
