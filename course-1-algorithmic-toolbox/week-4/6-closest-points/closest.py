# Uses python3
import sys

from bisect import bisect_left, bisect_right
from itertools import combinations
from math import hypot
from operator import itemgetter
from typing import Tuple, List

_Y_COORD = itemgetter(1)


def distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    return hypot(p[0] - q[0], p[1] - q[1])


def closest_distance(p_points: List[Tuple[float, float]]) -> float:
    """
    >>> closest_distance([(0, 0), (3, 4)])
    5.0

    >>> closest_distance([(7, 7), (1, 100), (4, 8), (7, 7)])
    0.0

    >>> closest_distance([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)])
    1.4142135623730951
    """
    p_points = sorted(p_points)
    px = [x for x, _ in p_points]

    def _closest(start, stop):
        if stop - start <= 8:
            return min(distance(p, q) for p, q in combinations(p_points[start:stop], 2))

        mid = (start + stop) // 2
        dist = min(_closest(start, mid), _closest(mid, stop))

        mid_x = px[mid]
        left = bisect_left(px, mid_x - dist, lo=start, hi=mid)
        right = bisect_right(px, mid_x + dist, lo=mid, hi=stop)
        strip = sorted(p_points[mid:right], key=_Y_COORD)
        strip_y = list(map(_Y_COORD, strip))

        for p in p_points[left:mid]:
            y = p[1]
            left = bisect_left(strip_y, y - dist)
            right = bisect_right(strip_y, y + dist)
            assert right - left <= 6
            for q in strip[left:right]:
                dist = min(dist, distance(p, q))

        return dist

    return _closest(0, len(p_points))


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n_input = data[0]
    x_input = data[1::2]
    y_input = data[2::2]

    points_input = list(zip(x_input, y_input))

    print("{0:.9f}".format(closest_distance(points_input)))
