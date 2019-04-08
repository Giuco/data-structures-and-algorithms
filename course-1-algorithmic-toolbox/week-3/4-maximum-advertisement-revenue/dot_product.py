#Uses python3

import sys


def max_dot_product(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    total_revenue = sum([c*d for c, d in zip(a, b)])

    return total_revenue


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]

    # a, b = [1, 3, -5], [-2, 4, 1]

    print(max_dot_product(a, b))

