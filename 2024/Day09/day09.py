file = open('input.txt', 'r')
text = file.read().strip()


def part1(disk_map):
    # Create blocks
    blocks = []
    id = 0
    flag = True
    for x in disk_map:
        if flag:
            # Add file blocks with their ID
            blocks.extend([id] * int(x))
            id += 1
        else:
            # Add empty spaces
            blocks.extend(['.'] * int(x))
        flag = not flag

    # compress blocks
    i = 0
    j = len(blocks) - 1
    while i <= j:
        # move i until we reach a gap
        if blocks[i] != '.':
            i += 1
            continue
        # move j until we reach a block
        elif blocks[j] == '.':
            j -= 1
            continue
        # swap i and j
        else:
            blocks[i], blocks[j] = blocks[j], '.'

    # calculate checksum
    checksum = sum(i * id for i, id in enumerate(blocks) if id != '.')
    return checksum


def part2(disk_map):
    # Create blocks
    blocks = []
    id = 0
    flag = True
    for x in disk_map:
        if flag:
            # Add file blocks with their ID
            blocks.extend([id] * int(x))
            id += 1
        else:
            # Add empty spaces
            blocks.extend(['.'] * int(x))
        flag = not flag

    # get the file sizes
    file_sizes = {}
    for block_id in range(id):
        file_sizes[block_id] = blocks.count(block_id)

    # compress blocks
    for current_id in range(id - 1, -1, -1):
        file_size = file_sizes[current_id]
        # Find the file's start and end
        start = blocks.index(current_id)
        end = start + file_size

        # Find the leftmost span of free space that can fit the file
        for i in range(start):
            if blocks[i : i + file_size] == ['.'] * file_size:
                # Move the file
                blocks[i : i + file_size] = [current_id] * file_size
                blocks[start:end] = ['.'] * file_size
                break

    # calculate checksum
    checksum = sum(i * id for i, id in enumerate(blocks) if id != '.')
    return checksum


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
