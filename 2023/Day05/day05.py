from tqdm import tqdm

file = open("input.txt", "r")
text = file.read().strip()


#################### Part 1 ####################
def get_nums(section: str):
    return [
        [int(num) for num in nums_string.split()]
        for nums_string in section.split(":")[1].strip().splitlines()
    ]


def get_location(seed: int, maps: list[list[list[int]]]):
    for map in maps:
        for rule in map:
            if rule[1] <= seed < rule[1] + rule[2]:
                seed = rule[0] + seed - rule[1]
                break

    return seed


def lowest_location_number(text: str):
    sections = text.split("\n\n")

    seeds = [int(num) for num in sections[0].split(":")[1].strip().split()]
    maps = [get_nums(section) for section in sections[1:]]
    locations = [get_location(seed, maps) for seed in seeds]

    return min(locations)


print("Solution 1: ", lowest_location_number(text))


#################### Part 2 ####################
# Note: This is a brute force solution, and takes a long time to run.
# I did this by printing whenever a new lowest location was found.
# Every so often I came back to the terminal to see if a new lowest location had been found and checked if it was the solution.
# The solution was found midway through the 6th seed pair
def get_seeds(seed_pair: list[int]):
    seeds: list[int] = []
    for i in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
        seeds.append(i)
    return seeds


def lowest_location_number_2(text: str):
    sections = text.split("\n\n")

    maps = [get_nums(section) for section in sections[1:]]
    seed_ranges = [int(num) for num in sections[0].split(":")[1].strip().split()]
    seed_pairs = [seed_ranges[i : i + 2] for i in range(0, len(seed_ranges), 2)]

    min_location = float("inf")
    for i, seed_pair in enumerate(seed_pairs):
        print(f"\nSeed pair {i + 1} of {len(seed_pairs)}")
        seeds = get_seeds(seed_pair)
        for seed in tqdm(seeds, total=len(seeds)):
            location = get_location(seed, maps)
            if location < min_location:
                print(f"New lowest location: {location}")
                min_location = location
    return min_location


print("Solution 2: ", lowest_location_number_2(text))
