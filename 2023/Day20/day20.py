from copy import deepcopy
from math import lcm

file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()
modules: dict[str, dict] = {}


# modules = {name: (type, pulse, [destinations])}
def reset_modules():
    global modules
    modules = {}
    for line in lines:
        module = line.split("->")
        type = module[0][0] if module[0][0] in ["%", "&"] else ""
        name = module[0].strip(f" {type}")
        dests = [dest.strip() for dest in module[1].strip().split(",")]

        modules[name] = {"type": type, "pulse": 0, "dests": dests}

    # set pulses for conjunction
    for m1 in modules.items():
        if m1[1]["type"] == "&":
            m1[1]["pulse"] = {}
            for m2 in modules.items():
                if m1[0] in m2[1]["dests"]:
                    m1[1]["pulse"][m2[0]] = 0


#################### Part 1 ####################


def process_input(source: str, dest: str):
    if dest not in modules:
        return None
    if source == "button":
        return (dest, modules[dest]["dests"])

    if source == "broadcaster":
        modules[dest]["pulse"] = 0 if modules[dest]["pulse"] == 1 else 1
        return (dest, modules[dest]["dests"])

    # Flip the flip-flop
    elif modules[source]["type"] == "%" and modules[dest]["type"] == "%":
        if modules[source]["pulse"] == 0:
            modules[dest]["pulse"] = 0 if modules[dest]["pulse"] == 1 else 1
            return (dest, modules[dest]["dests"])
        else:
            return None

    # Add to configuration input memory
    elif modules[source]["type"] == "%" and modules[dest]["type"] == "&":
        modules[dest]["pulse"][source] = modules[source]["pulse"]
        return (dest, modules[dest]["dests"])

    # Conjunction
    elif modules[source]["type"] == "&" and modules[dest]["type"] == "%":
        if all(pulse == 1 for pulse in modules[source]["pulse"].values()):
            modules[dest]["pulse"] = 0 if modules[dest]["pulse"] == 1 else 1
            return (dest, modules[dest]["dests"])
        else:
            return None

    elif modules[source]["type"] == "&" and modules[dest]["type"] == "&":
        if all(pulse == 1 for pulse in modules[source]["pulse"].values()):
            modules[dest]["pulse"][source] = 0
        else:
            modules[dest]["pulse"][source] = 1
        return (dest, modules[dest]["dests"])


def push_button():
    # Push Button
    first_move = process_input("button", "broadcaster")
    moves = [first_move] if first_move else []
    low_pulses = 1
    high_pulses = 0
    while moves:
        next: list[tuple[str, list[str]]] = []
        for move in moves:
            source = move[0]
            for dest in move[1]:
                # add pulse to total
                if modules[source]["pulse"] == 0 or (
                    isinstance(modules[source]["pulse"], dict)
                    and all(value == 1 for value in modules[source]["pulse"].values())
                ):
                    low_pulses += 1
                else:
                    high_pulses += 1
                # make move
                next_move = process_input(source, dest)
                if next_move:
                    next.append(next_move)
        moves = deepcopy(next)
    return low_pulses, high_pulses


def num_pulses():
    reset_modules()
    tot_low_pulses = 0
    tot_high_pulses = 0
    i = 0
    while i < 1000:
        low_pulses, high_pulses = push_button()
        tot_low_pulses += low_pulses
        tot_high_pulses += high_pulses
        i += 1
    return int(tot_low_pulses * tot_high_pulses)


print("Solution 1: ", num_pulses())


#################### Part 2 ####################
# Output is rx which is fed by dr
# dr will feed a 0 to rx when all of its inputs are 1
# dr is fed by mp, qt, qb and ng
# If we find the amount of time it takes for mp, qt, qb and ng
# to become 1 we can take the lcm to find when dr will feed a 0 to rx
# Did this manually and found lcm


def fewest_num_pulses():
    reset_modules()
    tot_low_pulses = 0
    tot_high_pulses = 0

    i = 0
    while True:
        low_pulses, high_pulses = push_button()
        tot_low_pulses += low_pulses
        tot_high_pulses += high_pulses
        i += 1
        break

    return lcm(3917, 3919, 4007, 4027)


print("Solution 2: ", fewest_num_pulses())
