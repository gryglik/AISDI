import argparse
from class_cord import cord

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', type=str)

args = parser.parse_args()

board = []
root = cord()
with open(args.filename) as f:
    line = f.readline()
    while line:
        board_line = []
        for item in line:
            if item == "X" and root.x is None:
                root = cord(len(board_line), len(board))
            if item != '\n':
                board_line.append(item)
        board.append(board_line)
        line = f.readline()

for row in board:
    print(row)
print()
print(f'root {root} \n')

size = cord(len(board[0]), len(board))

d = [[None] * size.x for i in range(size.y)]
d[root.y][root.x] = 0
print("d: ")
for row in d:
    print(row)
print()

p = [[cord()] * size.x for i in range(size.y)]
p[root.y][root.x] = root
for row in p:
    print(row)
print(p)

