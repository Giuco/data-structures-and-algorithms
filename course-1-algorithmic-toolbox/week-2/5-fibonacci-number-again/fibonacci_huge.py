# python3
import sys


def get_fibonacci_huge_naive(n: int, m: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def is_recurring(l: list) -> bool:
    if len(l) < 3 or len(l) % 2 != 0:
        return False

    comb_1, comb_2 = l[:len(l) // 2], l[(len(l) // 2):]
    matches = [x1 == x2 for x1, x2 in zip(comb_1, comb_2)]

    return all(matches)


def get_fibonacci_huge_efficient(n: int, m: int) -> int:
    sequence = [0, 1]

    while len(sequence) < 3 or not sequence[-2:] == [0, 1]:
        to_append = (sequence[-1] + sequence[-2]) % m
        sequence.append(to_append)

    sequence = sequence[:-2]

    return sequence[n % len(sequence)]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n_data, m_input = map(int, input_data.split())
    print(get_fibonacci_huge_efficient(n_data, m_input))
