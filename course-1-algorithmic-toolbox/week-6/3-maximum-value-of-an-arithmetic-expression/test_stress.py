from random import randint
from statistics import mean
from time import time

from placing_parentheses import get_maximum_value_naive, get_maximum_value

MAX_LEN = 100
MAX_NUMBER = 9
NUMBER_OF_TESTS = 100


def generate_algebra_expression(max_len, max_number):
    operations = ["+", "-", "*"]
    expression_size = randint(3, max_len)
    expression = ""

    if expression_size % 2 == 0:
        expression_size += 1

    for i in range(expression_size):
        if i % 2 == 0:
            expression += str(randint(0, max_number))
        else:
            expression += operations[randint(0, 2)]

    return expression


def test_stress_count_segments():
    nai_time = list()
    eff_time = list()

    for _ in range(NUMBER_OF_TESTS):
        data = generate_algebra_expression(MAX_LEN, MAX_NUMBER)

        t = time()
        nai_result = get_maximum_value_naive(data)
        nai_time.append(time() - t)

        t = time()
        eff_result = get_maximum_value(data)
        eff_time.append(time() - t)

        assert eff_result == nai_result

    assert mean(eff_time) < mean(nai_time)

    print("\n")
    print(mean(eff_time))
    print(mean(nai_time))