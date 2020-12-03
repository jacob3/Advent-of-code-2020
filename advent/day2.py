from shared import read_puzzle_input


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
            correct_policies += 1

    return f"{correct_policies} / {len(puzzle_input)}"


def advent2_2(puzzle_input):
    puzzle_input = read_puzzle_input(2)
    correct_policies = 0

    for x in puzzle_input:
        policy = {
            # index starts at 1
            "pos1": int(x.split(" ")[0].split("-")[0]) - 1,
            # index starts at 1
            "pos2": int(x.split(" ")[0].split("-")[1]) - 1,
            "letter": x.split(" ")[1].strip(":"),
            "password": x.split(" ")[2]
        }

        try:
            if (policy["password"][policy["pos1"]] == policy["letter"]) ^ (policy["password"][policy["pos2"]] == policy["letter"]):
                correct_policies += 1
        except:
            pass

    return f"{correct_policies} / {len(puzzle_input)}"


# today I'm lazy and don't want to achieve it with a onliner
puzzle_input = read_puzzle_input(2)

print("\n\n*Advent 2:*")
print("\nPart 1:")
print(advent2_1(puzzle_input))
print("\nPart 2:")
print(advent2_2(puzzle_input))
