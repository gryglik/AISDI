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


def partition(s_list: list[Any], start: int, end:  int) -> int:
    pivot = s_list[end]
    i = start - 1
    for j in range(start, end):
        if s_list[j] < pivot:
            i += 1
            s_list[i], s_list[j] = s_list[j], s_list[i]
    s_list[i+1], s_list[end] = s_list[end], s_list[i+1]
    return i+1


def quick_sort_rec(s_list: list[Any], start: int, end:  int):
    if start < end:
        pivot_index = partition(s_list, start, end)
        quick_sort_rec(s_list, start, pivot_index - 1)
        quick_sort_rec(s_list, pivot_index + 1, end)


def quick_sort(given_list: list[Any]) -> list[Any]:
    s_list = given_list[:]
    quick_sort_rec(s_list, 0, len(s_list)-1)
    return s_list
