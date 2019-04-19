# Uses python3
import sys
from typing import List


def get_majority_element(a: List[int]) -> int:
    count_of_n = {}

    for u in a:
        if u not in count_of_n:
            count_of_n[u] = 1
        else:
            count_of_n[u] += 1

    output = 1 if max(list(count_of_n.values())) > len(a) / 2 else 0

    return output


if __name__ == '__main__':
    input_data = sys.stdin.read()
    _, *a_input = list(map(int, input_data.split()))

    print(get_majority_element(a_input))
