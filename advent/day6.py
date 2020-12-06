from shared import read_puzzle_input
import functools
import math


puzzle_input = read_puzzle_input(6, False)


def advent6_1():
    return sum([len(set(x.replace("\n", ""))) for x in puzzle_input.split("\n\n")])


def advent6_2():
    return sum([len(functools.reduce(lambda x, y: list(set(x) & set(y)), x)) for x in [x.splitlines() for x in puzzle_input.split("\n\n")]])


print("\n\n*Advent 6:*")
print("\nPart 1:")
print(advent6_1())
print("\nPart 2:")
print(advent6_2())
