# Uses python3
import sys
from typing import List


def optimal_sequence_naive(n: int) -> List[int]:
    sequence = list()
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return list(reversed(sequence))


def optimal_sequence(big_number: int) -> List[int]:
    """
    >>> optimal_sequence(1)
    [1]

    >>> optimal_sequence(5)
    [1, 2, 4, 5]

    >>> optimal_sequence(96234)
    [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
    """
    table = list()
    table.append(0)

    for sub_number in range(1, big_number+1):
        table.append(float("inf"))
        if sub_number % 3 == 0:
            table[sub_number] = 1 + table[sub_number//3]

        if sub_number % 2 == 0 and table[sub_number//2]+1 < table[sub_number]:
            table[sub_number] = 1 + table[sub_number//2]

        if table[sub_number-1]+1 < table[sub_number]:
            table[sub_number] = table[sub_number-1]+1

    return reconstruct_optimal_sequence(table, big_number)


def reconstruct_optimal_sequence(table: List[int], n) -> List[int]:
    seq_table = list()

    while n > 1:
        seq_table.append(n)
        if n % 3 == 0 and table[n//3] == table[n] - 1:
            n = n//3
        elif n % 2 == 0 and table[n//2] == table[n] - 1:
            n = n//2
        elif table[n-1] == (table[n] - 1):
            n -= 1

    seq_table.append(1)

    return list(reversed(seq_table))


if __name__ == "__main__":
    input_data = sys.stdin.read()
    n_input = int(input_data)
    sequence_input = list(optimal_sequence(n_input))
    print(len(sequence_input) - 1)
    for x in sequence_input:
        print(x, end=' ')
