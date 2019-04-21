# Uses python3
import sys


def count_segments_efficient(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here
    return cnt


def count_segments_naive(starts, ends, points):
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

    count_output = count_segments_naive(starts_input, ends_input, points_input)
    for x in count_output:
        print(x, end=' ')
