from majority_element import get_majority_element_divide_and_conquer, get_majority_element_naive
from random import randint

NUMBER_OF_TEST = 10000
LIST_SIZE = 10
N_MAX = 5


def test_stress_majority_element_divide_and_conquer():
    for _ in range(NUMBER_OF_TEST):
        array = [randint(0, N_MAX) for _ in range(LIST_SIZE)]

        assert get_majority_element_divide_and_conquer(array) == get_majority_element_naive(array), print(array)
