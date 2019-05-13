from random import randint
from statistics import mean
from time import time

from fibonacci_huge import get_fibonacci_huge_efficient, get_fibonacci_huge_naive


def main():
    for i in range(1000):
        n = randint(1, (10 ** 5) + 1)
        m = randint(2, (10 ** 3) + 1)

        eff_time = list()
        nai_time = list()

        print('{} | {}'.format(m, n))

        st = time()
        eff_result = get_fibonacci_huge_efficient(n, m)
        eff_time.append(time() - st)

        st = time()
        nai_result = get_fibonacci_huge_naive(n, m)
        nai_time.append(time() - st)

        if nai_result != eff_result:
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break

    print("Naive Avg. Time: {:.10f} | Efficient Avg. Time: {:.10f}".format(mean(nai_time), mean(eff_time)))


if __name__ == '__main__':
    main()
