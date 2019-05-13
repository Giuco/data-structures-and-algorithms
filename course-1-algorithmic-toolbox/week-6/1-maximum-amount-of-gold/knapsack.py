# Uses python3
import sys


def optimal_weight(total_weight, bars):
    """
    >>> optimal_weight(10, [1, 4, 8])
    9
    """
    bars = [0] + bars

    table = [[0] * (total_weight + 1) for _ in range(len(bars))]

    for i in range(1, len(bars)):
        for w in range(1, total_weight + 1):
            table[i][w] = table[i - 1][w]
            if bars[i] <= w:
                val = table[i - 1][w - bars[i]] + bars[i]
                if table[i][w] < val:
                    table[i][w] = val

    return table[len(bars) - 1][total_weight]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    W, n, *w = list(map(int, input_data.split()))
    print(optimal_weight(W, w))
