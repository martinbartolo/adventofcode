import re

file = open("input.txt", "r")
text = file.read().strip()


def part1(text):
    number_pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)
    return sum(int(x) * int(y) for (x, y) in number_pairs)


def part2(text):
    number_pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', text)
    count = True
    total = 0
    for pair in number_pairs:
        if pair[0] and pair[1] and count:
            total += int(pair[0]) * int(pair[1])
        if pair[2]:
            count = True
        if pair[3]:
            count = False
    return total


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
