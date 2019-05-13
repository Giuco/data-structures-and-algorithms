# Uses python3
import sys
from math import inf
from typing import List


def get_change(total_amount_of_money: int, coin_denominations: List[int]) -> int:
    """
    >>> get_change(2, [4, 3, 1])
    2

    >>> get_change(6, [4, 3, 1])
    2

    >>> get_change(34, [3, 4, 1])
    9
    """
    n_coins = [inf] * (total_amount_of_money + 1)

    for money_subset in range(1, total_amount_of_money + 1):
        for coin in coin_denominations:
            if coin == money_subset:
                n_coins[money_subset] = 1
            elif coin < money_subset:
                n_coins[money_subset] = min(n_coins[money_subset - coin] + 1, n_coins[money_subset])

    return int(n_coins[total_amount_of_money])


if __name__ == '__main__':
    m_input = int(sys.stdin.read())
    coin_denominations_input = [4, 3, 1]
    print(get_change(m_input, coin_denominations_input))
