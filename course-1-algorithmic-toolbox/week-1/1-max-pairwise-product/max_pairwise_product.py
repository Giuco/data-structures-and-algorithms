# python3
from typing import List


def max_pairwise_product_original(numbers: List[int]) -> int:
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product(numbers: List[int]) -> int:
    biggest = float("-inf")
    biggest_2 = float("-inf")

    for number in numbers:
        if number >= biggest:
            biggest_2 = biggest
            biggest = number
        elif number >= biggest_2:
            biggest_2 = number

    return biggest_2 * biggest


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
