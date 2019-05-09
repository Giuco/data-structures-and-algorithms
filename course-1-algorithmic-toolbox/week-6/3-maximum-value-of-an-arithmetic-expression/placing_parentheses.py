# Uses python3
from numbers import Number
from typing import Union


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


def get_maximum_value(data: str):
    elements = map(convert_to_number_if_possible, data.split())


if __name__ == "__main__":
    print(get_maximum_value(input()))
