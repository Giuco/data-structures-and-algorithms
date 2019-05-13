from inversions import get_number_of_inversions


def test_get_number_of_inversion_1():
    input_list = [2, 3, 9, 2, 9]

    assert get_number_of_inversions(input_list) == 2


def test_get_number_of_inversions_2():
    input_list = [1, 20, 6, 4, 5]

    assert get_number_of_inversions(input_list) == 5


def test_get_number_of_inversions_3():
    input_list = [1, 2, 3, 4, 5]

    assert get_number_of_inversions(input_list) == 0


def test_get_number_of_inversion_4():
    input_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    len_list = len(input_list)
    answer = len_list * ((len_list - 1) / 2)

    assert get_number_of_inversions(input_list) == answer
