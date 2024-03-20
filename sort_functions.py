from typing import Any


def selection_sort(s_list: list[Any]) -> list[Any]:
    sorted_list = s_list[:]
    n = len(sorted_list)
    for i in range(0, n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[idx_min]:
                idx_min = j
        val_temp = sorted_list[i]
        sorted_list[i] = sorted_list[idx_min]
        sorted_list[idx_min] = val_temp
    return sorted_list


def insertion_sort(given_list: list[Any]) -> list[Any]:
    s_list = given_list[:]
    n = len(s_list)
    for i in range(1, n):
        element = s_list[i]
        j = i - 1

        while j >= 0 and s_list[j] > element:
            s_list[j+1] = s_list[j]
            j -= 1

        s_list[j+1] = element

    return s_list
