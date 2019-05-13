# Uses python3
from copy import deepcopy
from typing import List, Union, Tuple


def eval_operation(a: int, b: int, op: str) -> int:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Not supported operation")


def string_to_ops(data: str) -> List[Union[str, int]]:
    return list(map(lambda x: int(x) if x.isdecimal() else x, list(data)))


def get_all_possible_values(data: List[Union[str, int]]) -> List[int]:
    if len(data) == 1:
        return data

    possible_values = list()

    for e in range(len(data)):
        if isinstance(data[e], str):
            left_results = get_all_possible_values(data[:e])
            right_results = get_all_possible_values(data[e + 1:])

            for i in range(len(left_results)):
                for j in range(len(right_results)):
                    possible_values.append(eval_operation(left_results[i], right_results[j], data[e]))

    return possible_values


def get_maximum_value_naive(data: str) -> int:
    """
    >>> get_maximum_value_naive("1+5")
    6

    >>> get_maximum_value_naive("5-8+7*4-8+9")
    200
    """
    copied_data = deepcopy(data)
    copied_data = string_to_ops(copied_data)
    return max(get_all_possible_values(copied_data))


def get_min_max(j: int, p: int, operations: List[str],
                table_min: List[List[int]], table_max: List[List[int]]) -> Tuple[int, int]:
    min_number = float("inf")
    max_number = float("-inf")

    for k in range(j, p):
        a = eval_operation(table_max[j][k], table_max[k + 1][p], operations[k])
        b = eval_operation(table_max[j][k], table_min[k + 1][p], operations[k])
        c = eval_operation(table_min[j][k], table_max[k + 1][p], operations[k])
        d = eval_operation(table_min[j][k], table_min[k + 1][p], operations[k])

        min_number = min(min_number, a, b, c, d)
        max_number = max(max_number, a, b, c, d)

    return min_number, max_number


def get_maximum_value(data: str) -> int:
    """
    >>> get_maximum_value("1+5")
    6

    >>> get_maximum_value("5-8+7*4-8+9")
    200
    """
    copied_data = deepcopy(data)
    copied_data = string_to_ops(copied_data)
    operations = list(filter(lambda x: isinstance(x, str), copied_data))
    numbers = list(filter(lambda x: isinstance(x, int), copied_data))
    n_numbers = len(numbers)

    table_min = [[0 for _ in range(n_numbers)] for _ in range(n_numbers)]
    table_max = [[0 for _ in range(n_numbers)] for _ in range(n_numbers)]

    for i, number in enumerate(numbers):
        table_max[i][i] = number
        table_min[i][i] = number

    for i in range(1, n_numbers):
        for j in range(0, n_numbers - i):
            p = i + j
            table_min[j][p], table_max[j][p] = get_min_max(j, p, operations, table_min, table_max)

    return table_max[0][n_numbers-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
