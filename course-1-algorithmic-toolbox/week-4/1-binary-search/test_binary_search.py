from binary_search import binary_search, linear_search


def test_binary_search_1():
    lq = [1, 2, 3, 4, 5]
    p_to_find = [1, 3, 5, 6]

    for p in p_to_find:
        assert binary_search(lq, p) == linear_search(lq, p)


def test_binary_search_2():
    lq = [1, 5, 8, 12, 13]
    p_to_find = [8, 1, 23, 1, 11]

    for p in p_to_find:
        assert binary_search(lq, p) == linear_search(lq, p)
