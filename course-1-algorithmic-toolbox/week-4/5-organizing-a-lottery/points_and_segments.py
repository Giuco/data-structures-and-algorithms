# Uses python3
import sys
from typing import List


def count_segments_efficient(starts: List[int], ends: List[int], points_list: List[int]):
    """
    >>> count_segments_efficient([2, 0], [3, 5], [1, 6, 11])
    [1, 0, 0]

    >>> count_segments_efficient([1, -10], [3, 10], [-100, 100, 0])
    [0, 0, 1]

    >>> count_segments_efficient([3, 0, -3, 7], [2, 5, 2, 10], [1, 6])
    [2, 0]
    """
    cnt = {}

    array = [(start, 0) for start in starts] + \
            [(end, 2) for end in ends] + \
            [(point, 1) for point in points_list]

    array = sorted(array)

    charge = 0
    for p, ob in array:
        if ob == 0:
            charge += 1
        elif ob == 2:
            charge -= 1
        else:
            cnt[p] = charge

    result = list()
    for p in points_list:
        result.append(cnt[p])

    return result


def count_segments_naive(starts: List[int], ends: List[int], points: List[int]):
    """
    >>> count_segments_naive([2, 0], [3, 5], [1, 6, 11])
    [1, 0, 0]

    >>> count_segments_naive([1, -10], [3, 10], [-100, 100, 0])
    [0, 0, 1]

    >>> count_segments_naive([3, 0, -3, 7], [2, 5, 2, 10], [1, 6])
    [2, 0]
    """
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n = data[0]
    m = data[1]

    starts_input = data[2:2 * n + 2:2]
    ends_input = data[3:2 * n + 2:2]
    points_input = data[2 * n + 2:]

    count_output = count_segments_efficient(starts_input, ends_input, points_input)
    for x in count_output:
        print(x, end=' ')
