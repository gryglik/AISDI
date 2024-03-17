def selection_sort(s_list: list):
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
