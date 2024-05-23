import argparse
import json
from ast import parse

parser = argparse.ArgumentParser()
parser.add_argument('tape', type=str)
parser.add_argument('program_path', type=str)

args = parser.parse_args()

tape = list(args.tape)
program = {}
with open(args.program_path) as fp:
    for line in fp:
        line_list = line.strip().split(' ')
        if line_list[0] not in program:
            program[line_list[0]] = dict()
        program[line_list[0]][line_list[1]] = line_list[2:]

current_state = "init"
current_symbol = 0

while current_state != "halt":
    new_symbol, direction, new_state = program[current_state][tape[current_symbol]]
    tape[current_symbol] = new_symbol
    if direction == "R":
        if current_symbol == len(tape) - 1:
            tape.append("_")
        current_symbol += 1
    elif direction == "L":
        if current_symbol == 0:
            tape.insert(0, "_")
        else:
            current_symbol -= 1
    current_state = new_state
    print(''.join(tape) + " " + current_state)
    print(' ' * current_symbol + '^')
