file = open("day-14.txt", "r")
text = file.read()


#################### Part 1 ####################


def shift_left(line: list[str]):
    for p1 in range(len(line)):
        if line[p1] == ".":
            for p2 in range(p1 + 1, len(line)):
                if line[p2] == "O":
                    # shift rock
                    line[p1] = "O"
                    line[p2] = "."
                    break
                if line[p2] == "#":
                    break
    return line


def total_load(text: str):
    rows = text.splitlines()
    cols = list(map(list, zip(*rows)))
    cols_shifted = [shift_left(col) for col in cols]
    rows_shifted = list(map("".join, zip(*cols_shifted)))

    # calculate load
    total = 0
    for i, row in enumerate(rows_shifted):
        for char in row:
            if char == "O":
                total += len(rows_shifted) - i
    return total


print("Solution 1: ", total_load(text))


#################### Part 2 ####################


def shift_north(rows):
    cols = list(map(list, zip(*rows)))
    cols_shifted = [shift_left(col) for col in cols]
    return list(map("".join, list(zip(*cols_shifted))))


def shift_west(rows):
    return list(map("".join, [shift_left([*row]) for row in rows]))


def shift_south(rows):
    cols_reversed = [list(reversed(row)) for row in list(map(list, zip(*rows)))]
    cols_shifted = [list(reversed(shift_left(col))) for col in cols_reversed]
    return list(map("".join, zip(*cols_shifted)))


def shift_east(rows):
    rows_reversed = [list(reversed([*row])) for row in rows]
    return list(map("".join, [list(reversed(shift_left(row))) for row in rows_reversed]))


def cycle(rows: list[str]):
    return shift_east(shift_south(shift_west(shift_north(rows))))


def total_load_2(text: str):
    rows = text.splitlines()
    row_length = len(rows[0])

    memory: dict[str, int] = {}
    i = 0
    while True:
        flat_rows = "".join(rows)
        if flat_rows in memory:
            # we have found a cycle
            cycle_start = memory[flat_rows]
            break
        memory[flat_rows] = i
        rows = cycle(rows)
        i += 1

    # ignore the ones before the cycle
    cycles_after_initial = 1_000_000_000 - cycle_start

    # configuration after all cycles
    configuration_index = cycles_after_initial % (len(memory) - cycle_start)
    configuration_string = list(memory.keys())[cycle_start:][configuration_index]
    configuration = [
        (configuration_string[i : i + row_length])
        for i in range(0, len(configuration_string), row_length)
    ]

    # calculate load
    total = 0
    for i, row in enumerate(configuration):
        for char in row:
            if char == "O":
                total += len(configuration) - i
    return total


print("Solution 2: ", total_load_2(text))
