import copy

file = open('input.txt', 'r')
text = file.read().strip()


def find_start(lines, dim):
    for i in range(dim):
        for j in range(dim):
            if lines[i][j] == '^':
                return i, j


def part1(lines):
    dim = len(lines)
    i, j = find_start(lines, dim)
    lines[i][j] = 'X'

    dir = 'up'
    total = 1
    while True:
        # calculate next position
        di = 0
        dj = 0
        if dir == 'up':
            di = -1
        elif dir == 'down':
            di = 1
        elif dir == 'left':
            dj = -1
        elif dir == 'right':
            dj = 1

        # move to next position
        i += di
        j += dj

        # end if guard leaves the area
        if i < 0 or j < 0 or i >= dim or j >= dim:
            break

        if lines[i][j] == '#':
            # we hit an obstacle
            # undo the movement and turn
            i -= di
            j -= dj
            if dir == 'up':
                dir = 'right'
            elif dir == 'down':
                dir = 'left'
            elif dir == 'left':
                dir = 'up'
            elif dir == 'right':
                dir = 'down'
        elif lines[i][j] == '.':
            # we hit a dot
            # mark as visited and add to total
            lines[i][j] = 'X'
            total += 1
    return total


def has_loop(lines, dim, start):
    i, j = start
    lines[i][j] = 'X'

    obstacle_hits = {}
    dir = 'up'
    while True:
        # calculate next position
        di = 0
        dj = 0
        if dir == 'up':
            di = -1
        elif dir == 'down':
            di = 1
        elif dir == 'left':
            dj = -1
        elif dir == 'right':
            dj = 1

        # move to next position
        i += di
        j += dj

        # no loop if guard leaves the area
        if i < 0 or j < 0 or i >= dim or j >= dim:
            return False

        if lines[i][j] == '#':
            if (i, j) in obstacle_hits:
                # we have hit this wall before
                if dir in obstacle_hits[(i, j)]:
                    # we have hit this wall from the same direction
                    # meaning that we found a loop
                    return True
                else:
                    # we have hit this wall from a new direction
                    # add it to set of obstacle's hits
                    obstacle_hits[(i, j)].add(dir)
            else:
                # we have never hit this wall before
                # make a new obstacle hit set
                obstacle_hits[(i, j)] = {dir}

            # undo the movement and turn
            i -= di
            j -= dj
            if dir == 'up':
                dir = 'right'
            elif dir == 'down':
                dir = 'left'
            elif dir == 'left':
                dir = 'up'
            elif dir == 'right':
                dir = 'down'


def part2(lines):
    dim = len(lines)
    start = find_start(lines, dim)
    start_i, start_j = start
    lines[start_i][start_j] = '.'

    loops = 0
    for i in range(dim):
        for j in range(dim):
            new_lines = copy.deepcopy(lines)
            if new_lines[i][j] == '.':
                # put a new wall in each possible empty spot and check if it causes a loop
                new_lines[i][j] = '#'
                if has_loop(new_lines, dim, start):
                    loops += 1
    return loops


lines = [list(line) for line in text.splitlines()]

print('Solution 1:', part1(copy.deepcopy(lines)))
print('Solution 2:', part2(copy.deepcopy(lines)))
