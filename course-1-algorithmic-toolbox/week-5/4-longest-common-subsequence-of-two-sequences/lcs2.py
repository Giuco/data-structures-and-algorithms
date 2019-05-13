# Uses python3

import sys
from itertools import combinations
from numbers import Number
from typing import List


def lis(arr: List[Number]) -> List[Number]:
    """
    >>> lis([10, 9, 2, 5, 3, 7, 101, 18])
    [2, 3, 7, 18]

    >>> lis([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1])
    [1, 3, 4, 5, 8]
    """
    n = len(arr)
    t = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and t[i] < t[j] + 1:
                t[i] = t[j] + 1

    reconstructed_lis = reconstruct_lis(arr, t)

    return reconstructed_lis


def reconstruct_lis(arr: List[Number], t: List[int]) -> List[Number]:
    n_lis = max(t)
    reconstructed_lis = list()

    for idx, m in enumerate(reversed(t)):
        if m == n_lis:
            n_lis -= 1
            reconstructed_lis.append(arr[-(idx + 1)])

    return list(reversed(reconstructed_lis))


def lcs2_naive(a: List[Number], b: List[Number]) -> List[Number]:
    """
    >>> len(lcs2_naive([2, 7, 5], [2, 5]))
    2

    >>> len(lcs2_naive([7], [1, 2, 3, 4]))
    0

    >>> len(lcs2_naive([2, 7, 8, 3], [5, 2, 8, 7]))
    2
    """
    a = [x for x in a if x in b]

    min_length = min(len(a), len(b))

    for n in range(min_length, 0, -1):
        a_combinations = combinations(a, n)
        for a_combination in a_combinations:
            b_combinations = combinations(b, n)
            for b_combination in b_combinations:
                if a_combination == b_combination:
                    return list(a_combination)

    return []


def lcs2_recursive(a: List[Number], b: List[Number]) -> int:
    """
    >>> lcs2([2, 7, 5], [2, 5])
    2

    >>> lcs2([7], [1, 2, 3, 4])
    0

    >>> lcs2([2, 7, 8, 3], [5, 2, 8, 7])
    2
    """
    m = len(a)
    n = len(b)

    if m == 0 or n == 0:
        return 0
    elif a[m - 1] == b[n - 1]:
        return 1 + lcs2_recursive(a[:-1], b[:-1])
    else:
        return max(lcs2_recursive(a[:-1], b), lcs2_recursive(a, b[:-1]))


def lcs2(a: List[Number], b: List[Number]) -> int:
    """
    >>> lcs2([2, 7, 5], [2, 5])
    2

    >>> lcs2([7], [1, 2, 3, 4])
    0

    >>> lcs2([2, 7, 8, 3], [5, 2, 8, 7])
    2
    """
    m = len(a)
    n = len(b)

    table = dict()

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i, j] = 0
            elif a[i - 1] == b[j - 1]:
                table[i, j] = 1 + table[i - 1, j - 1]
            else:
                table[i, j] = max(table[i - 1, j], table[i, j - 1])

    return table[m, n]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n_input = data[0]
    data = data[1:]
    a_input = data[:n_input]

    data = data[n_input:]
    m_input = data[0]
    data = data[1:]
    b_input = data[:m_input]

    print(lcs2(a_input, b_input))
