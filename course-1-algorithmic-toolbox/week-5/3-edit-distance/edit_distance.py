# Uses python3
from functools import lru_cache


@lru_cache(maxsize=9999999999999)
def edit_distance_recursive(str_a: str, str_b: str) -> int:
    """
    >>> edit_distance_recursive("ab", "ab")
    0

    >>> edit_distance_recursive("short", "ports")
    3

    >>> edit_distance_recursive("editing", "distance")
    5
    """
    if len(str_a) == 0:
        return len(str_b)

    if len(str_b) == 0:
        return len(str_a)

    result = min(
        edit_distance_recursive(str_a[:-1], str_b)+1,
        edit_distance_recursive(str_a, str_b[:-1])+1,
        edit_distance_recursive(str_a[:-1], str_b[:-1]) + (str_a[-1] != str_b[-1]),
    )

    return result


def edit_distance(str_a: str, str_b: str) -> int:
    """
    >>> edit_distance("ab", "ab")
    0

    >>> edit_distance("short", "ports")
    3

    >>> edit_distance("editing", "distance")
    5
    """

    len_a = len(str_a) + 1
    len_b = len(str_b) + 1

    T = [
        [int()] * len_b
        for _ in range(len_a)
    ]

    for i in range(len_a):
        T[i][0] = i
    for j in range(len_b):
        T[0][j] = j

    for i in range(1, len_a):
        for j in range(1, len_b):
            insert_cost = T[i-1][j] + 1
            match_cost = T[i-1][j-1] + (str_a[i-1] != str_b[j-1])
            delete_cost = T[i][j-1] + 1

            node_cost = min(insert_cost, match_cost, delete_cost)

            T[i][j] = node_cost

    return T[len(str_a)][len(str_b)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
