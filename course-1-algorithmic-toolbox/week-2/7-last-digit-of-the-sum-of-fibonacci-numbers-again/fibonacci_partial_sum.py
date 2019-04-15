# Uses python3
import sys


def fibonacci_partial_sum_efficient(start: int, end: int) -> int:
    sequence = [0, 1]

    while len(sequence) < 3 or not sequence[-2:] == [0, 1]:
        to_append = (sequence[-1] + sequence[-2]) % 10
        sequence.append(to_append)

    sequence = sequence[:-2]

    start_index = start % len(sequence)
    end_index = (end % len(sequence) + 1)

    sequence = sequence[start_index:end_index]

    sum_sequence = sum(sequence)
    last_digit = sum_sequence % 10

    return last_digit


if __name__ == '__main__':
    input_data = sys.stdin.read()
    start_input, end_input = map(int, input_data.split())

    # start_input, end_input = 1234, 12345

    print(fibonacci_partial_sum_efficient(start_input, end_input))
