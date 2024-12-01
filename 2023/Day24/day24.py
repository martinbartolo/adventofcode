import numpy as np
from sympy import Symbol, solve_poly_system

file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()
parts = [line.split(" @ ") for line in lines]
points = [[int(num) for num in part[0].split(", ")] for part in parts]
velocities = [[int(num) for num in part[1].split(", ")] for part in parts]


#################### Part 1 ####################


def part1(min, max):
    count = 0
    for i, pv in enumerate(zip(points, velocities)):
        p1 = pv[0]
        v1 = pv[1]
        m1 = v1[1] / v1[0]
        b1 = p1[1] - m1 * p1[0]
        for p2, v2 in zip(points[i + 1 :], velocities[i + 1 :]):
            m2 = v2[1] / v2[0]
            b2 = p2[1] - m2 * p2[0]
            # now we have 2 lines m1x1 + y1 + b1 = 0 and m2x2 + y2 + b2 = 0
            # which we can solve to get the point of intersection
            denom = m1 - m2
            if denom == 0:
                # lines are parallel
                continue
            pix = (b2 - b1) / denom
            piy = m1 * pix + b1
            # check if intersection is in the future
            if (
                (
                    (v1[0] > 0 and pix > p1[0])
                    or (v1[0] < 0 and pix < p1[0])
                    or (v1[0] == 0 and pix == p1[0])
                )
                and (
                    (v2[0] > 0 and pix > p2[0])
                    or (v2[0] < 0 and pix < p2[0])
                    or (v2[0] == 0 and pix == p2[0])
                )
                and (
                    (v1[1] > 0 and piy > p1[1])
                    or (v1[1] < 0 and piy < p1[1])
                    or (v1[1] == 0 and piy == p1[1])
                )
                and (
                    (v2[1] > 0 and piy > p2[1])
                    or (v2[1] < 0 and piy < p2[1])
                    or (v2[1] == 0 and piy == p2[1])
                )
            ):
                # check if the point of intersection is in the test area
                if min <= pix <= max and min <= piy <= max:
                    count += 1
    return count


print("Solution 1: ", part1(200000000000000, 400000000000000))

#################### Part 2 ####################
# Solution from https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kepmry2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def part2():
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    vx = Symbol("vx")
    vy = Symbol("vy")
    vz = Symbol("vz")

    equations = []
    t_syms = []

    # once you have three shards to intersect, there's only one valid line
    # so we don't have to set up a huge system of equations that would take forever to solve. Just pick the first three.
    for i in range(3):
        # vx is the velocity of our throw, xv is the velocity of the shard we're trying to hit. Yes, this is a confusing naming convention.
        x0, y0, z0 = points[i]
        xv, yv, zv = velocities[i]
        t = Symbol(
            "t" + str(i)
        )  # remember that each intersection will have a different time, so it needs its own variable

        # (x + vx*t) is the x-coordinate of our throw, (x0 + xv*t) is the x-coordinate of the shard we're trying to hit.
        # set these equal, and subtract to get x + vx*t - x0 - xv*t = 0
        # similarly for y and z
        eqx = x + vx * t - x0 - xv * t
        eqy = y + vy * t - y0 - yv * t
        eqz = z + vz * t - z0 - zv * t

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_syms.append(t)

    result = solve_poly_system(equations, *([x, y, z, vx, vy, vz] + t_syms))
    return result[0][0] + result[0][1] + result[0][2]


print("Solution 2: ", part2())
