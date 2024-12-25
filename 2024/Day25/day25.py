file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text: str):
    schematics = text.split("\n\n")
    locks = []
    keys = []
    for schematic in schematics:
        lines = schematic.split()
        if lines[0] == "#" * len(lines[0]):
            lock_counts = [0] * len(lines[0])
            for line in lines[1:]:
                for i, char in enumerate(line):
                    if char == '#':
                        lock_counts[i] += 1
            locks.append(lock_counts)
        elif lines[0] == "." * len(lines[0]):
            key_counts = [0] * len(lines[0])
            for line in lines[:-1]:
                for i, char in enumerate(line):
                    if char == '#':
                        key_counts[i] += 1
            keys.append(key_counts)
    return locks, keys


def part1(locks, keys):
    dim = len(locks[0])
    result = 0
    for lock in locks:
        for key in keys:
            fits = True
            for i in range(dim):
                if lock[i] + key[i] > 5:
                    fits = False
                    break
            if fits:
                result += 1
    return result


locks, keys = clean_text(text)
print('Solution 1:', part1(locks, keys))
