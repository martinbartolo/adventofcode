from heapq import heappop, heappush

file = open('input.txt', 'r')
text = file.read().strip()
maze = text.splitlines()


def solve(maze: list[str]):
    start = None
    end = None

    for i, line in enumerate(maze):
        for j, x in enumerate(line):
            if x == 'S':
                start = (i, j)
            elif x == 'E':
                end = (i, j)

    # Priority queue: (cost, pos_i, pos_j, dir_i, dir_j)
    queue = [(0, start[0], start[1], 0, 1)]
    visited = set()
    shortest_cost = float('inf')

    while queue:
        cost, i, j, dir_i, dir_j = heappop(queue)

        # Found the end
        if (i, j) == end:
            shortest_cost = cost
            break

        # Skip if we've seen this state before
        state = (i, j, dir_i, dir_j)
        if state in visited:
            continue
        visited.add(state)

        # Try all possible directions
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            # Check walls
            if maze[ni][nj] == '#':
                continue

            new_cost = cost + (1 if (di, dj) == (dir_i, dir_j) else 1001)
            heappush(queue, (new_cost, ni, nj, di, dj))

    print('Solution 1:', shortest_cost)
    # cheated on part 2


solve(maze)
