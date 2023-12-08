import math

file = open("day-08.txt", "r")
text = file.read()


#################### Part 1 ####################


def create_map(map_raw: list[str]):
    map: dict[str, list[str]] = {}
    for line in map_raw:
        key = line.split("=")[0].strip()
        left = line.split("=")[1].strip().split(",")[0].strip("(")
        right = line.split("=")[1].strip().split(",")[1].strip(" )")
        map[key] = [left, right]
    return map


def num_steps(text: str):
    instructions = text.split("\n\n")[0]
    map_raw = text.split("\n\n")[1].splitlines()
    map = create_map(map_raw)

    position = "AAA"
    steps = 0
    i = 0
    # Follow instructions
    while i < len(instructions):
        steps += 1
        # Go to the next position
        if instructions[i] == "L":
            position = map[position][0]
        else:
            position = map[position][1]

        # Check if we reached the end
        if position == "ZZZ":
            return steps

        # Next instruction
        if i == len(instructions) - 1:
            i = 0
        else:
            i += 1


print("Solution 1: ", num_steps(text))


#################### Part 2 ####################


def get_steps(map: dict[str, list[str]], instructions: str, start: str):
    position = start
    i = 0
    cycle_length = 0
    while i < len(instructions):
        # Go to the next position
        if instructions[i] == "L":
            position = map[position][0]
        else:
            position = map[position][1]

        cycle_length += 1

        # Check if we reached the beginning of a cycle
        if position[-1] == "Z":
            return cycle_length

        # Next instruction
        if i == len(instructions) - 1:
            i = 0
        else:
            i += 1
    return 0


def num_steps_2(text: str):
    instructions = text.split("\n\n")[0]
    map_raw = text.split("\n\n")[1].splitlines()
    map = create_map(map_raw)

    positions = [position for position in map.keys() if position[-1] == "A"]
    result = 1
    for start in positions:
        result = math.lcm(result, get_steps(map, instructions, start))
    return result


print("Solution 2: ", num_steps_2(text))
