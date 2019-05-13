from random import randint
from statistics import mean
from time import time

from lcm import lcm_efficient_1, lcm_efficient_2


def main():
    for i in range(100):
        a = randint(0, 10000000)
        b = randint(0, 10000000)

        eff_1_time = list()
        eff_2_time = list()
        naive_time = list()

        print('{} | {}'.format(a, b))

        st = time()
        eff_1_result = lcm_efficient_1(a, b)
        eff_1_time.append(time() - st)

        st = time()
        eff_2_result = lcm_efficient_2(a, b)
        eff_2_time.append(time() - st)

        # st = time()
        # naive_result = lcm_naive(a, b)
        # naive_time.append(time() - st)

        if eff_2_result != eff_1_result:
            print("Efficient 1 Result: {} \t\t Efficient 2 Result {}".format(eff_1_result,
                                                                             eff_2_result))
            break

    print("Efficient 1 Avg. Time: {:.10f} | Efficient 2 Avg. Time: {:.10f}".format(mean(eff_1_time), mean(eff_2_time)))

    #     if eff_2_result != naive_result or eff_2_result != eff_1_result:
    #         print("Naive Result: {} \t\t Efficient 1 Result: {} \t\t Efficient 2 Result {}".format(naive_result,
    #                                                                                                eff_1_result,
    #                                                                                                eff_2_result))
    #         break
    #
    # print("Naive Avg. Time: {:.10f} | Efficient 1 Avg. Time: {:.10f} | Efficient 2 Avg. Time: {:.10f}".format(
    #     mean(naive_time), mean(eff_1_time), mean(eff_2_time)))


if __name__ == '__main__':
    main()
