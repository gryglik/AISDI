import time
import gc
import random
from matplotlib import pyplot as plt
from typing import TypeAlias

from heap import Heap

time_stat: TypeAlias = tuple[int, float]


def measure_making_heap_time(a: int, input_list: list[int]) -> list[time_stat]:
    time_stats = []
    for i in range(1, 11):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(a, input_list[:i * 10000])
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 10000, stop - start))
    return time_stats


def measure_removing_roots_from_heap_time(a: int, input_list: list[int]) -> list[time_stat]:
    time_stats = []
    for i in range(1, 11):
        heap = Heap(a, input_list)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for _ in range(i*10000):
            heap.remove_root()
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 10000, stop - start))
    return time_stats


input_list = [
    random.randint(1, 300000) for i in range(0, 100000)]

time.sleep(5)  # czas na załadowanie bibliotek
data_2_a = measure_making_heap_time(2, input_list)
data_5_a = measure_making_heap_time(5, input_list)
data_7_a = measure_making_heap_time(7, input_list)

plt.clf()
plt.title('compared heap creation')
plt.xlabel('elements count')
plt.ylabel('seconds')
plt.plot([element for element, time in data_2_a],
         [time for element, time in data_2_a])
plt.plot([element for element, time in data_5_a],
         [time for element, time in data_5_a])
plt.plot([element for element, time in data_7_a],
         [time for element, time in data_7_a])
plt.legend(['2-ary heap', '5-ary heap', '7-ary heap'])
plt.savefig('plots/compared_heap_creation.png')
# plt.show()

# Creating plots for removing
data_2_r = measure_removing_roots_from_heap_time(2, input_list)
data_5_r = measure_removing_roots_from_heap_time(5, input_list)
data_7_r = measure_removing_roots_from_heap_time(7, input_list)

plt.clf()
plt.title('"Deletion time comparison"')
plt.xlabel('elements count')
plt.ylabel('seconds')
plt.plot([element for element, time in data_2_r],
         [time for element, time in data_2_r])
plt.plot([element for element, time in data_5_r],
         [time for element, time in data_5_r])
plt.plot([element for element, time in data_7_r],
         [time for element, time in data_7_r])
plt.legend(['2-ary heap', '5-ary heap', '7-ary heap'])
plt.savefig('plots/compared_heap_deletion.png')
plt.show()
