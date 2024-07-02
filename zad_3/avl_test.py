from avl import AVLNode


def test_AVLNode_create():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([3, 6, 13, 20, 1, 23, 7, 8, 9, 10, 22, 21])
    assert avl_root.search(22).h == 3


def test_right_right_rotation():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([1, 2, 3])
    assert avl_root.search(1).h == 1
    assert avl_root.search(2).h == 2
    assert avl_root.search(3).h == 1


def test_left_left_rotation():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([3, 2, 1])
    assert avl_root.search(1).h == 1
    assert avl_root.search(2).h == 2
    assert avl_root.search(3).h == 1


def test_right_left_rotation():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([3, 6, 5])
    assert avl_root.search(3).h == 1
    assert avl_root.search(5).h == 2
    assert avl_root.search(6).h == 1


def test_left_right_rotation():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([3, 5, 4])
    assert avl_root.search(3).h == 1
    assert avl_root.search(5).h == 1
    assert avl_root.search(4).h == 2


def test_add_bigger():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([1, 2, 3])
    assert avl_root.search(1).h == 1
    assert avl_root.search(2).h == 2
    assert avl_root.search(3).h == 1
    avl_root.add(4)
    assert avl_root.search(1).h == 1
    assert avl_root.search(2).h == 3
    assert avl_root.search(3).h == 2
    assert avl_root.search(4).h == 1
    avl_root.add(5)
    assert avl_root.search(1).h == 1
    assert avl_root.search(2).h == 3
    assert avl_root.search(3).h == 1
    assert avl_root.search(4).h == 2
    assert avl_root.search(5).h == 1


def test_add_smaller():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([7, 6, 5])
    assert avl_root.search(7).h == 1
    assert avl_root.search(6).h == 2
    assert avl_root.search(5).h == 1
    avl_root.add(4)
    assert avl_root.search(7).h == 1
    assert avl_root.search(6).h == 3
    assert avl_root.search(5).h == 2
    assert avl_root.search(4).h == 1
    avl_root.add(3)
    assert avl_root.search(7).h == 1
    assert avl_root.search(6).h == 3
    assert avl_root.search(5).h == 1
    assert avl_root.search(4).h == 2
    assert avl_root.search(3).h == 1