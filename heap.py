def heapify(k: int, n: int, T: list[int]) -> None:
    length = len(T) - 1
    left = (n - 1) * k + 2 if (n - 1) * k + 2 <= length else None
    right = n * k + 1 if n * k + 1 <= length else length

    if left:
        i_max = left
        for i in range(left + 1, right + 1):
            if T[i] > T[i_max]:
                i_max = i
        if T[i_max] > T[n]:
            temp = T[n]
            T[n] = T[i_max]
            T[i_max] = temp
            heapify(k, i_max, T)


def make_heap(k: int, T: list[int]) -> None:
    length = len(T) - 1
    for i in range(1 + (length - 2) // k, 0, -1):
        heapify(k, i, T)


def add(k: int, new_item: int, T: list[int]) -> None:
    T.append(new_item)
    length = len(T) - 1
    i_item = length
    i_parent = 1 + (i_item - 2) // k
    while T[i_item] > T[i_parent] and not i_item == 1:
        T[i_item] = T[i_parent]
        T[i_parent] = new_item
        i_item = i_parent
        i_parent = 1 + (i_item - 2) // k
