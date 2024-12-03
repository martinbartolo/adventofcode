file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text):
    return [[int(level) for level in line.split()] for line in text.splitlines()]


def is_valid_sequence(nums):
    increasing = ""
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff < -3 or diff == 0 or diff > 3:
            return False
        if diff < 0 and increasing is True:
            return False
        if diff > 0 and increasing is False:
            return False
        if diff > 0:
            increasing = True
        if diff < 0:
            increasing = False
    return True


def part1(reports):
    total_safe = 0
    for report in reports:
        if is_valid_sequence(report):
            total_safe += 1
    return total_safe


def part2(reports):
    total_safe = 0
    for report in reports:
        # First check if it's already safe without removing any number
        if is_valid_sequence(report):
            total_safe += 1
            continue

        # Try removing each number one at a time
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            if is_valid_sequence(modified_report):
                total_safe += 1
                break
    return total_safe


reports = clean_text(text)
print("Solution 1: ", part1(reports))
print("Solution 2: ", part2(reports))
