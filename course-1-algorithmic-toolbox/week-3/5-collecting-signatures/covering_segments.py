# Uses python3
import sys
from collections import namedtuple
from itertools import combinations
from typing import List

Segment = namedtuple('Segment', 'start end')


def is_point_inside_segment(segment: Segment, point: float) -> bool:
    return segment.start <= point <= segment.end


def is_segment_covered(segment: Segment, list_of_points: List[float]) -> bool:
    covered = False

    for point in list_of_points:
        if is_point_inside_segment(segment, point):
            covered = True
            break

    return covered


def is_combination_covering_all_segments(segments: List[Segment], list_of_points: List[float]) -> bool:
    covered = True

    for segment in segments:
        if not is_segment_covered(segment, list_of_points):
            covered = False
            break

    return covered


def optimal_points_naive(segments: List[Segment]) -> List[float]:
    min_point = 1
    max_point = max([x.end for x in segments])

    all_possible_points = range(min_point, max_point+1)

    right_combination = None

    for number_of_points in all_possible_points:
        all_possible_combinations = combinations(all_possible_points, number_of_points)

        for possible_combination in iter(reversed(list(all_possible_combinations))):
            if is_combination_covering_all_segments(segments, possible_combination):
                right_combination = possible_combination
                break

        if right_combination:
            break

    return right_combination


def optimal_points_efficient(segments: List[Segment]) -> List[float]:
    segments = iter(sorted(segments, key=lambda x: x.end))
    segment = next(segments)
    maximum_point = segment.end
    right_combination = list()

    while True:
        try:
            if not is_point_inside_segment(segment, maximum_point):
                right_combination.append(maximum_point)
                maximum_point = segment.end
            else:
                segment = next(segments)
        except StopIteration:
            break

    right_combination.append(maximum_point)

    return right_combination


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *data = map(int, input_data.split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    output_points = optimal_points_efficient(input_segments)

    print(len(output_points))
    for p in output_points:
        print(p, end=' ')
