file = open('input.txt', 'r')
text = file.read().strip()

known_conversions = {}


def add_to_dict(_dict, key, val):
    if key not in _dict:
        _dict[key] = val
    else:
        _dict[key] += val


def blink(counts_old):
    counts_new = counts_old.copy()
    for stone in counts_old:
        if stone == 0:
            # add 1s to our counts dict
            add_to_dict(counts_new, 1, counts_old[stone])
        elif len(str(stone)) % 2 == 0:
            # add stone's split to known conversions
            if stone not in known_conversions:
                mid = len(str(stone)) // 2
                first = int(str(stone)[:mid])
                second = int(str(stone)[mid:])
                known_conversions[stone] = (first, second)
            # get the split from our known splits
            first, second = known_conversions[stone]
            # add split values to our counts dict
            add_to_dict(counts_new, first, counts_old[stone])
            add_to_dict(counts_new, second, counts_old[stone])
        else:
            # add stone's changed value to known conversions
            if stone not in known_conversions:
                known_conversions[stone] = stone * 2024
            add_to_dict(counts_new, known_conversions[stone], counts_old[stone])
        counts_new[stone] -= counts_old[stone]
    counts_new = {k: v for k, v in counts_new.items() if v > 0}
    return counts_new


def blinker(stones, blinks):
    counts = {k: 1 for k in stones}
    for _ in range(blinks):
        counts = blink(counts)
    return sum(counts.values())


stones = [int(x) for x in text.split()]
print('Solution 1:', blinker(stones.copy(), 25))
print('Solution 2:', blinker(stones.copy(), 75))
