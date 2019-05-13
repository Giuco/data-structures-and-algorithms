# Uses python3
import sys
from typing import List


def optimal_summands_naive(n: int) -> List[int]:
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
    n_input = int(input_data)
    summands_input = optimal_summands_naive(n_input)

    print(len(summands_input))
    for x in summands_input:
        print(x, end=' ')
