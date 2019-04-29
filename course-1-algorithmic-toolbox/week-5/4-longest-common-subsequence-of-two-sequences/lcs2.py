# Uses python3

import sys
from numbers import Number
from typing import List, Tuple


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
            reconstructed_lis.append(arr[-(idx+1)])

    return list(reversed(reconstructed_lis))


def lcs2(a, b):
    # write your code here
    return min(len(a), len(b))


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
