file = open("input.txt", "r")
text = file.read().strip()

#################### Part 1 ####################


def sum_extrapolated_values(text: str):
    histories = [[int(num) for num in line.strip().split(" ")] for line in text.splitlines()]
    total = 0
    for history in histories:
        # build sequences
        current = history
        sequences: list[list[int]] = [current]
        while not all(num == 0 for num in current):
            current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
            sequences.append(current)
        # get value
        value = 0
        for i in range(len(sequences) - 2, -1, -1):
            value += sequences[i][-1]
        total += value

    return total


print("Solution 1:", sum_extrapolated_values(text))


#################### Part 2 ####################
def sum_extrapolated_values_backwards(text: str):
    histories = [[int(num) for num in line.strip().split(" ")] for line in text.splitlines()]
    total = 0
    for history in histories:
        # build sequences
        current = history
        sequences: list[list[int]] = [current]
        while not all(num == 0 for num in current):
            current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
            sequences.append(current)
        # reverse sequences
        sequences_reversed = [sequence[::-1] for sequence in sequences]
        # get value
        value = 0
        for i in range(len(sequences_reversed) - 2, -1, -1):
            value = sequences_reversed[i][-1] - value
        total += value

    return total


print("Solution 2:", sum_extrapolated_values_backwards(text))
