# Uses python3

import sys


def lcs3(a, b, c):
    # write your code here
    return min(len(a), len(b), len(c))


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
