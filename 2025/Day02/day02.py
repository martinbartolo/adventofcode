file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text):
    return [id.split('-') for id in text.split(',')]


# Take first half of a number e.g. 1 from 11
def get_half(num_string: str):
    return int(num_string[0 : (len(num_string) // 2)])


# Get full number from a half e.g. 11 from 1
def get_full(num: int):
    return int(str(num) + str(num))


def part1(pairs: list[list[str]]):
    result = 0
    for first, last in pairs:
        first_int, last_int = int(first), int(last)
        # number of digits of first is even
        if len(first) % 2 == 0:
            half = get_half(first)
            if get_full(half) < first_int:
                half += 1
            while (full := get_full(half)) <= last_int:
                result += full
                half += 1
        # number of digits of first is odd -> jump to next even
        else:
            new_digits = len(first) + 1
            half = int('1' + ('0' * (new_digits // 2 - 1)))
            if get_full(half) > last_int:
                continue
            while (full := get_full(half)) <= last_int:
                result += full
                half += 1
    return result


def part2(pairs: list[list[str]]):
    result = set()
    for first, last in pairs:
        for num in range(int(first), int(last) + 1):
            s = str(num)
            for i in range(1, len(s) // 2 + 1):
                if s[:i] * (len(s) // i) == s:
                    result.add(num)
                    break
    return sum(result)


pairs = clean_text(text)
print("Solution 1: ", part1(pairs))
print("Solution 2: ", part2(pairs))
