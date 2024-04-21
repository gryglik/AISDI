from avl import AVLNode


def test_AVLNode_create():
    avl_root = AVLNode()
    avl_root = avl_root.add_list([3, 6, 13, 20, 1, 23, 7, 8, 9, 10, 22, 21])
    assert avl_root.search(22).h == 3
