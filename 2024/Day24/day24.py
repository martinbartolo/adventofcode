file = open("input.txt", "r")
text = file.read().strip()


def clean_text(text):
    top, bottom = text.split("\n\n")

    values = {}
    all_ops = set()
    gates = {}

    for line in top.splitlines():
        op, val = line.strip().split()
        values[op[:-1]] = int(val)
        all_ops.add(op[:-1])

    for line in bottom.splitlines():
        op1, op, op2, arrow, out_op = line.strip().split()
        gates[out_op] = (op1, op, op2)
        all_ops.add(out_op)

    return values, gates, all_ops


def evaluate(op, values, gates):
    if op in values:
        return values[op]
    op1 = evaluate(gates[op][0], values, gates)
    op2 = evaluate(gates[op][2], values, gates)
    if gates[op][1] == "AND":
        return op1 & op2
    if gates[op][1] == "OR":
        return op1 | op2
    if gates[op][1] == "XOR":
        return op1 ^ op2


def part1(text):
    values, gates, all_ops = clean_text(text)
    digs = {}
    for op in all_ops:
        if op.startswith("z"):
            digs[int(op[1:])] = evaluate(op, values, gates)

    x = max([k for k in digs])
    num = 0
    for i in range(x, -1, -1):
        num = 2 * num + digs[i]
    return num


print('Solution 1:', part1(text))
