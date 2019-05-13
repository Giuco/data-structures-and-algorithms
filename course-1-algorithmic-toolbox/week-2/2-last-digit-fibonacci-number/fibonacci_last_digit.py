# Uses python3
import sys


def get_last_digit(x: int) -> int:
    return int(str(x)[-1])


def get_fibonacci_last_digit_efficient(n: int) -> int:
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, get_last_digit(previous + current)

    return current


def get_fibonacci_last_digit_naive(n: int) -> int:
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n_input = int(input_)
    print(get_fibonacci_last_digit_efficient(n_input))
