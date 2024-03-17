from typing import Callable, Any
import time
from matplotlib import pyplot as plt


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
            splitted = new_line.split(' ')
            text.extend([word for word in splitted if word])
    time_stats = []
    for i in range(1, 11):
        start = time.process_time()
        sort_func(text[:1000 * i])
        stop = time.process_time()
        time_stats.append((1000 * i, stop - start))
    return time_stats
