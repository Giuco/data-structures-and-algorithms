from random import randint
from statistics import mean
from time import time

from fibonacci_sum_last_digit import fibonacci_sum_efficient, fibonacci_sum_naive

NUMBER_OF_TEST = 100
N_MAX = 10000


def main():
    for i in range(NUMBER_OF_TEST):
        n = randint(0, N_MAX)

        eff_time = list()
        nai_time = list()

        st = time()
        eff_result = fibonacci_sum_efficient(n)
        eff_time.append(time() - st)

        st = time()
        nai_result = fibonacci_sum_naive(n)
        nai_time.append(time() - st)

        if nai_result != eff_result:
            print(n)
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break

    print("Naive Avg. Time: {:.10f} | Efficient Avg. Time: {:.10f}".format(mean(nai_time), mean(eff_time)))


if __name__ == '__main__':
    main()
