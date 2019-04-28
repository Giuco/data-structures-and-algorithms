# Uses python3
import sys


COIN_DENOMINATIONS = [4, 3, 1]


def get_change(m):
    """
    >>> get_change(2)
    2
    >>> get_change(34)
    9
    """

    return m // 4


if __name__ == '__main__':
    m_input = int(sys.stdin.read())
    print(get_change(m_input))
