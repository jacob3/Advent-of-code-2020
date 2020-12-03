import os


def read_puzzle_input(advent):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    raw = open(f"{dir_path}/inputs/input_{advent}.txt")
    puzzle_input = raw.read().splitlines()
    raw.close()

    return puzzle_input
