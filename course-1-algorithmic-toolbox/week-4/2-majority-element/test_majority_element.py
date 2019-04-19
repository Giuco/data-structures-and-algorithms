from majority_element import get_majority_element


def test_get_majority_element_basic():
    a_input = [2, 3, 9, 2, 2]
    b_input = [1, 2, 3, 4]
    c_input = [1, 2, 3, 1]

    assert get_majority_element(a_input) == 1
    assert get_majority_element(b_input) == 0
    assert get_majority_element(c_input) == 0


def test_get_majority_element_bigint_input():
    a_input = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]

    assert get_majority_element(a_input) == 0