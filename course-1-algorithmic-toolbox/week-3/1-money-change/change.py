# Uses python3
import sys


def get_change(change):
    coin_sizes = iter((10, 5, 1))
    coin_size = next(coin_sizes)
    n_coins = 0

    while change > 0:
        if change >= coin_size:
            change -= coin_size
            n_coins += 1
        else:
            coin_size = next(coin_sizes)

    return n_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 28
    print(get_change(m))
