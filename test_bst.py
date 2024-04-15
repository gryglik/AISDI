from bst import BST


def test_create_root():
    my_tree = BST([1])
    assert my_tree.nodes[0].parent == 0
    assert my_tree.nodes[0].left is None
    assert my_tree.nodes[0].right is None


def test_add_root():
    my_tree = BST()
    my_tree.add(67)
    assert my_tree.nodes[0].parent == 0
    assert my_tree.nodes[0].left is None
    assert my_tree.nodes[0].right is None
    assert my_tree.nodes[0].key == 67


def test_create_simple_tree():
    my_tree = BST([8])
    assert my_tree.nodes[0].parent == 0
    assert my_tree.nodes[0].left is None
    assert my_tree.nodes[0].right is None
    assert my_tree.nodes[0].key == 8
    my_tree.add(1)
    assert my_tree.nodes[0].parent == 0
    assert my_tree.nodes[0].left == 1
    assert my_tree.nodes[0].right is None
    assert my_tree.nodes[1].parent == 0
    assert my_tree.nodes[1].left is None
    assert my_tree.nodes[1].right is None
    assert my_tree.nodes[1].key == 1


def test_create_bigger_tree():
    my_tree = BST([8, 2, 9, 4, 5, 11, 15])

    assert my_tree.nodes[5].parent == 2
    assert my_tree.nodes[5].left is None
    assert my_tree.nodes[5].right == 6
    assert my_tree.nodes[5].key == 11

    assert my_tree.nodes[6].parent == 5
    assert my_tree.nodes[6].left is None
    assert my_tree.nodes[6].right is None
    assert my_tree.nodes[6].key == 15


def test_create_full_tree():
    my_tree = BST([8, 5, 13, 3, 10, 6, 16])

    assert my_tree.nodes[1].parent == 0
    assert my_tree.nodes[1].left == 3
    assert my_tree.nodes[1].right == 5
    assert my_tree.nodes[1].key == 5

    assert my_tree.nodes[2].parent == 0
    assert my_tree.nodes[2].left == 4
    assert my_tree.nodes[2].right == 6
    assert my_tree.nodes[2].key == 13


def test_search_full_tree():
    my_tree = BST([8, 5, 13, 3, 10, 6, 16])

    assert my_tree.search(8) == 0
    assert my_tree.search(7) is None
    assert my_tree.search(5) == 1
    assert my_tree.search(13) == 2
    assert my_tree.search(3) == 3
    assert my_tree.search(10) == 4
    assert my_tree.search(6) == 5
    assert my_tree.search(16) == 6
