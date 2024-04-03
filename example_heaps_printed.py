from heap import Heap
import random

input_list2 = [
    random.randint(1, 300) for i in range(0, 100)]

heap2 = Heap(2, input_list2)
heap2.print()

print('\n' * 5)

input_list5 = [
    random.randint(1, 300) for i in range(0, 30)]

heap5 = Heap(5, input_list5)
heap5.print()

print('\n' * 5)

input_list7 = [
    random.randint(1, 300) for i in range(0, 50)]

heap7 = Heap(7, input_list7)
heap7.print()

print('\n' * 5)
