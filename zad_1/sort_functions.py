from typing import Any


def bubble_sort(given_list: list[Any]) -> list[Any]:
    s_list = given_list[:]
    n = len(s_list)
    for i in range(0, n - 1):
        sorted = True
        for j in range(0, n-i-1):
            if s_list[j] > s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
                sorted = False
        if sorted is True:
            break
    return s_list


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


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    sorted = [None] * (len(left) + len(right))
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted[i + j] = left[i]
            i += 1
        else:
            sorted[i + j] = right[j]
            j += 1

    if i >= len(left):
        while j < len(right):
            sorted[i + j] = right[j]
            j += 1
    else:
        while i < len(left):
            sorted[i + j] = left[i]
            i += 1
    return sorted


def merge_sort(given_list: list[Any]) -> list[Any]:
    s_list = given_list[:]
    n = len(s_list)
    pivot = n // 2
    if pivot > 0:
        left = merge_sort(s_list[:pivot])
        right = merge_sort(s_list[pivot:])
        return merge(left, right)
    return s_list


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
