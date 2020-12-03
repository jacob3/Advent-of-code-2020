import math
import functools

def read_puzzle_input(advent):
    raw = open(f"input_{advent}.txt")
    puzzle_input = raw.read().splitlines()
    raw.close()

    return puzzle_input


def advent1():
    puzzle_input = list(map(int, read_puzzle_input(1)))

    print("Part 1:")
    print(advent1_1(puzzle_input))
    print("\nPart 2:")
    print(advent1_2(puzzle_input))


def advent1_1(puzzle_input):
    return [x*y for x in puzzle_input for y in puzzle_input if x + y == 2020][0]

def advent1_2(puzzle_input):
    return [x*y*z for x in puzzle_input for y in puzzle_input for z in puzzle_input if x + y + z== 2020][0]

def advent2():
    #today I'm lazy and don't want to achieve it with a onliner
    puzzle_input = read_puzzle_input(2)

    print("\nPart 1")
    print(advent2_1(puzzle_input))
    print("\nPart 2:")
    print(advent2_2(puzzle_input))


def advent2_1(puzzle_input):
    puzzle_input = read_puzzle_input(2)
    correct_policies = 0

    for x in puzzle_input:
        policy = {
            "min": int(x.split(" ")[0].split("-")[0]),
            "max": int(x.split(" ")[0].split("-")[1]),
            "letter": x.split(" ")[1].strip(":"),
            "password": x.split(" ")[2]
        }

        count = policy["password"].count(policy["letter"])
        if policy["min"] <= count <= policy["max"]:
            correct_policies+=1

    return f"{correct_policies} / {len(puzzle_input)}"


def advent2_2(puzzle_input):
    puzzle_input = read_puzzle_input(2)
    correct_policies = 0

    for x in puzzle_input:
        policy = {
            "pos1": int(x.split(" ")[0].split("-")[0]) - 1, # index starts at 1
            "pos2": int(x.split(" ")[0].split("-")[1]) - 1, # index starts at 1
            "letter": x.split(" ")[1].strip(":"),
            "password": x.split(" ")[2]
        }

        try:
            if (policy["password"][policy["pos1"]] == policy["letter"]) ^ (policy["password"][policy["pos2"]] == policy["letter"]):
                correct_policies+=1
        except:
            pass

    return f"{correct_policies} / {len(puzzle_input)}"


def advent3():
    puzzle_input = read_puzzle_input(3)

    print("\nPart 1")
    print(advent3_1(puzzle_input))
    print("\nPart 2:")
    print(advent3_2(puzzle_input))


def advent3_1(puzzle_input):
    return advent3_calc(puzzle_input, 3, 1)


def advent3_2(puzzle_input):
    slopes = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    return math.prod([advent3_calc(puzzle_input, x, y) for x,y in slopes])

def advent3_calc(puzzle_input, right, down):
    return len(list(filter(lambda x: x[0] == "#", [l[(right*y)%len(l):] + l[:(right*y)%len(l)] for y,l in enumerate([puzzle_input[i] for i in range(0,len(puzzle_input), down)])])))

print("*Advent 1:*")
advent1()

print("\nAdvent 2:")
advent2()

print("\nAdvent 3:")
advent3()
