from shared import read_puzzle_input
import math


puzzle_input = read_puzzle_input(5)


def advent5_1():
    return max(get_ids())


def advent5_2():
    ids = get_ids()
    return sorted(set(range(ids[0], ids[1] + 1)).difference(ids))[0]


def get_ids():
    ids = []
    for x in puzzle_input:
        rows = [0, 127]
        seats = [0, 7]

        for idx, val in enumerate(x):
            if idx <= 6:
                if val == "F":
                    rows = [rows[0], math.floor(
                        rows[1] - (rows[1] - rows[0]) / 2)]
                else:
                    rows = [rows[1] - int((rows[1] - rows[0]) / 2), rows[1]]
            else:
                if val == "L":
                    seats = [seats[0], math.floor(
                        seats[1] - (seats[1] - seats[0]) / 2)]
                else:
                    seats = [seats[1] -
                             int((seats[1] - seats[0]) / 2), seats[1]]

        ids.append(rows[0] * 8 + seats[0])

    return ids


print("\n\n*Advent 5:*")
print("\nPart 1:")
print(advent5_1())
print("\nPart 2:")
print(advent5_2())
