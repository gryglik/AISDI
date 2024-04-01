from heap import heapify, make_heap


def test_heapify_2_a_typical():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    heapify(2, 3, T)
    assert T == [None, 1, 2, 9, 7, 8, 3, 4, 5, 10, 12]


def test_heapify_5_a_typical():
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12]
    heapify(5, 2, T)
    assert T == [None, 1, 20, 3, 7, 15, 6, 2, 18, 19, 8, 9, 4, 5, 10, 12]


def test_heapify_5_a_leaf():
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12]
    heapify(5, 15, T)
    heapify(5, 4, T)
    heapify(5, 6, T)
    heapify(5, 12, T)
    assert T == [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12]


def test_heapify_5_a_incomplete():
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12]
    heapify(5, 3, T)
    assert T == [None, 1, 2, 12, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 3]


def test_heapify_7_a_typical():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    heapify(2, 3, T)
    assert T == [None, 1, 2, 9, 7, 8, 3, 4, 5, 10, 12]


def test_make_heap_2_a_typical():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    make_heap(2, T)
    assert T == [None, 12, 10, 9, 7, 8, 3, 4, 5, 1, 2]
