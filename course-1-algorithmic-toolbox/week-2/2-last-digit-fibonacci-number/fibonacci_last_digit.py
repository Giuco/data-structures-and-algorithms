# Uses python3
import sys


def get_fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = int(str(current)[-1]), int(str(previous)[-1]) + int(str(current)[-1])

    return int(str(current)[-1])


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n = int(input_)
    print(get_fibonacci_last_digit_efficient(n))
