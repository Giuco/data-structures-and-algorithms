# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    total_value = 0.0

    weights_and_values = iter(sorted([(weight, value) for weight, value in zip(weights, values)], key=lambda x: x[1]/x[0], reverse=True))
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
            total_value += (capacity/w_v[0]) * w_v[1]
            capacity = 0

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # capacity = 50
    # values = [60, 100, 120]
    # weights = [20, 50, 30]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
