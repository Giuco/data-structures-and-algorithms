#Uses python3

import sys


def digits_bigger_or_equal(a, b):
    a_first = int(str(a) + str(b))
    b_first = int(str(b) + str(a))

    return a_first >= b_first


def largest_number_usual(list_of_digits):
    result = ""

    while list_of_digits:
        max_digit = 0
        max_digit_i = 0

        for i, digit in enumerate(list_of_digits):
            if digits_bigger_or_equal(digit, max_digit):
                max_digit = digit
                max_digit_i = i

        result += str(max_digit)
        del list_of_digits[max_digit_i]

    return result


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = input_data.split()
    lq = data[1:]
    print(largest_number_usual(lq))

    # lq = [21, 2]
    # print(largest_number_usual(lq))
    # lq = [9, 4, 6, 1, 9]
    # print(largest_number_usual(lq))
    # lq = [23, 39, 92]
    # print(largest_number_usual(lq))

