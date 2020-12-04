from shared import read_puzzle_input
import re
import functools
import string


req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

puzzle_input = read_puzzle_input(4, False)


def advent4_1():
    return len(filter_required())


def advent4_2():
    return len([z for z in [
        [x for x in y if
                (x[0] == "byr" and (len(x[1]) == 4 and 1920 <= int(x[1]) <= 2002)) or
                (x[0] == "iyr" and (len(x[1]) == 4 and 2010 <= int(x[1]) <= 2020)) or
                (x[0] == "eyr" and (len(x[1]) == 4 and 2020 <= int(x[1]) <= 2030)) or
                (x[0] == "hgt" and ("cm" in x[1] and 150 <= int(x[1].split("cm")[0]) <= 193)) or
                (x[0] == "hgt" and ("in" in x[1] and 59 <= int(x[1].split("in")[0]) <= 76)) or
                (x[0] == "hcl" and (x[1][0] == "#" and len(x[1].split("#")[1]) == 6 and all(c in string.hexdigits for c in x[1].split("#")[1]))) or
                (x[0] == "ecl" and (x[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])) or
                (x[0] == "pid" and (len(x[1]) == 9 and x[1].isnumeric()))
                ] for y in filter_required()]
                if set(req_fields).issubset([i[0] for i in z])
                ])


def filter_required():
    return [x for x in [
        [i.split(":") for i in re.split(" |\\n", j)] for j in puzzle_input.split("\n\n")]
        if set(req_fields).issubset([y[0] for y in x])]


print("\n\n*Advent 4:*")
print("\nPart 1:")
print(advent4_1())
print("\nPart 2:")
print(advent4_2())
