# Uses python3
import sys


def minimum_distance(x, y):
    raise NotImplementedError


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance(x, y)))
