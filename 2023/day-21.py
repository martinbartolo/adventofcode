from functools import cache
from math import ceil

file = open("day-21.txt", "r")
text = file.read()
lines = text.splitlines()

############### Part 1 ###############


@cache
def next_move(pos_y, pos_x, steps):
    if steps == 0:
        return {(pos_y, pos_x)}

    reachable = set()

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_y, new_x = pos_y + dy, pos_x + dx
        if lines[new_y][new_x] != "#":
            reachable.update(next_move(new_y, new_x, steps - 1))

    return reachable


def find_start_position():
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                return i, j
    return -1, -1


def num_plots(steps, next_move):
    start_y, start_x = find_start_position()
    return len(next_move(start_y, start_x, steps))


print("Solution 1: ", num_plots(6, next_move))


############### Part 1 ###############


@cache
def next_move_2(pos_y, pos_x, steps):
    height = len(lines)
    width = len(lines[0])

    if steps == 0:
        return {(pos_y, pos_x)}

    reachable = set()

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_y, new_x = pos_y + dy, pos_x + dx
        if lines[new_y % height][new_x % width] != "#":
            reachable.update(next_move_2(new_y, new_x, steps - 1))

    return reachable


def part_two():
    height = len(lines)
    mod = 26501365 % height

    seen = []

    for run in [mod, mod + height, mod + height * 2]:
        reachable_positions = num_plots(run, next_move_2)
        seen.append(reachable_positions)
        print(seen)

    m = seen[1] - seen[0]
    n = seen[2] - seen[1]
    a = (n - m) // 2
    b = m - 3 * a
    c = seen[0] - b - a
    ceiling = ceil(26501365 / height)
    answer = a * ceiling**2 + b * ceiling + c
    return answer


print("Solution 2: ", part_two())
