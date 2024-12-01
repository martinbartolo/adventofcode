file = open("day-04.txt", "r")
text = file.read()


#################### Part 1 ####################
def sum_points(text: str):
    cards = [line.split(":")[1].strip() for line in text.splitlines()]
    split_cards = [card.split("|") for card in cards]
    winners = [[int(num) for num in split_card[0].strip().split()] for split_card in split_cards]
    numbers = [[int(num) for num in split_card[1].strip().split()] for split_card in split_cards]

    points_total = 0
    for i in range(len(winners)):
        points = 0
        matches = [num for num in numbers[i] if num in winners[i]]
        for _ in matches:
            if points == 0:
                points = 1
            else:
                points *= 2
        points_total += points

    return points_total


#################### Part 2 ####################
def count_scratchcards(text: str):
    cards = [line.split(":")[1].strip() for line in text.splitlines()]
    split_cards = [card.split("|") for card in cards]
    winners = [[int(num) for num in split_card[0].strip().split()] for split_card in split_cards]
    numbers = [[int(num) for num in split_card[1].strip().split()] for split_card in split_cards]

    card_counts = [1] * len(winners)
    for i in range(len(winners)):
        for _ in range(card_counts[i]):
            matches = [num for num in numbers[i] if num in winners[i]]
            for j in range(len(matches)):
                card_counts[i + j + 1] += 1

    return sum(card_counts)


print("Solution 1: ", sum_points(text))
print("Solution 2: ", count_scratchcards(text))
