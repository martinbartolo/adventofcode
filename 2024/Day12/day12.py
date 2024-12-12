file = open('input.txt', 'r')
text = file.read().strip()


def calc_region(i, j, lines, plot, visited):
    # if out of bounds or outside region
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines) or lines[i][j] != plot:
        return 1, 0

    # if already visited
    if (i, j) in visited:
        return 0, 0

    # mark as visited
    visited.add((i, j))

    # Calculate perimeter and area by checking all 4 directions
    perimeter = 0
    area = 1  # current cell counts as 1 area

    up_p, up_a = calc_region(i - 1, j, lines, plot, visited)
    down_p, down_a = calc_region(i + 1, j, lines, plot, visited)
    left_p, left_a = calc_region(i, j - 1, lines, plot, visited)
    right_p, right_a = calc_region(i, j + 1, lines, plot, visited)

    area += up_a + down_a + left_a + right_a
    perimeter += up_p + down_p + left_p + right_p

    return perimeter, area


def part1(lines):
    visited = set()
    price = 0
    for i, line in enumerate(lines):
        for j, plot in enumerate(line):
            # skip if already visited
            if (i, j) in visited:
                continue
            perimeter, area = calc_region(i, j, lines, plot, visited)
            price += perimeter * area
    return price


# TLDR counting corners is the same as counting sides
def calc_region_sides(i, j, lines, plot, visited):
    # if out of bounds or outside region
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] != plot:
        return 0, 0

    # if already visited
    if (i, j) in visited:
        return 0, 0

    # mark as visited
    visited.add((i, j))

    # Calculate corners and area
    corners = 0
    area = 1  # current cell counts as 1 area

    # Check if current position is a corner
    is_up_outside = (
        i - 1 < 0 or i - 1 >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i - 1][j] != plot
    )
    is_down_outside = (
        i + 1 < 0 or i + 1 >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i + 1][j] != plot
    )
    is_left_outside = (
        i < 0 or i >= len(lines) or j - 1 < 0 or j - 1 >= len(lines[0]) or lines[i][j - 1] != plot
    )
    is_right_outside = (
        i < 0 or i >= len(lines) or j + 1 < 0 or j + 1 >= len(lines[0]) or lines[i][j + 1] != plot
    )
    is_up_left_outside = (
        i - 1 < 0
        or i - 1 >= len(lines)
        or j - 1 < 0
        or j - 1 >= len(lines[0])
        or lines[i - 1][j - 1] != plot
    )
    is_up_right_outside = (
        i - 1 < 0
        or i - 1 >= len(lines)
        or j + 1 < 0
        or j + 1 >= len(lines[0])
        or lines[i - 1][j + 1] != plot
    )
    is_down_left_outside = (
        i + 1 < 0
        or i + 1 >= len(lines)
        or j - 1 < 0
        or j - 1 >= len(lines[0])
        or lines[i + 1][j - 1] != plot
    )
    is_down_right_outside = (
        i + 1 < 0
        or i + 1 >= len(lines)
        or j + 1 < 0
        or j + 1 >= len(lines[0])
        or lines[i + 1][j + 1] != plot
    )

    # Top-left corner
    if is_up_outside and is_left_outside:
        corners += 1
    # Top-right corner
    if is_up_outside and is_right_outside:
        corners += 1
    # Bottom-left corner
    if is_down_outside and is_left_outside:
        corners += 1
    # Bottom-right corner
    if is_down_outside and is_right_outside:
        corners += 1
    # Top-left inner corner
    if is_up_left_outside and not is_up_outside and not is_left_outside:
        corners += 1
    # Top-right inner corner
    if is_up_right_outside and not is_up_outside and not is_right_outside:
        corners += 1
    # Bottom-left inner corner
    if is_down_left_outside and not is_down_outside and not is_left_outside:
        corners += 1
    # Bottom-right inner corner
    if is_down_right_outside and not is_down_outside and not is_right_outside:
        corners += 1

    up_c, up_a = calc_region_sides(i - 1, j, lines, plot, visited)
    down_c, down_a = calc_region_sides(i + 1, j, lines, plot, visited)
    left_c, left_a = calc_region_sides(i, j - 1, lines, plot, visited)
    right_c, right_a = calc_region_sides(i, j + 1, lines, plot, visited)

    area += up_a + down_a + left_a + right_a
    corners += up_c + down_c + left_c + right_c

    return corners, area


def part2(lines):
    visited = set()
    price = 0
    for i, line in enumerate(lines):
        for j, plot in enumerate(line):
            # skip if already visited
            if (i, j) in visited:
                continue
            sides, area = calc_region_sides(i, j, lines, plot, visited)
            price += sides * area
    return price


lines = text.splitlines()
print('Solution 1:', part1(lines))
print('Solution 2:', part2(lines))
