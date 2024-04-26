from heap import Heap
from class_cord import queue_element
from class_cord import cord


def test_create_2_a_typical():
    heap = Heap(2, [12, 10, 9, 7, 8, 3, 4, 5, 1, 2])
    assert heap.list() == [1, 2, 3, 5, 8, 9, 4, 10, 7, 12]


def test_create_heap_q_element():
    q1 = queue_element(None, cord(1, 2))
    q2 = queue_element(1, cord(2, 2))
    q3 = queue_element(2, cord(3, 3))
    heap = Heap(2, [q1, q2, q3])
    assert heap.remove_root() == q2

