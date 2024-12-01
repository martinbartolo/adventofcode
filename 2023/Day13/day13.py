file = open("input.txt", "r")
text = file.read().strip()
patterns = [pattern.split() for pattern in text.split("\n\n")]


#################### Part 1 ####################


def rows_above_reflection(pattern: list[str]):
    rows_above = 1
    seen_stack: list[str] = []
    for i in range(len(pattern) - 1):
        seen_stack.append(pattern[i])
        if pattern[i] == pattern[i + 1]:
            for j in range(len(seen_stack) + 1):
                if i + j + 1 == len(pattern) or len(seen_stack) - j - 1 < 0:
                    return rows_above
                if seen_stack[len(seen_stack) - j - 1] != pattern[i + 1 + j]:
                    break
        rows_above += 1
    return -1


def notes_summary(patterns: list[list[str]]):
    total = 0
    for pattern in patterns:
        rows_above = rows_above_reflection(pattern)
        if rows_above == -1:
            total += rows_above_reflection(list(zip(*pattern)))
        else:
            total += 100 * rows_above
    return total


print("Solution 1: ", notes_summary(patterns))

#################### Part 2 ####################


# Find match with smudge
def match(s1: str, s2: str):
    mismatch = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if mismatch:
                return False
            else:
                mismatch = True
    return mismatch


def rows_above_reflection_smudge(pattern: list[str]):
    rows_above = 1
    seen_stack: list[str] = []
    for i in range(len(pattern) - 1):
        seen_stack.append(pattern[i])
        equal = pattern[i] == pattern[i + 1]
        smudge = match(pattern[i], pattern[i + 1])
        if equal or smudge:
            for j in range(len(seen_stack) + 1):
                if smudge:
                    if i + j + 1 == len(pattern) or len(seen_stack) - j - 1 < 0:
                        return rows_above
                    # once we see a smudge the rest must be equal
                    if seen_stack[len(seen_stack) - j - 1] != pattern[i + 1 + j] and not (
                        j == 0 and match(seen_stack[len(seen_stack) - j - 1], pattern[i + 1 + j])
                    ):
                        break
                elif equal:
                    if i + j + 1 == len(pattern) or len(seen_stack) - j - 1 < 0:
                        break
                    # we need at least one smudge
                    if match(seen_stack[len(seen_stack) - j - 1], pattern[i + 1 + j]):
                        smudge = True
        rows_above += 1
    return -1


def notes_summary_smudge(patterns: list[list[str]]):
    total = 0
    for pattern in patterns:
        rows_above = rows_above_reflection_smudge(pattern)
        if rows_above == -1:
            total += rows_above_reflection_smudge(list(zip(*pattern)))
        else:
            total += 100 * rows_above
    return total


print("Solution 2: ", notes_summary_smudge(patterns))
