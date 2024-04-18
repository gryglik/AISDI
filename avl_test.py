from avl import AVL


def test_AVL_create():
    avl_tree = AVL([3, 6, 13, 20, 1, 23, 7, 8, 9, 10, 22, 21])
    assert avl_tree.search(22).h == 3