from heap import heapify, make_heap


def test_heapify_2_a_typical():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    heapify(2, 3, T)
    assert T == [None, 1, 2, 9, 7, 8, 3, 4, 5, 10, 12]


def test_heapify_2_a_leaf():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    heapify(2, 6, T)
    heapify(2, 7, T)
    heapify(2, 8, T)
    heapify(2, 9, T)
    heapify(2, 10, T)
    assert T == [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]


def test_heapify_2_a_incomplete():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    heapify(2, 5, T)
    assert T == [None, 1, 2, 3, 7, 12, 9, 4, 5, 10, 8]


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
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 31]
    heapify(7, 2, T)
    assert T == [None, 1, 19, 3, 7, 15, 6, 20, 18, 2, 8, 9, 4, 5, 10, 12, 31]


def test_heapify_7_a_leaf():
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 31]
    heapify(7, 4, T)
    heapify(7, 8, T)
    heapify(7, 9, T)
    heapify(7, 15, T)
    heapify(7, 16, T)
    assert T == [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 31]


def test_heapify_7_a_incomplete():
    T = [None, 1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 31]
    heapify(7, 3, T)
    assert T == [None, 1, 2, 31, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 3]


def test_make_heap_2_a_typical():
    T = [None, 1, 2, 3, 7, 8, 9, 4, 5, 10, 12]
    make_heap(2, T)
    assert T == [None, 12, 10, 9, 7, 8, 3, 4, 5, 1, 2]
