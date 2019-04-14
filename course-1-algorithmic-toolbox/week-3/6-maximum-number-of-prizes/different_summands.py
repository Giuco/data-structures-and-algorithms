# Uses python3
import sys


def optimal_summands_naive(n):
    partition = []
    step = 1
    while n > 2*step:
        partition.append(step)
        n = n - step
        step += 1
    partition.append(n)
    return partition


if __name__ == '__main__':
    input_data = sys.stdin.read()
    # input_data = 6

    n_input = int(input_data)
    summands_input = optimal_summands_naive(n_input)
    print(len(summands_input))
    for x in summands_input:
        print(x, end=' ')
