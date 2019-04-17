from binary_search import binary_search, linear_search


def test_binary_search_1():
    l = [1, 2, 3, 4, 5]
    p_to_find = [1, 3, 5, 6]

    for p in p_to_find:
        assert binary_search(l, p) == linear_search(l, p)


def test_binary_search_2():
    l = [1, 5, 8, 12, 13]
    p_to_find = [8, 1, 23, 1, 11]

    for p in p_to_find:
        assert binary_search(l, p) == linear_search(l, p)

