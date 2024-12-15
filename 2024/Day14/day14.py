file = open('input.txt', 'r')
text = file.read().strip()


def clean_text(text):
    lines = text.splitlines()
    ps, vs = zip(*[line.split() for line in lines])
    ps = [[int(x) for x in p.split('p=')[1].split(',')] for p in ps]
    vs = [[int(x) for x in v.split('v=')[1].split(',')] for v in vs]
    return ps, vs


def part1(ps, vs, width, height):
    final_positions = []
    for i in range(len(ps)):
        final_x = (ps[i][0] + vs[i][0] * 100) % width
        final_y = (ps[i][1] + vs[i][1] * 100) % height
        final_positions.append([final_x, final_y])

    # calculate safety factor
    tl, tr, bl, br = [0, 0, 0, 0]
    mid_w = width // 2
    mid_h = height // 2
    for px, py in final_positions:
        if px < mid_w:
            if py < mid_h:
                tl += 1
            elif py > mid_h:
                bl += 1
        elif px > mid_w:
            if py < mid_h:
                tr += 1
            elif py > mid_h:
                br += 1
    return tl * tr * bl * br


def part2(ps, vs, width, height, steps):
    for step in range(steps):
        # Create empty grid
        grid = [['.'] * width for _ in range(height)]

        # Update positions and mark them on grid
        for i in range(len(ps)):
            # Update position
            ps[i][0] = (ps[i][0] + vs[i][0]) % width
            ps[i][1] = (ps[i][1] + vs[i][1]) % height

            # Mark position on grid
            x, y = ps[i]
            grid[y][x] = '#'

        tree = False
        for line in grid:
            line_str = ''.join(line)
            if '##########' in line_str:
                tree = True

        # Print grid
        if tree:
            print('Seconds elapsed:', step + 1)
            for row in grid:
                print(''.join(row))


ps, vs = clean_text(text)
print('Solution 1:', part1(ps, vs, 101, 103))
part2(ps, vs, 101, 103, 10000)
