from fibonacci_last_digit import get_fibonacci_last_digit_efficient, get_fibonacci_last_digit_naive
from random import randint


def main():
    for i in range(500):
        a = randint(0, 10000)
        print('{}'.format(a))

        eff_result = get_fibonacci_last_digit_efficient(a)
        nai_result = get_fibonacci_last_digit_naive(a)

        if eff_result != nai_result:
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break


if __name__ == '__main__':
    main()
