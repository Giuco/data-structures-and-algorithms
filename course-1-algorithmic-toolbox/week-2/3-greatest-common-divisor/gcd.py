# Uses python3
import sys


def is_prime(x: int) -> int:
    """Useless for current solution, but i'm not removing because it is cool"""
    for divisor in range(2, x-1):
        if x % divisor == 0:
            return False

    return True


def get_primes() -> int:
    """Same as the above"""
    i = 0

    while True:
        i += 1
        if is_prime(i):
            yield i


def gcd_efficient(a: int, b: int) -> int:
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


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_efficient(a, b))
