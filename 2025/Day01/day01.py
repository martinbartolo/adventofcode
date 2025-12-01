file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text):
    return [(line[0], int(line[1:])) for line in text.splitlines()]


def part1(rotations):
    dial = 50
    password = 0
    for rot in rotations:
        dir = rot[0]
        dist = rot[1] % 100
        if dir == "L":
            new = dial - dist
            if new < 0:
                dial = 100 + new
            else:
                dial = new
        else:  # dir == R
            new = dial + dist
            if new > 99:
                dial = new - 100
            else:
                dial = new
        if dial == 0:
            password += 1
    return password


def part2(rotations):
    dial = 50
    password = 0
    for rot in rotations:
        dir = rot[0]
        dist = rot[1] % 100
        extra = rot[1] // 100
        startedOnZero = dial == 0
        if dir == "L":
            new = dial - dist
            if new < 0:
                dial = 100 + new
                if dial != 0 and not startedOnZero:
                    password += 1
            else:
                dial = new
        else:  # dir == R
            new = dial + dist
            if new > 99:
                dial = new - 100
                if dial != 0 and not startedOnZero:
                    password += 1
            else:
                dial = new
        if dial == 0:
            password += 1
        password += extra
    return password


rotations = clean_text(text)
print("Solution 1: ", part1(rotations))
print("Solution 2: ", part2(rotations))
