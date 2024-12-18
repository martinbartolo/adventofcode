from collections import deque
from typing import List, Tuple


def parse_input(filename: str, bytes: int = None) -> List[Tuple[int, int]]:
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()
        if bytes is not None:
            lines = lines[:bytes]
        return [tuple(map(int, line.split(','))) for line in lines]


def part1(obstacles: List[Tuple[int, int]], grid_size: int = 71) -> int:
    grid = {
        (x, y): '#' if (x, y) in obstacles else '.'
        for x in range(grid_size)
        for y in range(grid_size)
    }

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < grid_size and 0 <= y < grid_size and grid[(x, y)] != '#'

    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

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


def part2(obstacles: List[Tuple[int, int]], grid_size: int = 71) -> Tuple[int, int]:
    # Binary search to find the first obstacle that blocks the path
    left = 1
    right = len(obstacles)

    while left < right:
        mid = (left + right) // 2
        if part1(obstacles[:mid], grid_size) == -1:
            right = mid
        else:
            left = mid + 1

    return str(obstacles[left - 1]).strip('()').replace(' ', '')


obstacles = parse_input('input.txt', bytes=1024)
print('Part 1:', part1(obstacles, grid_size=71))
obstacles = parse_input('input.txt')
print('Part 2:', part2(obstacles, grid_size=71))
