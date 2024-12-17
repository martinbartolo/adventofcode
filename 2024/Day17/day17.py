file = open('input.txt', 'r')
text = file.read().strip()


def clean_text(text: str):
    registers, program = text.split('\n\n')

    registers = registers.splitlines()
    a = int(registers[0].split('Register A: ')[1])
    b = int(registers[1].split('Register B: ')[1])
    c = int(registers[2].split('Register C: ')[1])
    program = [int(x) for x in program.split('Program: ')[1].split(',')]

    return a, b, c, program


def part1(a: int, b: int, c: int, program: list[int]):
    output = []
    i = 0
    while i < len(program):
        opcode, operand = program[i], program[i + 1]
        combo = None

        if operand == 4:
            combo = a
        elif operand == 5:
            combo = b
        elif operand == 6:
            combo = c
        else:
            combo = operand

        if opcode == 0:
            a //= 2**combo
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            b = a // 2**combo
        else:
            c = a // 2**combo

        i += 2

    return ','.join(map(str, output))


def part2(b: int, c: int, program: list[int]):
    a = 1569800000570882
    prev = 0
    while True:
        # print(a)
        output = part1(a, b, c, program)
        output_values = [int(x) for x in output.split(',')]
        # print(len(output_values), len(program))
        if all(output_values[i] == program[i] for i in range(6)):
            print(a, len(output_values), a - prev, output_values, program)
            prev = a
        if output_values == program:
            print(a)
            break
        # if len(output_values) < 16:
        #     print(a)
        #     a *= 2

        a += 1

    return None


a, b, c, program = clean_text(text)
print('Solution 1:', part1(a, b, c, program))
print('Solution 2:', part2(b, c, program))
