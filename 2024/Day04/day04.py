file = open('input.txt', 'r')
text = file.read().strip()


def part1(text):
    lines = text.splitlines()
    dim = len(lines)
    total = 0
    for i in range(dim):
        for j in range(dim):
            if lines[i][j] != 'X':
                continue
            up = (
                i >= 3
                and lines[i - 1][j] == 'M'
                and lines[i - 2][j] == 'A'
                and lines[i - 3][j] == 'S'
            )
            up_right = (
                i >= 3
                and j < dim - 3
                and lines[i - 1][j + 1] == 'M'
                and lines[i - 2][j + 2] == 'A'
                and lines[i - 3][j + 3] == 'S'
            )
            right = (
                j < dim - 3
                and lines[i][j + 1] == 'M'
                and lines[i][j + 2] == 'A'
                and lines[i][j + 3] == 'S'
            )
            down_right = (
                i < dim - 3
                and j < dim - 3
                and lines[i + 1][j + 1] == 'M'
                and lines[i + 2][j + 2] == 'A'
                and lines[i + 3][j + 3] == 'S'
            )
            down = (
                i < dim - 3
                and lines[i + 1][j] == 'M'
                and lines[i + 2][j] == 'A'
                and lines[i + 3][j] == 'S'
            )
            down_left = (
                i < dim - 3
                and j >= 3
                and lines[i + 1][j - 1] == 'M'
                and lines[i + 2][j - 2] == 'A'
                and lines[i + 3][j - 3] == 'S'
            )
            left = (
                j >= 3
                and lines[i][j - 1] == 'M'
                and lines[i][j - 2] == 'A'
                and lines[i][j - 3] == 'S'
            )
            up_left = (
                i >= 3
                and j >= 3
                and lines[i - 1][j - 1] == 'M'
                and lines[i - 2][j - 2] == 'A'
                and lines[i - 3][j - 3] == 'S'
            )
            found = [up, up_right, right, down_right, down, down_left, left, up_left]
            total += len([x for x in found if x])
    return total


def part2(text):
    lines = text.splitlines()
    dim = len(lines)
    total = 0
    for i in range(dim):
        for j in range(dim):
            inbounds = 1 <= i < dim - 1 and 1 <= j < dim - 1
            if lines[i][j] != 'A' or not inbounds:
                continue
            top = (
                lines[i - 1][j - 1] == 'M'
                and lines[i - 1][j + 1] == 'M'
                and lines[i + 1][j - 1] == 'S'
                and lines[i + 1][j + 1] == 'S'
            )
            right = (
                lines[i - 1][j + 1] == 'M'
                and lines[i + 1][j + 1] == 'M'
                and lines[i - 1][j - 1] == 'S'
                and lines[i + 1][j - 1] == 'S'
            )
            bottom = (
                lines[i + 1][j - 1] == 'M'
                and lines[i + 1][j + 1] == 'M'
                and lines[i - 1][j - 1] == 'S'
                and lines[i - 1][j + 1] == 'S'
            )
            left = (
                lines[i - 1][j - 1] == 'M'
                and lines[i + 1][j - 1] == 'M'
                and lines[i - 1][j + 1] == 'S'
                and lines[i + 1][j + 1] == 'S'
            )
            if any([top, right, bottom, left]):
                total += 1
    return total


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
