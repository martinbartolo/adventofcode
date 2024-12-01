import sys

sys.setrecursionlimit(100000)

file = open("day-23.txt", "r")
text = file.read()
lines = text.splitlines()


def find_start_position(lines):
    for i, char in enumerate(lines[0]):
        if char == ".":
            return 0, i
    return -1, -1


def find_end_position(lines):
    for i, char in enumerate(lines[-1]):
        if char == ".":
            return len(lines) - 1, i
    return -1, -1


#################### Part 1 ####################


def find_longest(pos_y, pos_x, end_y, end_x, current, lines, visited):
    if pos_y < 0 or pos_x < 0 or pos_y >= len(lines) or pos_x >= len(lines[0]):
        return -1

    if visited[pos_y][pos_x]:
        return -1

    if lines[pos_y][pos_x] == "#":
        return -1

    if (pos_y, pos_x) == (end_y, end_x):
        return current

    visited[pos_y][pos_x] = True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    arrows = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    if lines[pos_y][pos_x] in arrows:
        directions = [arrows[lines[pos_y][pos_x]]]

    maximum = max(
        [
            find_longest(pos_y + dy, pos_x + dx, end_y, end_x, current + 1, lines, visited)
            for dy, dx in directions
        ]
    )
    visited[pos_y][pos_x] = False

    return maximum


def part1(lines):
    start_y, start_x = find_start_position(lines)
    end_y, end_x = find_end_position(lines)
    visited = [[False] * len(lines[0]) for _ in range(len(lines))]
    return find_longest(start_y, start_x, end_y, end_x, 0, lines, visited)


print("Solution 1: ", part1(lines))

#################### Part 2 ####################
max_length = 0


def find_longest_2(pos_y, pos_x, end_y, end_x, current, lines, visited):
    global max_length
    if pos_y < 0 or pos_x < 0 or pos_y >= len(lines) or pos_x >= len(lines[0]):
        return -1

    if visited[pos_y][pos_x]:
        return -1

    if lines[pos_y][pos_x] == "#":
        return -1

    if (pos_y, pos_x) == (end_y, end_x):
        return current

    visited[pos_y][pos_x] = True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    maximum = max(
        [
            find_longest_2(pos_y + dy, pos_x + dx, end_y, end_x, current + 1, lines, visited)
            for dy, dx in directions
        ]
    )
    visited[pos_y][pos_x] = False
    if maximum > max_length:
        max_length = maximum
        print(maximum)
    return maximum


def part2(lines):
    start_y, start_x = find_start_position(lines)
    end_y, end_x = find_end_position(lines)
    visited = [[False] * len(lines[0]) for _ in range(len(lines))]
    return find_longest_2(start_y, start_x, end_y, end_x, 0, lines, visited)


print("Solution 2: ", part2(lines))
