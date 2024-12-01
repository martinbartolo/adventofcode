from collections import Counter

file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text):
    list1 = []
    list2 = []
    for line in text.splitlines():
        line_split = line.split()
        list1.append(int(line_split[0]))
        list2.append(int(line_split[1]))
    return list1, list2


def part1(list1, list2):
    list1, list2 = sorted(list1), sorted(list2)
    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])
    return total


def part2(list1, list2):
    counts = Counter(list2)
    total = 0
    for num in list1:
        total += num * counts[num]
    return total


list1, list2 = clean_text(text)
print("Solution 1: ", part1(list1, list2))
print("Solution 2: ", part2(list1, list2))
