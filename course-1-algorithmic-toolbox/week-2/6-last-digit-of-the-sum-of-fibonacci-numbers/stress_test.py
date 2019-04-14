from fibonacci_sum_last_digit import fibonacci_sum_naive, fibonacci_sum_efficient
from random import randint
from time import time
from statistics import mean

NUMBER_OF_TEST = 1000
N_MAX = 1000


def main():
    for i in range(NUMBER_OF_TEST):
        n = randint(0, N_MAX)

        eff_time = list()
        nai_time = list()

        print('{}'.format(n))

        st = time()
        eff_result = fibonacci_sum_efficient(n)
        eff_time.append(time() - st)

        st = time()
        nai_result = fibonacci_sum_naive(n)
        nai_time.append(time() - st)

        if nai_result != eff_result:
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break

    print("Naive Avg. Time: {:.10f} | Efficient Avg. Time: {:.10f}".format(mean(nai_time), mean(eff_time)))


if __name__ == '__main__':
    main()
