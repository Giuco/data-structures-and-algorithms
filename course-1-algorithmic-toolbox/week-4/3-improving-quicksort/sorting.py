# Uses python3
import random
import sys
from typing import List
from numbers import Number
from random import randint


def get_random_pivot_point(size: int) -> int:
    return randint(0, size-1)


def get_pivot_point(elements: List[Number]) -> int:
    return get_random_pivot_point(len(elements))


def quick_sort(elements: List[Number]) -> List[Number]:
    if len(elements) <= 1:
        return elements

    pivot_point = get_pivot_point(elements)
    pivot = elements[pivot_point]

    left, middle, right = [], [], []

    for e in elements:
        if e == pivot:
            middle.append(e)
        elif e > pivot:
            right.append(e)
        else:
            left.append(e)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + middle + right


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = quick_sort(a)
    for x in a:
        print(x, end=' ')
