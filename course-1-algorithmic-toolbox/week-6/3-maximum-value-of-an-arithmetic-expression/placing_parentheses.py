# Uses python3
from numbers import Number
from typing import Union, List, Tuple


def eval_operation(a: Number, b: Number, op: str) -> Number:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Not supported operation")


def convert_to_number_if_possible(string: str) -> Union[str, Number]:
    try:
        as_float = float(string)
        return int(as_float) if as_float.is_integer() else as_float
    except ValueError:
        return string.strip()


def string_to_ops_and_numbers(data: str) -> Tuple[List[Number], List[str]]:
    elements = list(map(convert_to_number_if_possible, data.split()))
    numbers = elements[0::2]
    operations = elements[1::2]

    return numbers, operations


def get_maximum_value(data: str) -> Number:
    numbers, operations = string_to_ops_and_numbers(data)

    min_table = [[0] * len(numbers)] * len(numbers)
    max_table = [[0] * len(numbers)] * len(numbers)

    for i in range(len(numbers)):
        min_table[i][i] = numbers[i]
        max_table[i][i] = numbers[i]


if __name__ == "__main__":
    print(get_maximum_value(input()))
