file = open("input.txt", "r")
text = file.read().strip()
steps = text.split(",")


#################### Part 1 ####################


def hash(s: str):
    result = 0
    for char in s:
        result += ord(char)
        result *= 17
        result %= 256
    return result


def initialize(steps: list[str]):
    total = 0
    for step in steps:
        total += hash(step)
    return total


print("Solution 1: ", initialize(steps))


#################### Part 2 ####################


def focusing_power(steps: list[str]):
    # build hashmap
    hashmap = {k: [] for k in range(256)}
    for step in steps:
        if "-" in step:
            label = step.split("-")[0]
            box = hash(label)
            labels = [lens[0] for lens in hashmap[box]]
            if any(label == l for l in labels):
                label_index = labels.index(label)
                del hashmap[box][label_index]
        else:
            # '=' operation
            operation = step.split("=")
            label = operation[0]
            focal_length = operation[1]
            box = hash(label)
            labels = [lens[0] for lens in hashmap[box]]
            if any(label == l for l in labels):
                label_index = labels.index(label)
                hashmap[box][label_index][1] = int(focal_length)
            else:
                hashmap[box].append([label, int(focal_length)])

    # calculate focusing power
    focusing_power = 0
    for i in range(256):
        for j, lens in enumerate(hashmap[i]):
            focusing_power += (i + 1) * (j + 1) * lens[1]

    return focusing_power


print("Solution 2: ", focusing_power(steps))
