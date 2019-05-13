from gcd import gcd_efficient, gcd_naive
from random import randint


def main():
    for i in range(1000):
        a = randint(0, 1000000)
        b = randint(1, 1000000)

        eff_result = gcd_efficient(a, b)
        nai_result = gcd_naive(a, b)

        if eff_result != nai_result:
            print('{} / {}'.format(a, b))
            print("Naive Result: {} \t\t Efficient Result: {}".format(nai_result, eff_result))
            break


if __name__ == '__main__':
    main()
