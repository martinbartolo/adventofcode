file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()
bricks = [
    (tuple(int(x) for x in brick[0].split(",")), tuple(int(x) for x in brick[1].split(",")))
    for brick in [line.split("~") for line in lines]
]
# sort bricks by left z coordinate
bricks = sorted(bricks, key=lambda brick: brick[0][2])

#################### Part 1 ####################


def drop_bricks(bricks):
    new_bricks = []
    for brick in bricks:
        resting_brick = None
        for brick2 in new_bricks:
            # check if brick can rest on brick2
            if (
                brick[0][0] <= brick2[1][0]
                and brick[1][0] >= brick2[0][0]
                and brick[0][1] <= brick2[1][1]
                and brick[1][1] >= brick2[0][1]
                and brick[0][2] >= brick2[1][2]
            ):
                # check if it is the highest brick that can be rested on
                if resting_brick is None or resting_brick[1][2] < brick2[1][2]:
                    resting_brick = brick2

        if resting_brick == None:
            # if no brick can be rested on, brick falls to the ground
            new_brick = (
                (brick[0][0], brick[0][1], 1),
                (brick[1][0], brick[1][1], brick[1][2] - brick[0][2] + 1),
            )
        else:
            # if a brick to rest on is found, brick rests on top of it
            new_brick = (
                (brick[0][0], brick[0][1], resting_brick[1][2] + 1),
                (brick[1][0], brick[1][1], resting_brick[1][2] + 1 + brick[1][2] - brick[0][2]),
            )
        new_bricks.append(new_brick)
    return new_bricks


def safe_to_disintegrate(bricks):
    safe_bricks = []
    for i, brick in enumerate(bricks):
        safe_to_disintegrate = True
        for j in range(i + 1, len(bricks)):  # only check bricks above
            brick2 = bricks[j]
            # check if brick2 is resting on brick
            if (
                brick != brick2
                and brick[0][0] <= brick2[1][0]
                and brick[1][0] >= brick2[0][0]
                and brick[0][1] <= brick2[1][1]
                and brick[1][1] >= brick2[0][1]
                and brick[1][2] + 1 == brick2[0][2]
            ):
                # check if there is another brick that can support brick2
                supported = False
                for brick3 in bricks:
                    if (
                        brick3 != brick
                        and brick3 != brick2
                        and brick3[0][0] <= brick2[1][0]
                        and brick3[1][0] >= brick2[0][0]
                        and brick3[0][1] <= brick2[1][1]
                        and brick3[1][1] >= brick2[0][1]
                        and brick3[1][2] + 1 == brick2[0][2]
                    ):
                        supported = True
                        break
                if not supported:
                    safe_to_disintegrate = False
                    break
        if safe_to_disintegrate:
            safe_bricks.append(brick)
    return safe_bricks


print("Solution 1: ", len(safe_to_disintegrate(drop_bricks(bricks))))


#################### Part 2 ####################


def count_falling_bricks(bricks):
    safe_bricks = safe_to_disintegrate(bricks)
    count = 0
    # disintegrate bricks one by one
    for i, brick in enumerate(bricks):
        # skip bricks that are safe to disintegrate
        if brick in safe_bricks:
            continue
        # remove brick from list
        new_bricks = bricks[:i] + bricks[i + 1 :]
        # drop bricks
        dropped_bricks = drop_bricks(new_bricks)
        # count bricks that have fallen
        count += sum(a != b for a, b in zip(new_bricks, dropped_bricks))
    return count


print("Solution 2: ", count_falling_bricks(drop_bricks(bricks)))
