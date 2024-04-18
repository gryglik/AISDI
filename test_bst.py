from bst import BST


def test_create_root():
    my_tree = BST([1])
    assert my_tree.root.right is None
    assert my_tree.root.left is None
    assert my_tree.root.key == 1


def test_add_root():
    my_tree = BST()
    my_tree.add_key(67)
    assert my_tree.root.left is None
    assert my_tree.root.right is None
    assert my_tree.root.key == 67


def test_create_simple_tree():
    my_tree = BST([8])
    assert my_tree.root.left is None
    assert my_tree.root.right is None
    assert my_tree.root.key == 8
    my_tree.add_key(1)
    assert my_tree.root.left.key == 1
    assert my_tree.root.left.left is None
    assert my_tree.root.left.right is None
    assert my_tree.root.right is None


def test_create_bigger_tree():
    my_tree = BST([8, 2, 9, 4, 5, 11, 15])

    assert my_tree.root.left.key == 2
    assert my_tree.root.right.key == 9
    assert my_tree.root.key == 8

    assert my_tree.root.left.right.key == 4
    assert my_tree.root.left.right.right.key == 5


def test_create_full_tree():
    my_tree = BST([8, 5, 13, 3, 10, 6, 16])

    assert my_tree.root.left.key == 5
    assert my_tree.root.right.key == 13
    assert my_tree.root.key == 8

    assert my_tree.root.left.right.key == 4
    assert my_tree.root.left.right.right.key == 5


def test_search_full_tree():
    my_tree = BST([8, 5, 13, 3, 10, 6, 16])

    assert my_tree.search(my_tree.root, 8).key == 8
    assert my_tree.search(my_tree.root, 7) is None
    assert my_tree.search(my_tree.root, 5).key == 5
    assert my_tree.search(my_tree.root, 13).key == 13
    assert my_tree.search(my_tree.root, 3).key == 3
    assert my_tree.search(my_tree.root, 10).key == 10
    assert my_tree.search(my_tree.root, 6).key == 6
    assert my_tree.search(my_tree.root, 16).key == 16


def test_remove_element_tree_leaf():
    my_tree = BST([8, 5, 13, 3, 10, 6, 16])

    my_tree.remove(my_tree.root, 16)
    assert my_tree.search(my_tree.root, 8).key == 8
    assert my_tree.search(my_tree.root, 7) is None
    assert my_tree.search(my_tree.root, 5).key == 5
    assert my_tree.search(my_tree.root, 13).key == 13
    assert my_tree.search(my_tree.root, 3).key == 3
    assert my_tree.search(my_tree.root, 10).key == 10
    assert my_tree.search(my_tree.root, 6).key == 6
    assert my_tree.search(my_tree.root, 16) is None


def test_remove_element_tree_one_child():
    my_tree = BST([8, 5, 13, 3, 6, 16])

    assert my_tree.search(my_tree.root, 8).key == 8
    assert my_tree.search(my_tree.root, 8) == my_tree.root
    assert my_tree.search(my_tree.root, 5).key == 5
    assert my_tree.search(my_tree.root, 13).key == 13
    assert my_tree.search(my_tree.root, 3).key == 3

    my_tree.remove(my_tree.root, 13)

    assert my_tree.search(my_tree.root, 8).key == 8
    assert my_tree.search(my_tree.root, 8) == my_tree.root
    assert my_tree.search(my_tree.root, 5).key == 5
    assert my_tree.search(my_tree.root, 13) is None
    assert my_tree.search(my_tree.root, 3).key == 3
