# Uses python3
import sys
from numbers import Number
from typing import List


def get_optimal_value(capacity: int, weights: List[int], values: List[int]) -> Number:
    total_value = 0.0

    weights_and_values = iter(
        sorted([(weight, value) for weight, value in zip(weights, values)], key=lambda x: x[1] / x[0], reverse=True))
    w_v = next(weights_and_values)

    while capacity > 0:
        if w_v[0] <= capacity:
            capacity -= w_v[0]
            total_value += w_v[1]
            try:
                w_v = next(weights_and_values)
            except StopIteration:
                break
        else:
            total_value += (capacity / w_v[0]) * w_v[1]
            capacity = 0

    return total_value


if __name__ == "__main__":
    data_input = list(map(int, sys.stdin.read().split()))
    n_input, capacity_input = data_input[0:2]
    values_input = data_input[2:(2 * n_input + 2):2]
    weights_input = data_input[3:(2 * n_input + 2):2]
    opt_value = get_optimal_value(capacity_input, weights_input, values_input)
    print("{:.10f}".format(opt_value))
