file = open("input.txt", "r")
text = file.read().strip()


def expand_rows(lines: list[str]):
    lines_expanded: list[str] = []

    # Expand empty rows
    for line in lines:
        found_galaxy = False
        for char in line:
            if char == "#":
                found_galaxy = True
                break
        lines_expanded.append(line)
        if not found_galaxy:
            lines_expanded.append("." * len(line))
    return lines_expanded


def sum_path_lengths(text: str):
    lines = text.splitlines()
    # Expand empty rows
    lines = expand_rows(lines)
    # Expand empty cols
    lines_T = list(map(list, zip(*lines)))
    lines_T = ["".join(line) for line in lines_T]
    lines = list(map(list, zip(*expand_rows(lines_T))))
    lines = ["".join(line) for line in lines]

    # Map galaxy positions
    universe: dict[int, tuple[int, int]] = {}
    galaxy_num = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                universe[galaxy_num] = (i, j)
                galaxy_num += 1

    # Gather Distances
    distances: dict[tuple[int, int], int] = {}
    for start in universe:
        for end in range(start + 1, len(universe)):
            distances[(start, end)] = abs((universe[end][0] - universe[start][0])) + abs(
                (universe[end][1] - universe[start][1])
            )
    return sum(distances.values())


print("Solution 1: ", sum_path_lengths(text))

#################### Part 2 ####################


def find_empty_rows(lines: list[str]):
    empty_rows: list[int] = []
    for i, line in enumerate(lines):
        found_galaxy = False
        for char in line:
            if char == "#":
                found_galaxy = True
                break
        if not found_galaxy:
            empty_rows.append(i)
    return empty_rows


def sum_path_lengths_2(text: str):
    lines = text.splitlines()

    # Map galaxy positions
    universe: dict[int, tuple[int, int]] = {}
    galaxy_num = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                universe[galaxy_num] = (i, j)
                galaxy_num += 1

    # Find empty rows
    empty_rows = find_empty_rows(lines)
    lines_T = list(map(list, zip(*lines)))
    lines_T = ["".join(line) for line in lines_T]
    empty_cols = find_empty_rows(lines_T)

    # Gather Distances
    distances: dict[tuple[int, int], int] = {}
    for start in universe:
        for end in range(start + 1, len(universe)):
            distances[(start, end)] = abs((universe[end][0] - universe[start][0])) + abs(
                (universe[end][1] - universe[start][1])
            )
            # Add empty rows
            for row in empty_rows:
                if universe[start][0] < row < universe[end][0]:
                    distances[(start, end)] += 999999
            # Add empty cols
            for col in empty_cols:
                if (
                    universe[start][1] < col < universe[end][1]
                    or universe[start][1] > col > universe[end][1]
                ):
                    distances[(start, end)] += 999999
    return sum(distances.values())


print("Solution 2: ", sum_path_lengths_2(text))
