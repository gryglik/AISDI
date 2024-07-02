import time
import gc
import random
import json
from matplotlib import pyplot as plt
from typing import TypeAlias, Callable, Any

from sort_functions import (
    selection_sort, bubble_sort, quick_sort, insertion_sort, merge_sort)

SORTING_FILE = 'pan-tadeusz-unix.txt'

f_sort: TypeAlias = Callable[[list[Any]], list[Any]]
time_stat: TypeAlias = tuple[int, float]


def measure_sorting_time(sort_func: f_sort) -> list[time_stat]:
    with open(SORTING_FILE, 'r') as fp:
        text = []
        while len(text) < 10000:
            line = fp.readline()
            line = line.lower()
            new_line = ''
            for char in line:
                if 'a' <= char <= 'z' or char == ' ':
                    new_line += char
            new_line = new_line.split(' ')
            text.extend([word for word in new_line if word])

    time_stats = []
    for i in range(1, 11):
        sort_time = 0
        sorting_list = [None] * (i * 1000)
        for _ran1 in range(2):
            for j in range(i * 1000):
                sorting_list[j] = random.choice(text)
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            for _ran2 in range(2):
                sort_func(sorting_list)
            stop = time.process_time()
            if gc_old:
                gc.enable()
            sort_time += (stop - start) / 2
        sort_time = sort_time / 2
        time_stats.append((1000 * i, sort_time))
    return time_stats


def plot(data: list[tuple[int, float]], title: str) -> None:
    plt.clf()
    elements = [item[0] for item in data]
    time = [item[1] for item in data]
    plt.plot(elements, time)
    plt.xlabel('words count')
    plt.ylabel('seconds')
    plt.xlim(1000, 10000)
    plt.ylim(0, 1)
    plt.savefig('plots/' + title + '.png')


print('Started measuring, it may take up to 5 mins ...')
data_bubble_sort = measure_sorting_time(bubble_sort)
data_selection_sort = measure_sorting_time(selection_sort)
data_insertion_sort = measure_sorting_time(insertion_sort)
data_merge_sort = measure_sorting_time(merge_sort)
data_quick_sort = measure_sorting_time(quick_sort)

with open('stats.json', 'w') as fp:
    json.dump(('bubble_sort', data_bubble_sort), fp, indent=4)
    json.dump(('selection_sort', data_selection_sort), fp, indent=4)
    json.dump(('insertion_sort', data_insertion_sort), fp, indent=4)
    json.dump(('merge_sort', data_merge_sort), fp, indent=4)
    json.dump(('quick_sort', data_quick_sort), fp, indent=4)

plot(data_bubble_sort, 'bubble_sort')
plot(data_selection_sort, 'selection_sort')
plot(data_insertion_sort, 'insertion_sort')
plot(data_merge_sort, 'merge_sort')
plot(data_quick_sort, 'quick_sort')

plt.clf()
plt.title('compared_sort')
plt.xlabel('words count')
plt.ylabel('seconds')
plt.xlim(1000, 10000)
plt.ylim(0, 1)
plt.plot([element for element, time in data_bubble_sort],
         [time for element, time in data_bubble_sort])
plt.plot([element for element, time in data_selection_sort],
         [time for element, time in data_selection_sort])
plt.plot([element for element, time in data_insertion_sort],
         [time for element, time in data_insertion_sort])
plt.plot([element for element, time in data_merge_sort],
         [time for element, time in data_merge_sort])
plt.plot([element for element, time in data_quick_sort],
         [time for element, time in data_quick_sort])
plt.legend([
    'bubble sort', 'selection sort', 'insertion sort',
    'merge sort', 'quick sort'])
plt.savefig('plots/compared_sort.png')
plt.show()
