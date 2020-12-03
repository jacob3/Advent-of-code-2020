from shared import read_puzzle_input


def advent1_1(puzzle_input):
    return [x*y for x in puzzle_input for y in puzzle_input if x + y == 2020][0]


def advent1_2(puzzle_input):
    return [x*y*z for x in puzzle_input for y in puzzle_input for z in puzzle_input if x + y + z == 2020][0]


puzzle_input = list(map(int, read_puzzle_input(1)))

print("\n\n*Advent 1:*")
print("\nPart 1:")
print(advent1_1(puzzle_input))
print("\nPart 2:")
print(advent1_2(puzzle_input))
