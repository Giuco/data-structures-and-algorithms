# Uses python3
import sys
from typing import List, Tuple


def get_majority_element_naive(a: List[int]) -> int:
    count_of_n = {}
    output = 0

    for u in a:
        if u not in count_of_n:
            count_of_n[u] = 1
        else:
            count_of_n[u] += 1

        if count_of_n[u] > len(a) / 2:
            output = 1
            break

    return output


def _get_majority_element_divide_and_conquer(elements: List[int]) -> int:
    if len(elements) == 1:
        return elements[0]

    left, right = split(elements)
    left = _get_majority_element_divide_and_conquer(left)
    right = _get_majority_element_divide_and_conquer(right)

    if left != -1:
        count = sum([1 for e in elements if e == left])
        if count > len(elements) // 2:
            return left

    if right != -1:
        count = sum([1 for e in elements if e == right])
        if count > len(elements) // 2:
            return right

    return -1


def split(elements: List[int]) -> Tuple[List[int], List[int]]:
    middle_index = len(elements) // 2

    return elements[:middle_index], elements[middle_index:]


def get_majority_element_divide_and_conquer(a: List[int]) -> int:
    k = _get_majority_element_divide_and_conquer(a)

    return 0 if k == -1 else 1


if __name__ == '__main__':
    input_data = sys.stdin.read()
    _, *a_input = list(map(int, input_data.split()))
    print(get_majority_element_divide_and_conquer(a_input))
