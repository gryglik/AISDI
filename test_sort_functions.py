from sort_functions import selection_sort


def test_selection_sort_typical():
    list_1 = [2, 1, 3, 1, 4, 7, 3]
    sorted = selection_sort(list_1)
    assert sorted == [1, 1, 2, 3, 3, 4, 7]
    assert list_1 == [2, 1, 3, 1, 4, 7, 3]


def test_selection_sort_sorted():
    list_1 = [1, 2, 3, 4, 4]
    sorted = selection_sort(list_1)
    assert sorted == [1, 2, 3, 4, 4]


def test_selection_sort_chars():
    list_1 = ['z', 'a', 'x', 'm', 'y']
    sorted = selection_sort(list_1)
    assert sorted == ['a', 'm', 'x', 'y', 'z']


def test_selection_sort_strings():
    list_1 = ['zyx', 'xyz', 'abbc', 'xzy', 'abc', 'aabc']
    sorted = selection_sort(list_1)
    assert sorted == ['aabc', 'abbc', 'abc', 'xyz', 'xzy', 'zyx']