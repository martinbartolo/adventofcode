# Note: file must have a newline at the end
file = open("input.txt", "r")
lines = file.readlines()


#################### Part 1 ####################
def is_symbol(ch: str):
    return not (ch.isdigit() or ch == ".")


def symbol_adjacent(lines: list[str], i: int, j: int, n: int, m: int):
    # top left
    if i > 0 and j > 0 and is_symbol(lines[i - 1][j - 1]):
        return True
    # top
    if i > 0 and is_symbol(lines[i - 1][j]):
        return True
    # top right
    if i > 0 and j < m - 2 and is_symbol(lines[i - 1][j + 1]):
        return True
    # right
    if j < m - 2 and is_symbol(lines[i][j + 1]):
        return True
    # bottom right
    if i < n - 1 and j < m - 2 and is_symbol(lines[i + 1][j + 1]):
        return True
    # bottom
    if i < n - 1 and is_symbol(lines[i + 1][j]):
        return True
    # bottom left
    if i < n - 1 and j > 0 and is_symbol(lines[i + 1][j - 1]):
        return True
    # left
    if j > 0 and is_symbol(lines[i][j - 1]):
        return True

    return False


def sum_part_nums(lines: list[str]):
    n = len(lines)
    m = len(lines[0])
    part_num_total = 0
    for i in range(n):
        is_part_num = False
        cur_num = ""
        for j in range(m):
            if lines[i][j].isdigit():
                cur_num += lines[i][j]
                if not is_part_num and symbol_adjacent(lines, i, j, n, m):
                    # number is part_num
                    is_part_num = True
            # check for end of number
            else:
                if cur_num != "" and is_part_num:
                    part_num_total += int(cur_num)
                is_part_num = False
                cur_num = ""

    return part_num_total


print("Solution 1: ", sum_part_nums(lines))


#################### Part 2 ####################
def get_full_num(line: str, j: int, m: int):
    while line[j - 1].isdigit() and j > 0:
        j -= 1
    full_num = ""
    while line[j].isdigit() and j < m - 1:
        full_num += line[j]
        j += 1
    return full_num


def get_gear_nums(lines: list[str], i: int, j: int, n: int, m: int):
    gear_nums: list[str] = []

    found_top_left = False
    found_top = False
    found_bottom_right = False
    found_bottom = False

    # top left
    if i > 0 and j > 0 and lines[i - 1][j - 1].isdigit():
        found_top_left = True
        gear_nums.append(get_full_num(lines[i - 1], j - 1, m))
    # top
    if i > 0 and lines[i - 1][j].isdigit():
        found_top = True
        if not found_top_left:
            gear_nums.append(get_full_num(lines[i - 1], j, m))
    # top right
    if i > 0 and j < m - 2 and lines[i - 1][j + 1].isdigit() and not found_top:
        gear_nums.append(get_full_num(lines[i - 1], j + 1, m))
    # right
    if j < m - 2 and lines[i][j + 1].isdigit():
        gear_nums.append(get_full_num(lines[i], j + 1, m))
    # bottom right
    if i < n - 1 and j < m - 2 and lines[i + 1][j + 1].isdigit():
        found_bottom_right = True
        gear_nums.append(get_full_num(lines[i + 1], j + 1, m))
    # bottom
    if i < n - 1 and lines[i + 1][j].isdigit():
        found_bottom = True
        if not found_bottom_right:
            gear_nums.append(get_full_num(lines[i + 1], j, m))
    # bottom left
    if i < n - 1 and j > 0 and lines[i + 1][j - 1].isdigit() and not found_bottom:
        gear_nums.append(get_full_num(lines[i + 1], j, m))
    # left
    if j > 0 and lines[i][j - 1].isdigit():
        gear_nums.append(get_full_num(lines[i], j - 1, m))

    return gear_nums


def sum_gear_ratios(lines: list[str]):
    # say size of lines is n x m
    n = len(lines)
    m = len(lines[0])
    gear_ratios_total = 0
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "*":
                gear_nums = get_gear_nums(lines, i, j, n, m)
                if len(gear_nums) == 2:
                    gear_ratios_total += int(gear_nums[0]) * int(gear_nums[1])

    return gear_ratios_total


print("Solution 2: ", sum_gear_ratios(lines))
