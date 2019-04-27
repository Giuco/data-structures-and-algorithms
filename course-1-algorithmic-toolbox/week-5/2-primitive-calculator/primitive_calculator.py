# Uses python3
import sys


def optimal_sequence(n):
    sequence = list()
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


if __name__ == "__main":
    input_data = sys.stdin.read()
    n_input = int(input_data)
    sequence_input = list(optimal_sequence(n_input))
    print(len(sequence_input) - 1)
    for x in sequence_input:
        print(x, end=' ')
