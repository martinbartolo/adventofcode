file = open('input.txt', 'r')
text = file.read().strip()


def get_score(lines, i, j, peaks, curr_height):
    if curr_height == 9:
        peaks.add((i, j))
        return

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < len(lines) and 0 <= new_j < len(lines[0]):
            new_height = lines[new_i][new_j]
            if new_height == curr_height + 1:
                get_score(lines, new_i, new_j, peaks, new_height)


def part1(lines):
    total = 0
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == 0:
                peaks = set()
                get_score(lines, i, j, peaks, 0)
                total += len(peaks)
    return total


def count_paths(lines, i, j, visited, curr_height):
    if curr_height == 9:
        return 1

    visited.add((i, j))
    paths = 0

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < len(lines) and 0 <= new_j < len(lines[0]):
            new_height = lines[new_i][new_j]
            if new_height == curr_height + 1 and (new_i, new_j) not in visited:
                paths += count_paths(lines, new_i, new_j, visited.copy(), new_height)

    return paths


def part2(lines):
    total = 0
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == 0:
                paths = count_paths(lines, i, j, set(), 0)
                total += paths
    return total


lines = [[int(x) for x in line] for line in text.splitlines()]
print('Solution 1:', part1(lines))
print('Solution 2:', part2(lines))
