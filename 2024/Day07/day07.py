file = open('input.txt', 'r')
text = file.read().strip()


def clean_text(text):
    answers = []
    numbers = []
    for line in text.splitlines():
        split_line = line.split(':')
        answers.append(int(split_line[0]))
        numbers.append([int(x) for x in split_line[1].strip().split()])
    return answers, numbers


def calculate(numbers, i, result, answer):
    # If we reached the end of numbers check if our result matches the answer
    if i >= len(numbers):
        return result == answer
    # If we did not check the next part of the calculation with a + or *
    return calculate(numbers, i + 1, result + numbers[i], answer) or calculate(
        numbers, i + 1, result * numbers[i], answer
    )


def part1(answers, numbers):
    result = 0
    for answer, nums in zip(answers, numbers):
        if calculate(nums, 0, 0, answer):
            result += answer
    return result


def calculate2(numbers, i, result, answer):
    # If we reached the end of numbers check if our result matches the answer
    if i >= len(numbers):
        return result == answer
    # If we did not check the next part of the calculation with a + or * or ||
    return (
        calculate2(numbers, i + 1, result + numbers[i], answer)
        or calculate2(numbers, i + 1, result * numbers[i], answer)
        or calculate2(numbers, i + 1, int(str(result) + str(numbers[i])), answer)
    )


def part2(answers, numbers):
    result = 0
    for answer, nums in zip(answers, numbers):
        if calculate2(nums, 0, 0, answer):
            result += answer
    return result


answers, numbers = clean_text(text)
print('Solution 1:', part1(answers, numbers))
print('Solution2:', part2(answers, numbers))
