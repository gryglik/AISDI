from heap import Heap


def test_heapify_2_a_typical():
    heap = Heap(2, [1, 2, 3, 7, 8, 9, 4, 5, 10, 12])
    assert heap.list() == [None, 12, 10, 9, 7, 8, 3, 4, 5, 1, 2]


def test_heapify_5_a_typical():
    heap = Heap(5, [1, 2, 3, 7, 8, 9, 4, 5, 10, 12])
    assert heap.list() == [None, 12, 10, 3, 7, 8, 9, 4, 5, 1, 2]


def test_heapify_7_a_typical():
    heap = Heap(7, [1, 2, 3, 7, 15, 6, 20, 18, 19, 8, 9, 4, 5, 10, 12, 31])
    assert heap.list() == [None, 31, 19, 3, 7, 15, 6, 20, 18, 2, 8, 9, 4, 5, 10, 12, 1]


def test_add_2_a_typical():
    heap = Heap(2, [1, 2, 3, 7, 8, 9, 4, 5, 10, 12])
    assert heap.list() == [None, 12, 10, 9, 7, 8, 3, 4, 5, 1, 2]
    heap.add(11)
    assert heap.list() == [None, 12, 11, 9, 7, 10, 3, 4, 5, 1, 2, 8]
