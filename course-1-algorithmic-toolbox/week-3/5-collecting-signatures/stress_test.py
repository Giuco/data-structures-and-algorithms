from covering_segments import optimal_points_naive, optimal_points_efficient, Segment
from random import randint
from time import time
from statistics import mean

NUMBER_TESTS = 100
MAX_NUMBER_SEGMENTS = 30
MAX_POSSIBLE_POINT = 30


def main():
    for _ in range(NUMBER_TESTS):
        n = randint(1, MAX_NUMBER_SEGMENTS)

        input_segments = list()
        for _ in range(n):
            start = randint(1, MAX_POSSIBLE_POINT - 1)
            end = randint(start, MAX_POSSIBLE_POINT)

            input_segments.append(Segment(start, end))

        eff_time, nai_time = list(), list()

        st = time()
        eff_result = optimal_points_efficient(input_segments)
        eff_time.append(time() - st)

        st = time()
        nai_result = optimal_points_naive(input_segments)
        nai_time.append(time() - st)

        if len(nai_result) != len(eff_result):
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break

    print("Naive Avg. Time: {:.10f} | Efficient Avg. Time: {:.10f}".format(mean(nai_time), mean(eff_time)))


if __name__ == '__main__':
    main()
