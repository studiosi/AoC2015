program = [l.strip() for l in open("input.txt").readlines()]

# Part 1
registers = { "a" : 0, "b" : 0 }
pc = 0
while pc < len(program):
    code = program[pc]
    x = code.split()
    if x[0] == "hlf":
        registers[x[1]] = registers[x[1]] // 2
        pc += 1
    elif x[0] == "tpl":
        registers[x[1]] = registers[x[1]] * 3
        pc += 1
    elif x[0] == "inc":
        registers[x[1]] = registers[x[1]] + 1
        pc += 1
    elif x[0] == "jmp":
        pc += int(x[1])
    elif x[0] == "jie":
        reg = x[1].replace(",",  "")
        if registers[reg] % 2 == 0:
            pc += int(x[2])
        else:
            pc += 1
    elif x[0] == "jio":
        reg = x[1].replace(",",  "")
        if registers[reg] == 1:
            pc += int(x[2])
        else:
            pc += 1
print(registers)

# Part 2
registers = { "a" : 1, "b" : 0 }
pc = 0
while pc < len(program):
    code = program[pc]
    x = code.split()
    if x[0] == "hlf":
        registers[x[1]] = registers[x[1]] // 2
        pc += 1
    elif x[0] == "tpl":
        registers[x[1]] = registers[x[1]] * 3
        pc += 1
    elif x[0] == "inc":
        registers[x[1]] = registers[x[1]] + 1
        pc += 1
    elif x[0] == "jmp":
        pc += int(x[1])
    elif x[0] == "jie":
        reg = x[1].replace(",",  "")
        if registers[reg] % 2 == 0:
            pc += int(x[2])
        else:
            pc += 1
    elif x[0] == "jio":
        reg = x[1].replace(",",  "")
        if registers[reg] == 1:
            pc += int(x[2])
        else:
            pc += 1
print(registers)
