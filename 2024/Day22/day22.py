file = open('input.txt', 'r')
text = file.read().strip()


def get_next_secret(secret: int):
    secret = (secret * 64 ^ secret) % 16777216
    secret = (secret // 32 ^ secret) % 16777216
    secret = (secret * 2048 ^ secret) % 16777216
    return secret


def part1(text: str):
    initial_secrets = [int(x) for x in text.splitlines()]
    final_secrets = []
    for secret in initial_secrets:
        for _ in range(2000):
            secret = get_next_secret(secret)
        final_secrets.append(secret)
    return sum(final_secrets)


def part2(text: str):
    initial_secrets = [int(x) for x in text.splitlines()]

    all_bananas = {}
    for secret in initial_secrets:
        # calculate all prices and price changes for the buyer
        bananas = {}
        prices = [int(str(secret)[-1])]
        price_changes = []
        for _ in range(2000):
            secret = get_next_secret(secret)
            prices.append(int(str(secret)[-1]))
            price_changes.append(prices[-1] - prices[-2])

        # find bananas for each sequence
        for i in range(len(price_changes) - 3):
            window = str(price_changes[i : i + 4])
            if window not in bananas:
                bananas[window] = prices[i + 4]

        # combine bananas dict into main all_bananas dict
        for window, price in bananas.items():
            if window not in all_bananas:
                all_bananas[window] = price
            else:
                all_bananas[window] += price
    return max(all_bananas.values())


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
