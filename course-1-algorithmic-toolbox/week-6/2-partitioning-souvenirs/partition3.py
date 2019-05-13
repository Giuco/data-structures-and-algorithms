# Uses python3
import sys
from itertools import product


def partition3(a):
    """
    >>> partition3([3, 3, 3, 3])
    0

    >>> partition3([40])
    0

    >>> partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])
    1

    >>> partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    1
    """
    for c in product(range(3), repeat=len(a)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(a[k] for k in range(len(a)) if c[k] == i)

        if sums[0] == sums[1] == sums[2]:
            return 1

    return 0


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a_input = list(map(int, input_data.split()))
    print(partition3(a_input))
