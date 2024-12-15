import copy

file = open('test.txt', 'r')
text = file.read().strip()


def clean_text(text: str):
    grid, moves = text.split('\n\n')
    grid = [list(row) for row in grid.splitlines()]
    moves = moves.replace('\n', '')
    start = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                start = (i, j)
    return grid, moves, start


move_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def part1(grid: list[list[str]], moves: str, start: tuple[int, int]):
    # make the moves
    robot = start
    for move in moves:
        dx, dy = move_map[move]
        x, y = robot
        if grid[x + dx][y + dy] == '.':
            grid[x][y] = '.'
            grid[x + dx][y + dy] = '@'
            robot = (x + dx, y + dy)
        elif grid[x + dx][y + dy] == 'O':
            push_pos = [x + dx, y + dy]
            while 0 < push_pos[0] < len(grid) and 0 < push_pos[1] < len(grid[0]):
                if grid[push_pos[0]][push_pos[1]] == '#':
                    break
                elif grid[push_pos[0]][push_pos[1]] == '.':
                    grid[push_pos[0]][push_pos[1]] = 'O'
                    grid[x + dx][y + dy] = '@'
                    grid[x][y] = '.'
                    robot = (x + dx, y + dy)
                    break
                push_pos = [push_pos[0] + dx, push_pos[1] + dy]

    # sum the coords
    total = 0
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            if x == 'O':
                total += 100 * i + j
    return total


grid, moves, start = clean_text(text)
print('Solution 1:', part1(copy.deepcopy(grid), moves, start))
# cheated for part 2 (nightmare)
