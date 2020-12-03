from shared import read_puzzle_input

import math


def advent3_1(puzzle_input):
    return advent3_calc(puzzle_input, 3, 1)


def advent3_2(puzzle_input):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    return math.prod([advent3_calc(puzzle_input, x, y) for x, y in slopes])


def advent3_calc(puzzle_input, right, down):
    return len(list(filter(lambda x: x[0] == "#", [l[(right*y) % len(l):] + l[:(right*y) % len(l)] for y, l in enumerate([puzzle_input[i] for i in range(0, len(puzzle_input), down)])])))


puzzle_input = read_puzzle_input(3)

print("\nPart 1")
print(advent3_1(puzzle_input))
print("\nPart 2:")
print(advent3_2(puzzle_input))
