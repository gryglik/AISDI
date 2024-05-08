import argparse
from class_cord import cord
from class_cord import next_nodes
from class_cord import queue_element
from heap import Heap

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', type=str)

args = parser.parse_args()

# Importing board
path = (args.filename)
board = []
start = cord()      # first X
end = cord()        # second X
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
                board_line.append(None)
            elif item != '\n':
                board_line.append(int(item))
        board.append(board_line)
        line = f.readline()

# Defining and initialising size of the board
size = cord(len(board[0]), len(board))

# Defining table of shortest path lenght for each node from start node (X)
# and initialising it with infinite path lenghts (None)
d = [[None] * size.x for i in range(size.y)]
# Initialising shortest path lenght for start node (X)
d[start.y][start.x] = 0

# Defining table of predeccesors for each node
p = [[cord()] * size.x for i in range(size.y)]
# Initialising predeccesor for start node (X)
p[start.y][start.x] = start

# Defining and initialising priority queue with start node
queue = Heap(2, [queue_element(0, start)])

# Dijkstra's algorithm
while (len(queue.list()) != 0):
    # Accessing the nearest node
    root = queue.remove_root()

    # Checking if already found smaller distance
    if root.dist > d[root.cord.y][root.cord.x]:
        continue

    # Accessing node and its children
    node = root.cord
    children = next_nodes(node, size)

    for child in children:
        # Computing new distance:
        # if node is "J" (None) or child is "J" (None) then
        # the new distance to child is same as the distance to node
        if board[node.y][node.x] is None or board[child.y][child.x] is None:
            new_dist_to_child = d[node.y][node.x]
        # else the new distance to child equals distance to node plus
        # weight of current edge
        elif board[child.y][child.x]:
            new_dist_to_child = d[node.y][node.x] + board[child.y][child.x]

        # if current distance to child is infinite or new distance to child
        # is smaller than current one then distance and pressedor tables
        # are updated with new values
        if d[child.y][child.x] is None or new_dist_to_child < d[child.y][child.x]:
            d[child.y][child.x] = new_dist_to_child
            p[child.y][child.x] = node
            queue.add(queue_element(new_dist_to_child, child))

# Printing
to_print = [[None] * size.x for i in range(size.y)]
to_print[end.y][end.x] = "X"
to_print[start.y][start.x] = "X"

node = end
while node != start:
    print(node)
    if board[node.y][node.x]:
        to_print[node.y][node.x] = board[node.y][node.x]
    else:
        to_print[node.y][node.x] = "J"
    node = p[node.y][node.x]

for row in to_print:
    for element in row:
        if element:
            print(element,  end=' ')
        else:
            print(" ",  end=' ')
    print()

print(f'Koszt: {d[end.y][end.x]}')
