# Uses python3


def calc_fib_iterative(n: int) -> int:
    """
    >>> calc_fib_iterative(5)
    5

    >>> calc_fib_iterative(7)
    13
    """
    previous, current = 0, 1

    for _ in range(2, n):
        previous, current = current, previous + current

    return previous + current


def calc_fib_recursive(n: int) -> int:
    """
    >>> calc_fib_iterative(5)
    5

    >>> calc_fib_iterative(7)
    13
    """
    if n <= 1:
        return n

    return calc_fib_recursive(n - 1) + calc_fib_recursive(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(calc_fib_iterative(n))
