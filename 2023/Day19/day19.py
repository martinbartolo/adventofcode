file = open("input.txt", "r")
text = file.read().strip()
rules = dict(
    [
        (rule[0], rule[1].split(","))
        for rule in [line.strip("}").split("{") for line in text.split("\n\n")[0].splitlines()]
    ]
)
parts = [
    {item.split("=")[0]: int(item.split("=")[1]) for item in part}
    for part in [line.strip("{}").split(",") for line in text.split("\n\n")[1].splitlines()]
]


#################### Part 1 ####################


def get_next_rule(next_rule_label, part):
    rule = rules[next_rule_label]
    for r in rule:
        if ":" in r:
            test = r.split(":")[0]
            label = r.split(":")[1]
            if "<" in test:
                cat_name = test.split("<")[0]
                cat_val = int(test.split("<")[1])
                if part[cat_name] < cat_val:
                    return label
            elif ">" in test:
                cat_name = test.split(">")[0]
                cat_val = int(test.split(">")[1])
                if part[cat_name] > cat_val:
                    return label
        else:
            return r


def sum_accepted(parts: list[dict[str, int]]):
    total = 0
    for part in parts:
        next_rule_label = "in"
        while True:
            next_rule_label = get_next_rule(next_rule_label, part)
            if next_rule_label == "A":
                total += sum(list(part.values()))
                break
            elif next_rule_label == "R":
                break
    return total


print("Solution 1: ", sum_accepted(parts))

#################### Part 2 ####################
# CHEATED - Code from https://www.reddit.com/r/adventofcode/comments/18ltr8m/comment/ke010be/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def both(category: str, is_gt: bool, val: int, ranges):
    ch_index = "xmas".index(category)
    ranges2 = []
    for range in ranges:
        range = list(range)
        lo, hi = range[ch_index]
        if is_gt:
            lo = max(lo, val + 1)
        else:
            hi = min(hi, val - 1)
        if lo > hi:
            continue
        range[ch_index] = (lo, hi)
        ranges2.append(tuple(range))
    return ranges2


def acceptance_ranges_outer(rule_label: str):
    return acceptance_ranges_inner(rules[rule_label])


def acceptance_ranges_inner(rule: list[str]):
    r = rule[0]
    if r == "R":
        return []
    if r == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    if ":" not in r:
        return acceptance_ranges_outer(r)
    condition = r.split(":")[0]
    is_gt = ">" in condition
    category = condition[0]
    val = int(condition[2:])
    val_inverted = val + 1 if is_gt else val - 1
    cond_true = both(category, is_gt, val, acceptance_ranges_inner([r.split(":")[1]]))
    cond_false = both(category, not is_gt, val_inverted, acceptance_ranges_inner(rule[1:]))
    return cond_true + cond_false


def sum_combinations():
    total = 0
    for rng in acceptance_ranges_outer("in"):
        v = 1
        for lo, hi in rng:
            v *= hi - lo + 1
        total += v
    return total


print("Solution 2: ", sum_combinations())
