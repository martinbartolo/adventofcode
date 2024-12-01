word_to_digit = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def replace_words(text: str):
    for key, value in word_to_digit.items():
        text = text.replace(key, value)
    return text


def calibration(lines: list[str]):
    result = 0
    for line in lines:
        numbers: list[str] = []

        # pull out all numbers from the line
        for ch in line:
            if ch.isdigit():
                numbers.append(ch)

        # combine first and last digits into 2 digit string and convert to int
        result += int(numbers[0] + numbers[-1])
    return result


file = open("input.txt", "r")
text = file.read().strip()

print("Solution 1: ", calibration(text.split("\n")))
print("Solution 2: ", calibration(replace_words(text).split("\n")))
