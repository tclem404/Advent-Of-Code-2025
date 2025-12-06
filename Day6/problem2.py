text_file = open("day6\\input.txt", "r")
lines = text_file.readlines()

operation = [[i, _] for [i, _] in enumerate(lines[-1]) if _ != ' ' and _ != '\n']

print(operation)

total = 0
for i in range(len(operation)):
    prod = 1

    inputs = [list(line[operation[i][0]: operation[i + 1][0] - 1 if i + 1 < len(operation) else -1]) for line in lines[:-1]]

    # transpose
    inputs = [list(row) for row in zip(*inputs)]

    inputs = [int(''.join(num)) for num in inputs]

    print(inputs)

    for j in range(len(inputs)):
        if operation[i][1] == '+':
            total += inputs[j]
        elif operation[i][1] == '*':
            prod *= inputs[j]
    
    if operation[i][1] == '*':
        total += prod

print(total)