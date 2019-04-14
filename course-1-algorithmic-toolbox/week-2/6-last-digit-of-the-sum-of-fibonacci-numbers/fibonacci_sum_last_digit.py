# Uses python3
import sys


def fibonacci_sum_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_fibonacci_huge_efficient(n: int, m: int) -> int:
    sequence = [0, 1]

    while len(sequence) < 3 or not sequence[-2:] == [0, 1]:
        to_append = (sequence[-1] + sequence[-2]) % m
        sequence.append(to_append)

    sequence = sequence[:-2]

    return sequence[n % len(sequence)]


def fibonacci_sum_efficient(n: int) -> int:
    sum_n = sum(range(0, n+1))

    return get_fibonacci_huge_efficient(sum_n, 10)


if __name__ == '__main__':
    # input_data = sys.stdin.read()
    # n_input = int(input_data)

    n_input = 263

    print(fibonacci_sum_efficient(n_input))
    print(fibonacci_sum_naive(n_input))
