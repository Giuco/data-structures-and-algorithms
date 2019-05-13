# Uses python3
import sys


def fibonacci_sum_naive(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    total_sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total_sum += current

    return total_sum % 10


def fibonacci_sum_efficient(n: int) -> int:
    sequence = [0, 1]

    while len(sequence) < 3 or not sequence[-2:] == [0, 1]:
        to_append = (sequence[-1] + sequence[-2]) % 10
        sequence.append(to_append)

    sequence = sequence[:-2]
    sequence = sequence[:(n % len(sequence)+1)]

    sum_sequence = sum(sequence)
    last_digit = sum_sequence % 10

    return last_digit


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n_input = int(input_data)
    print(fibonacci_sum_efficient(n_input))
