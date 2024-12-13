import numpy as np

file = open('input.txt', 'r')
text = file.read().strip()


def clean_text(text):
    machines = text.split('\n\n')
    configs = []
    for machine in machines:
        lines = machine.splitlines()
        a1 = int(lines[0].split('X+')[1].split(',')[0])
        b1 = int(lines[1].split('X+')[1].split(',')[0])
        a2 = int(lines[0].split('Y+')[1])
        b2 = int(lines[1].split('Y+')[1])
        x = int(lines[2].split('X=')[1].split(',')[0])
        y = int(lines[2].split('Y=')[1].split(',')[0])
        configs.append((a1, b1, a2, b2, x, y))
    return configs


def calculate(configs, p):
    tokens = 0
    for a1, b1, a2, b2, x, y in configs:
        matrix = np.array([[a1, b1], [a2, b2]])
        constants = np.array([x, y]) + p
        a, b = np.round(np.linalg.solve(matrix, constants))  # round floating point errors
        if a * a1 + b * b1 == constants[0] and a * a2 + b * b2 == constants[1]:
            tokens += a * 3 + b
    return int(tokens)


configs = clean_text(text)
print('Solution 1:', calculate(configs, 0))
print('Solution 2:', calculate(configs, 10000000000000))
