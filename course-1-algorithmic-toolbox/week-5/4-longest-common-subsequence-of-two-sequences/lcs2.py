# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    return min(len(a), len(b))


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n = data[0]
    data = data[1:]
    a_input = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b_input = data[:m]

    print(lcs2(a_input, b_input))
