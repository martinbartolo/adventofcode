from typing import Callable

file = open("input.txt", "r")
text = file.read().strip()

#################### Part 1 ####################

card_rank = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


# For us to be able to rank hand types we assign them as:
# Five of a kind  -> 6
# Four of a kind  -> 5
# Full house      -> 4
# Three of a kind -> 3
# Two pair        -> 2
# One pair        -> 1
# High card       -> 0
def get_hand_type(hand: list[int]):
    card_counts = dict.fromkeys(card_rank.values(), 0)
    for card in hand:
        card_counts[card] += 1

    counts = list(card_counts.values())
    if 5 in counts:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts:
        if 2 in counts:
            return 4
        else:
            return 3
    else:
        return counts.count(2)


def get_total_winnings(
    text: str, card_rank: dict[str, int], get_hand_type: Callable[[list[int]], int]
):
    lines = text.splitlines()
    hands = [[card_rank[card] for card in line.split()[0]] for line in lines]
    bets = [int(line.split()[1]) for line in lines]
    hand_types = [get_hand_type(hand) for hand in hands]

    total_winnings = 0
    current_rank = 1
    for type in range(7):
        hands_with_type = [hand for j, hand in enumerate(hands) if hand_types[j] == type]
        hands_with_type_sorted = sorted(
            hands_with_type, key=lambda x: (x[0], x[1], x[2], x[3], x[4])
        )
        for h in hands_with_type_sorted:
            total_winnings += current_rank * bets[hands.index(h)]
            current_rank += 1
    return total_winnings


print("Solution 1: ", get_total_winnings(text, card_rank, get_hand_type))

#################### Part 2 ####################

card_rank_2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_hand_type_2(hand: list[int]):
    card_counts = dict.fromkeys(card_rank_2.values(), 0)
    for card in hand:
        card_counts[card] += 1

    # Add points from jokers
    num_jokers = card_counts[1]
    card_counts[1] = 0
    counts = list(card_counts.values())
    max_count_index = counts.index(max(counts))
    for _ in range(num_jokers):
        counts[max_count_index] += 1

    if 5 in counts:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts:
        if 2 in counts:
            return 4
        else:
            return 3
    else:
        return counts.count(2)


print("Solution 2: ", get_total_winnings(text, card_rank_2, get_hand_type_2))
