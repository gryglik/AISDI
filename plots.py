from bst import BST
from avl import AVLNode
import time
import gc
import random
from matplotlib import pyplot as plt


def measure_make_bst(input_list: list[int]):
    time_stats = []
    for i in range(1, 11):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        BST(input_list[:i * 1000])
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 1000, stop - start))
    return time_stats


def measure_make_avl(input_list: list[int]):
    time_stats = []
    for i in range(1, 11):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        root = AVLNode()
        root = root.add_list(input_list[:i * 1000])
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 1000, stop - start))
    return time_stats


def measure_search_bst(input_list: list[int]):
    time_stats = []
    bst = BST(input_list)
    for i in range(1, 11):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for key in input_list[:i * 1000]:
            bst.search(bst.root, key)
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 1000, stop - start))
    return time_stats


def measure_search_avl(input_list: list[int]):
    time_stats = []
    root = AVLNode()
    root.add_list(input_list)
    for i in range(1, 11):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for key in input_list[:i * 1000]:
            root.search(key)
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 1000, stop - start))
    return time_stats


def measure_remove_bst(input_list: list[int]):
    time_stats = []
    for i in range(1, 11):
        bst = BST(input_list)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for key in input_list[:i * 1000]:
            bst.remove(bst.root, key)
        stop = time.process_time()
        if gc_old:
            gc.enable()
        time_stats.append((i * 1000, stop - start))
    return time_stats


input_list = [
    random.randint(1, 30000) for i in range(0, 10000)]
# input_list = []
# input_set = set()
# while len(input_list) < 10000:
#     new_key = random.randint(1, 30000)

#     if new_key not in input_set:
#         input_set.add(new_key)
#         input_list.append(new_key)

time.sleep(10)  # czas na załadowanie bibliotek
data_make_bst = measure_make_bst(input_list)
data_make_avl = measure_make_avl(input_list)

data_search_bst = measure_search_bst(input_list)
data_search_avl = measure_search_avl(input_list)

data_remove_bst = measure_remove_bst(input_list)

plt.clf()
plt.title('compared tree creation, search and remove')
plt.xlabel('elements count')
plt.ylabel('seconds')
plt.plot([element for element, time in data_make_bst],
         [time for element, time in data_make_bst])
plt.plot([element for element, time in data_make_avl],
         [time for element, time in data_make_avl])
plt.plot([element for element, time in data_search_bst],
         [time for element, time in data_search_bst])
plt.plot([element for element, time in data_search_avl],
         [time for element, time in data_search_avl])
plt.plot([element for element, time in data_remove_bst],
         [time for element, time in data_remove_bst])
plt.legend(['Make bst', 'Make avl', 'Search bst', 'Search avl',
            'Remove from bst'])
plt.savefig('compared_tree.png')
plt.show()
