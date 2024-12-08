from itertools import combinations

file = open('input.txt', 'r')
text = file.read().strip()


def part1(lines):
    dim = len(lines)

    # Get all antenna positions
    antennas = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == '.':
                continue
            if x in antennas:
                antennas[x].append((i, j))
            else:
                antennas[x] = [(i, j)]

    antinodes = set()
    for positions in antennas.values():
        for pair in combinations(positions, 2):
            # Calculate vector between antennas
            di = pair[1][0] - pair[0][0]
            dj = pair[1][1] - pair[0][1]

            # Calculate potential antinode positions
            antinode_1 = (pair[0][0] - di, pair[0][1] - dj)
            antinode_2 = (pair[1][0] + di, pair[1][1] + dj)

            # Check and add valid antinodes
            for antinode in (antinode_1, antinode_2):
                if 0 <= antinode[0] < dim and 0 <= antinode[1] < dim:
                    antinodes.add(antinode)
    return len(antinodes)


def part2(lines):
    dim = len(lines)

    # Get all antenna positions
    all_antennas = set()
    antennas = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == '.':
                continue
            if x in antennas:
                antennas[x].append((i, j))
            else:
                antennas[x] = [(i, j)]
            all_antennas.add((i, j))

    antinodes = set()
    for positions in antennas.values():
        for pair in combinations(positions, 2):
            # Calculate vector between antennas
            di = pair[1][0] - pair[0][0]
            dj = pair[1][1] - pair[0][1]

            # add antinodes in both directions until we go past boundary
            i = pair[0][0] - di
            j = pair[0][1] - dj
            while 0 <= i < dim and 0 <= j < dim:
                if (i, j) not in all_antennas:
                    antinodes.add((i, j))
                i -= di
                j -= dj

            i = pair[1][0] + di
            j = pair[1][1] + dj
            while 0 <= i < dim and 0 <= j < dim:
                if (i, j) not in all_antennas:
                    antinodes.add((i, j))
                i += di
                j += dj
    return len(antinodes) + len(all_antennas)


lines = text.splitlines()
print('Solution 1:', part1(lines))
print('Solution 2:', part2(lines))
