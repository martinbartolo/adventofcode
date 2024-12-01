# CHEATED
# Solution Followed from reddit comment
# https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd0oj1t/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

from functools import cache

file = open("day-12.txt", "r")
text = file.read()


#################### Part 1 ####################


@cache  # cache functions since we are using recursion - makes it run way faster
def num_legal(condition, groups):
    condition = condition.lstrip(".")

    # ['', ()] is legal
    if condition == "":
        return int(groups == ())

    # [condition, []] is legal as long as condition has no "#" left
    if groups == ():
        return int(condition.find("#") == -1)

    if condition[0] == "#":
        if len(condition) < groups[0] or "." in condition[: groups[0]]:
            return 0  # not enough space for the spring
        elif len(condition) == groups[0]:
            return int(len(groups) == 1)  # single spring space left, return 1 if right size
        elif condition[groups[0]] == "#":
            return 0  # space too big for spring
        else:
            # remove leading spring and following character
            return num_legal(condition[groups[0] + 1 :], groups[1:])

    return num_legal("#" + condition[1:], groups) + num_legal(condition[1:], groups)


def num_arrangements(text: str):
    lines = text.splitlines()
    conditions = [line.split() for line in lines]
    cc = [[c[0], tuple(int(num) for num in c[1].split(","))] for c in conditions]
    return sum(num_legal(condition, groups) for [condition, groups] in cc)


print("Solution 1: ", num_arrangements(text))

#################### Part 2 ####################


def num_arrangements_2(text: str):
    lines = text.splitlines()
    conditions = [line.split() for line in lines]
    cc = [[c[0], tuple(int(num) for num in c[1].split(","))] for c in conditions]
    cc2 = [[(c[0] + "?") * 4 + c[0], c[1] * 5] for c in cc]
    return sum(num_legal(condition, groups) for [condition, groups] in cc2)


print("Solution 2: ", num_arrangements_2(text))
