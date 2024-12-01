file = open("input.txt", "r")
text = file.read().strip()


#################### Part 1 ####################


def get_distances(
    lines: list[str],
    distances: list[list[float | int]],
    prev_x: int,
    prev_y: int,
    start_x: int,
    start_y: int,
):
    cur_x = start_x
    cur_y = start_y
    distance_from_start = 1
    while lines[cur_y][cur_x] != "S":
        distances[cur_y][cur_x] = min(distances[cur_y][cur_x], distance_from_start)

        if lines[cur_y][cur_x] == "|":
            if prev_y < cur_y:
                prev_y = cur_y
                cur_y += 1
            else:
                prev_y = cur_y
                cur_y -= 1
        elif lines[cur_y][cur_x] == "-":
            if prev_x < cur_x:
                prev_x = cur_x
                cur_x += 1
            else:
                prev_x = cur_x
                cur_x -= 1
        elif lines[cur_y][cur_x] == "L":
            if prev_y < cur_y:
                prev_y = cur_y
                cur_x += 1
            else:
                prev_x = cur_x
                cur_y -= 1
        elif lines[cur_y][cur_x] == "J":
            if prev_y < cur_y:
                prev_y = cur_y
                cur_x -= 1
            else:
                prev_x = cur_x
                cur_y -= 1
        elif lines[cur_y][cur_x] == "7":
            if prev_y > cur_y:
                prev_y = cur_y
                cur_x -= 1
            else:
                prev_x = cur_x
                cur_y += 1
        elif lines[cur_y][cur_x] == "F":
            if prev_y > cur_y:
                prev_y = cur_y
                cur_x += 1
            else:
                prev_x = cur_x
                cur_y += 1
        distance_from_start += 1
    return distances


def furthest_point(text: str):
    lines = text.splitlines()
    start_x = 0
    start_y = 0
    # Get starting index
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start_y = i
                start_x = j
                break

    distances: list[list[float | int]] = [
        [float("inf")] * len(lines[0]) for _ in range(len(lines))
    ]
    distances[start_y][start_x] = 0
    # Above S
    if start_y > 0 and lines[start_y - 1][start_x] in ["F", "|", "7"]:
        distances = get_distances(lines, distances, start_x, start_y, start_x, start_y - 1)
    # Right of S
    if start_x < len(lines[0]) and lines[start_y][start_x + 1] in ["J", "-", "7"]:
        distances = get_distances(lines, distances, start_x, start_y, start_x + 1, start_y)
    # Below S
    if start_y < len(lines) and lines[start_y + 1][start_x] in ["J", "|", "L"]:
        distances = get_distances(lines, distances, start_x, start_y, start_x, start_y + 1)
    # Left of S
    if start_x > 0 and lines[start_y][start_x - 1] in ["F", "-", "L"]:
        distances = get_distances(lines, distances, start_x, start_y, start_x - 1, start_y)

    # Get largest non inf value
    largest = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if distances[i][j] != float("inf"):
                largest = max(largest, distances[i][j])

    return distances, largest


distances, largest = furthest_point(text)
print("Solution 1: ", largest)

#################### Part 2 ####################


# For every point not in the pipe loop, check if it is inside a pipe loop
# by checking if it intersects the pipe loop an odd number of times.
def count_inside(text: str):
    lines = text.splitlines()
    walls = ["|", "L", "J"]
    total = 0
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            if distances[i][j] != float("inf"):
                continue
            idx = j
            inside = False
            while idx >= 0:
                if distances[i][idx] != float("inf") and line[idx] in walls:
                    inside = not inside
                idx -= 1
            if inside:
                total += 1
    return total


print("Solution 2: ", count_inside(text))
