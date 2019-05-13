from random import randint

from fibonacci_last_digit import get_fibonacci_last_digit_efficient, get_fibonacci_last_digit_naive


def main():
    for i in range(500):
        a = randint(0, 10000)

        eff_result = get_fibonacci_last_digit_efficient(a)
        nai_result = get_fibonacci_last_digit_naive(a)

        if eff_result != nai_result:
            print('{}'.format(a))
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break


if __name__ == '__main__':
    main()
