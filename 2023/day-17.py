# CHEATED - Solution copied from https://www.reddit.com/r/adventofcode/comments/18k9ne5/comment/kdq86mr/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# I knew I had to use Dijkstra's algorithm and found the shortest path but could not figure out how to limit to 3 moves in a row :(
import heapq


def minimal_heat(start, end, least, most):
    queue = [(0, *start, 0, 0)]
    seen = set()
    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))
        # calculate turns only
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(px, py), (-px, -py)}:
            a, b, h = x, y, heat
            for i in range(1, most + 1):
                a, b = a + dx, b + dy
                if (a, b) in board:
                    h += board[a, b]
                    if i >= least:
                        heapq.heappush(queue, (h, a, b, dx, dy))  # type: ignore


file = open("day-17.txt", "r")
text = file.read()
lines = text.splitlines()
board = {(i, j): int(c) for i, r in enumerate(lines) for j, c in enumerate(r)}
print(minimal_heat((0, 0), max(board), 1, 3))
print(minimal_heat((0, 0), max(board), 4, 10))
