file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text: str):
    parts, designs = text.split('\n\n')
    parts = parts.split(', ')
    designs = designs.split()
    return parts, designs


def check_design(design: str, parts):
    if design == '':
        return True
    for part in parts:
        if design.startswith(part):
            if check_design(design[len(part) :], parts):
                return True
    return False


def part1(parts: list[str], designs: list[str]):
    parts = set(parts)
    total = 0
    for design in designs:
        if check_design(design, parts):
            total += 1
    return total


def get_num_patterns(design: str, parts, memo=None):
    if memo is None:
        memo = {}

    if design in memo:
        return memo[design]

    if design == '':
        return 1

    total = 0
    for part in parts:
        if design.startswith(part):
            total += get_num_patterns(design[len(part) :], parts, memo)

    memo[design] = total
    return total


def part2(parts: list[str], designs: list[str]):
    parts = set(parts)
    total = 0
    for design in designs:
        total += get_num_patterns(design, parts)
    return total


parts, designs = clean_text(text)
print('Solution 1:', part1(parts, designs))
print('Solution 2:', part2(parts, designs))
