import copy
from collections import deque

file = open('input.txt', 'r')
text = file.read().strip()


def get_start(grid: list[list[str]]):
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            if x == 'S':
                return (i, j)


def get_end(grid: list[list[str]]):
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            if x == 'E':
                return (i, j)


def print_grid(grid: list[list[str]]):
    for line in grid:
        print(''.join(line))
    print()


def bfs(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[x][y] != '#'

    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        pos, steps = queue.popleft()

        if pos == end:
            return steps

        x, y = pos
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            next_pos = (next_x, next_y)

            if next_pos not in seen and is_valid(next_x, next_y):
                queue.append((next_pos, steps + 1))
                seen.add(next_pos)

    return -1  # No path found


def bfs_with_cheat(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    def is_valid(x: int, y: int):
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

    # State: (position, steps, cheat_steps_used, is_cheating, cheat_start_pos)
    queue = deque([(start, 0, 0, False, None)])
    # Track unique paths by their cheat start position and end state
    seen = set()
    # Track unique paths that save >= 100 steps by their cheat start position
    valid_cheats = set()
    original_steps = bfs(grid, start, end)

    while queue:
        pos, steps, cheat_steps, is_cheating, cheat_start = queue.popleft()
        state = (pos, cheat_steps, is_cheating, cheat_start)

        if state in seen:
            continue
        seen.add(state)

        if pos == end and not is_cheating:
            if (
                steps < original_steps
                and original_steps - steps >= 100
                and cheat_start is not None
            ):
                valid_cheats.add(cheat_start)
            continue

        x, y = pos
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            next_pos = (next_x, next_y)

            if not is_valid(next_x, next_y):
                continue

            # If we hit a wall and aren't cheating, we can start cheating
            if grid[next_x][next_y] == '#' and not is_cheating:
                queue.append((next_pos, steps + 1, 1, True, (next_x, next_y)))

            # If we're cheating and still have steps available
            elif is_cheating and cheat_steps < 20:
                # Always try to stop cheating if we're on a valid path
                if grid[next_x][next_y] == '.' or grid[next_x][next_y] in 'SE':
                    queue.append((next_pos, steps + 1, 0, False, cheat_start))

                # Continue cheating regardless if we can stop or not
                queue.append((next_pos, steps + 1, cheat_steps + 1, True, cheat_start))

            # Normal movement without cheating
            elif not is_cheating and grid[next_x][next_y] != '#':
                queue.append((next_pos, steps + 1, 0, False, cheat_start))

    return len(valid_cheats)


def part1(text: str):
    grid = [list(line) for line in text.splitlines()]
    start = get_start(grid)
    end = get_end(grid)

    original = bfs(grid, start, end)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid_copy = copy.deepcopy(grid)
            if grid_copy[i][j] == '#':
                grid_copy[i][j] = '.'
            new_shortest = bfs(grid_copy, start, end)
            if new_shortest < original and original - new_shortest >= 100:
                total += 1
    return total


def part2(text: str):
    grid = [list(line) for line in text.splitlines()]
    start = get_start(grid)
    end = get_end(grid)
    return bfs_with_cheat(grid, start, end)


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
