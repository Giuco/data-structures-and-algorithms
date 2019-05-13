# Uses python3
from sys import stdin


def fibonacci_sum_efficient(n: int) -> int:
    sequence = [0, 1]

    while len(sequence) < 3 or not sequence[-2:] == [0, 1]:
        to_append = (sequence[-1] + sequence[-2]) % 10
        sequence.append(to_append)

    sequence = sequence[:-2]
    sequence = sequence[:(n % len(sequence) + 1)]

    sum_sequence = sum(map(lambda x: x ** 2, sequence))
    last_digit = sum_sequence % 10

    return last_digit


if __name__ == '__main__':
    n_input = int(stdin.read())
    print(fibonacci_sum_efficient(n_input))
