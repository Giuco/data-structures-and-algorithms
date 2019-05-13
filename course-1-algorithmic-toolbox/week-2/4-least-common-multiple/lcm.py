# Uses python3
import sys


def lcm_naive(a, b) -> int:
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_efficient_1(a: int, b: int) -> int:

    a_mult = 1
    b_mult = 1

    while True:

        if a_mult*a == b_mult*b:
            return a_mult*a
        elif a_mult*a > b_mult*b:
            b_mult += 1
        else:
            a_mult += 1


def gcd(a: int, b: int) -> int:
    if a == 0:
        return 1

    if b == 0:
        raise ZeroDivisionError

    min_arg = min(a, b)
    max_arg = max(a, b)

    while True:
        remainder = max_arg % min_arg

        if remainder == 0:
            return min_arg

        max_arg = min_arg
        min_arg = remainder


def lcm_efficient_2(a: int, b: int) -> int:
    return int((a*b) // gcd(a, b))


if __name__ == '__main__':
    input_data = sys.stdin.read()
    a_input, b_input = map(int, input_data.split())
    print(lcm_efficient_2(a_input, b_input))
