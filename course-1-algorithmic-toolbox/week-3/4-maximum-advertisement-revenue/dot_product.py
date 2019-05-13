# Uses python3

import sys
from typing import List


def max_dot_product(a: List[int], b: List[int]) -> int:
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    total_revenue = sum([c * d for c, d in zip(a, b)])

    return total_revenue


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n_input = data[0]
    a_input = data[1:(n_input + 1)]
    b_input = data[(n_input + 1):]
    print(max_dot_product(a_input, b_input))
