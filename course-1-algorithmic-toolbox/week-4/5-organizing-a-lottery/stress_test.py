from random import randint
from statistics import mean
from time import time

from points_and_segments import count_segments_efficient, count_segments_naive

NUMBER_OF_TEST = 100
MAX_POINT = 500
MAX_SEGMENTS = 1000


def test_stress_count_segments():
    nai_time = list()
    eff_time = list()

    for _ in range(NUMBER_OF_TEST):
        starts = [randint(-MAX_POINT, MAX_POINT) for _ in range(MAX_SEGMENTS + 1)]
        ends = [randint(start, MAX_POINT) for start in starts]
        points = list(set([randint(-MAX_POINT, MAX_POINT) for _ in range(MAX_SEGMENTS + 1)]))

        t = time()
        nai_result = count_segments_naive(starts, ends, points)
        nai_time.append(time() - t)

        t = time()
        eff_result = count_segments_efficient(starts, ends, points)
        eff_time.append(time() - t)

        assert len(eff_result) == len(nai_result)
        assert sorted(eff_result) == sorted(nai_result)

    assert mean(eff_time) < mean(nai_time)
    print("\n")
    print(mean(eff_time))
    print(mean(nai_time))
