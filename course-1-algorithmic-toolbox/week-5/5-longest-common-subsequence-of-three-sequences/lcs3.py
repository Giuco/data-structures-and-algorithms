# Uses python3

import sys
from itertools import combinations
from numbers import Number
from typing import List


def lcs3_naive(a: List[Number], b: List[Number], c: List[Number]) -> List[Number]:
    """
    >>> len(lcs3_naive([1, 2, 3], [2, 1, 3], [1, 3 ,5]))
    2

    >>> len(lcs3_naive([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))
    3
    """
    a = [x for x in a if x in b and x in c]
    b = [x for x in b if x in a and x in c]

    min_length = min(len(a), len(b), len(c))

    for n in range(min_length, 0, -1):
        a_combinations = combinations(a, n)
        for a_combination in a_combinations:
            b_combinations = combinations(b, n)
            for b_combination in b_combinations:
                c_combinations = combinations(c, n)
                for c_combination in c_combinations:
                    if a_combination == b_combination == c_combination:
                        return list(a_combination)

    return []


def lcs3_recursive(a: List[Number], b: List[Number], c: List[Number]) -> int:
    """
    >>> lcs3_recursive([1, 2, 3], [2, 1, 3], [1, 3 ,5])
    2

    >> lcs3_recursive([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])
    3
    """
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        return 0
    elif a[-1] == b[-1] == c[-1]:
        return 1 + lcs3_recursive(a[:-1], b[:-1], c[:-1])
    else:
        return max(lcs3_recursive(a[:-1], b, c), lcs3_recursive(a, b[:-1], c), lcs3_recursive(a, b, c[:-1]))


def lcs3(a: List[Number], b: List[Number], c: List[Number]) -> int:
    """
    >>> lcs3([1, 2, 3], [2, 1, 3], [1, 3 ,5])
    2

    >>> lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])
    3
    """
    table = dict()

    for int_a in range(len(a) + 1):
        for int_b in range(len(b) + 1):
            for int_c in range(len(c) + 1):
                if int_a == 0 or int_b == 0 or int_c == 0:
                    table[int_a, int_b, int_c] = 0
                elif a[int_a - 1] == b[int_b - 1] == c[int_c - 1]:
                    table[int_a, int_b, int_c] = 1 + table[int_a - 1, int_b - 1, int_c - 1]
                else:
                    table[int_a, int_b, int_c] = max(
                        table[int_a - 1, int_b, int_c],
                        table[int_a, int_b - 1, int_c],
                        table[int_a, int_b, int_c - 1]
                    )

    return table[len(a), len(b), len(c)]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    an = data[0]
    data = data[1:]
    a_input = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b_input = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c_input = data[:cn]
    print(lcs3(a_input, b_input, c_input))
