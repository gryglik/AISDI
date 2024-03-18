import time
import gc
import random
from matplotlib import pyplot as plt
from typing import Callable, Any

from sort_functions import selection_sort


def measure_sorting_time(
        sort_func: Callable[[list[Any]], list[Any]]) -> list[tuple[int, float]]:
    with open('pan-tadeusz-unix.txt', 'r') as fp:
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

        # 3 - krotne losowanie tablicy do sortowania
        for a in range(3):
            # losowanie wyrazów
            for j in range(i * 1000):
                sorting_list[j] = random.choice(text)
            # 5 - krotne mierzenie czasu sortowania
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            for _ in range(5):
                sort_func(sorting_list)
            stop = time.process_time()
            if gc_old:
                gc.enable()
            # obliczanie średniej
            sort_time += (stop - start) / 5

        # obliczanie końcowego czasu
        sort_time = sort_time / 3
        time_stats.append((1000 * i, sort_time))

    return time_stats


def plot(data: list[tuple[int, float]]):
    elements = [item[0] for item in data]
    time = [item[1] for item in data]
    plt.plot(elements, time)
    plt.show()


print('Measuring selection sort performance')
data_selection_sort = measure_sorting_time(selection_sort)
print('Showing plot')
plot(data_selection_sort)
