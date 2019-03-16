from fibonacci_last_digit import get_fibonacci_last_digit_efficient, get_fibonacci_last_digit_naive
from random import randint


def main():
    for i in range(1000):
        a = randint(0, 1000000)
        b = randint(0, 1000000)

        print('{} / {}'.format(a, b))

        eff_result = get_fibonacci_last_digit_efficient(a, b)
        nai_result = get_fibonacci_last_digit_naive(a, b)

        if eff_result != nai_result:
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break


if __name__ == '__main__':
    main()
