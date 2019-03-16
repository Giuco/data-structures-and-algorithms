# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci(n):
    if n <= 1:
        return n

    t = 0, 1

    for i in range(2, n):
        t = t[1], sum(t)

    return sum(t)


def is_recurring(l: list) -> bool:
    if len(l) < 3 or len(l) % 2 != 0:
        return False

    comb_1, comb_2 = l[:len(l) // 2], l[(len(l) // 2):]
    matches = [x1 == x2 for x1, x2 in zip(comb_1, comb_2)]

    return all(matches)


def get_fibonacci_huge_efficient(n: int, m: int) -> int:
    i = 0
    fib_mod = list()

    while not is_recurring(fib_mod):
        fib_mod.append(get_fibonacci(i) % m)
        i += 1

    periodic_mod = fib_mod[:len(fib_mod) // 2]

    return periodic_mod[n % len(periodic_mod)]


# def get_fibonacci_last_digit_efficient(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#
#     for _ in range(n - 1):
#         previous, current = int(str(current)[-1]), int(str(previous)[-1]) + int(str(current)[-1])
#
#     return int(str(current)[-1])


# def get_fibonacci_huge_efficient(n: int, m: int) -> int:
#     i = 0
#     fib_mod = list()
#
#     while not is_recurring(fib_mod):
#         fib_mod.append(get_fibonacci_last_digit_efficient(i) % m)
#         i += 1
#
#     periodic_mod = fib_mod[:len(fib_mod) // 2]
#
#     return periodic_mod[n % len(periodic_mod)]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
