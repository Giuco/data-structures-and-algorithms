# Uses python3


def calc_fib_iterative(n):
    if n <= 1:
        return n

    t = 0, 1

    for i in range(2, n):
        t = t[1], sum(t)

    return sum(t)


def calc_fib_recursive(n):
    if n <= 1:
        return n

    return calc_fib_recursive(n - 1) + calc_fib_recursive(n - 2)


if __name__ == '__main__':
    n = int(input())
    # print(calc_fib_recursive(n))
    print(calc_fib_iterative(n))
