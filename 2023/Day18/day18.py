file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()


#################### Part 1 ####################


directions = [line.split()[0] for line in lines]
amounts = [int(line.split()[1]) for line in lines]


def trench_vol(directions: list[str], amounts: list[int]):
    row = 0
    col = 0
    vertices = [(0, 0)]
    dir_map = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
    for direction, amount in zip(directions, amounts):
        col += amount * dir_map[direction][0]
        row += amount * dir_map[direction][1]
        vertices.append((col, row))

    # Shoelace formula
    area = (
        abs(
            sum(
                vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]
                for i in range(len(vertices) - 1)
            )
        )
        / 2
    )

    # Pick's theorem
    boundary_points = sum(amounts)
    int_points = area + 1 - 0.5 * boundary_points
    return int(boundary_points + int_points)


print("Solution 1: ", trench_vol(directions, amounts))


#################### Part 2 ####################


hex_codes = [line.split()[2].strip("()") for line in lines]
dir_map = {0: "R", 1: "D", 2: "L", 3: "U"}
directions = [dir_map[int(hex_code[-1])] for hex_code in hex_codes]
amounts = [int(hex_code[1:-1], 16) for hex_code in hex_codes]
print("Solution 2: ", trench_vol(directions, amounts))
