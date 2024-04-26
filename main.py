import argparse
from class_cord import cord
from class_cord import next_nodes
from class_cord import queue_element
from heap import Heap

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('filename', type=str)

# args = parser.parse_args()

path = ("graf1.txt")
board = []
start = cord()
end = cord()
with open(path) as f:
    line = f.readline()
    while line:
        board_line = []
        for item in line:
            if item == "X" and start.x is None:
                start = cord(len(board_line), len(board))
                board_line.append(0)
            elif item == "X" and start.x is not None:
                end = cord(len(board_line), len(board))
                board_line.append(0)
            elif item == "J":
                board_line.append(0)
            elif item != '\n':
                board_line.append(int(item))
        board.append(board_line)
        line = f.readline()

for row in board:
    print(row)
print()
print(f'root {start} \n')

size = cord(len(board[0]), len(board))

d = [[None] * size.x for i in range(size.y)]
d[start.y][start.x] = 0
q1 = queue_element(0, start)
queue = Heap(2, [q1])

print("d: ")
for row in d:
    print(row)
print()

p = [[cord()] * size.x for i in range(size.y)]
p[start.y][start.x] = start
for row in p:
    print(row)
print(p)

while (len(queue.list()) != 0):
    root = queue.remove_root()
    if root.dist > d[root.cord.y][root.cord.x]:
        continue
    node = root.cord
    childs = next_nodes(node, size)
    print(node)
    for child in childs:
        new_dist = d[node.y][node.x] + board[child.y][child.x]
        if d[child.y][child.x] is None:
            d[child.y][child.x] = new_dist
            queue.add(queue_element(new_dist, child))
        elif new_dist < d[child.y][child.x]:
            d[child.y][child.x] = new_dist
            queue.add(queue_element(new_dist, child))

for row in d:
    print(row)
print(d)
