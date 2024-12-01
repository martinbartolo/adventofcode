import sys

from tqdm import tqdm

sys.setrecursionlimit(10000)

file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()
empty_space_visited = []
mirrors_visited = []

#################### Part 1 ####################


def next_step(pos_y: int, pos_x: int, direction: str):
    # Check out of bounds
    if pos_x < 0 or pos_x >= len(lines[0]) or pos_y < 0 or pos_y >= len(lines):
        return

    # Directions
    directions = {"u": (-1, 0), "d": (1, 0), "r": (0, 1), "l": (0, -1)}
    mirrors = {
        "/": {"u": "r", "d": "l", "r": "u", "l": "d"},
        "\\": {"u": "l", "d": "r", "r": "d", "l": "u"},
        "|": {"u": "u", "d": "d", "r": ["u", "d"], "l": ["u", "d"]},
        "-": {"u": ["r", "l"], "d": ["r", "l"], "r": "r", "l": "l"},
    }

    # Empty space
    if lines[pos_y][pos_x] == ".":
        if (pos_y, pos_x) not in empty_space_visited:
            empty_space_visited.append((pos_y, pos_x))
        dy, dx = directions[direction]
        next_step(pos_y + dy, pos_x + dx, direction)

    # Mirror
    else:
        if lines[pos_y][pos_x] in mirrors:
            next_dirs = mirrors[lines[pos_y][pos_x]][direction]
            if isinstance(next_dirs, list):
                # Return if we have already hit the mirror from a flat end
                if lines[pos_y][pos_x] == "|":
                    if any((pos_y, pos_x, dir) in mirrors_visited for dir in ["r", "l"]):
                        return
                elif lines[pos_y][pos_x] == "-":
                    if any((pos_y, pos_x, dir) in mirrors_visited for dir in ["u", "d"]):
                        return
                mirrors_visited.append((pos_y, pos_x, direction))
                for next_dir in next_dirs:
                    dy, dx = directions[next_dir]
                    next_step(pos_y + dy, pos_x + dx, next_dir)
            else:
                # Return if we have already hit the mirror from this direction
                if (pos_y, pos_x, direction) in mirrors_visited:
                    return
                mirrors_visited.append((pos_y, pos_x, direction))
                dy, dx = directions[next_dirs]
                next_step(pos_y + dy, pos_x + dx, next_dirs)


def reset():
    global empty_space_visited
    global mirrors_visited
    empty_space_visited = []
    mirrors_visited = []


def energized_tiles(pos_y: int, pos_x: int, direction: str):
    reset()
    next_step(pos_y, pos_x, direction)
    mirrors_visited_positions = [(x[0], x[1]) for x in mirrors_visited]
    total = 0
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if (i, j) in empty_space_visited or (i, j) in mirrors_visited_positions:
                total += 1
    return total


print("Solution 1: ", energized_tiles(0, 0, "r"))


#################### Part 2 ####################


def all_possibilities():
    most_energized = 0
    # Top Row
    for i in tqdm(range(len(lines[0])), desc="Top Row"):
        most_energized = max(most_energized, energized_tiles(0, i, "d"))
    # Bottom Row
    for i in tqdm(range(len(lines[0])), desc="Bottom Row"):
        most_energized = max(most_energized, energized_tiles(len(lines) - 1, i, "u"))
    # Left Column
    for i in tqdm(range(len(lines)), desc="Left Col"):
        most_energized = max(most_energized, energized_tiles(i, 0, "r"))
    # Right Column
    for i in tqdm(range(len(lines)), desc="Right Col"):
        most_energized = max(most_energized, energized_tiles(i, len(lines[0]) - 1, "l"))
    return most_energized


print("Solution 2: ", all_possibilities())
