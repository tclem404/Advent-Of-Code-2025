text_file = open("day6\\input.txt", "r")
lines = text_file.readlines()

operation = [[i, _] for [i, _] in enumerate(lines[-1]) if _ != ' ' and _ != '\n']

print(operation)

total = 0
for i in range(len(operation)):
    prod = 1

    # get matrix of numbers
    inputs = [list(line[operation[i][0]: operation[i + 1][0] - 1 if i + 1 < len(operation) else -1]) for line in lines[:-1]]

    # transpose list arr
    inputs = [list(row) for row in zip(*inputs)]

    # make numbers
    inputs = [int(''.join(num)) for num in inputs]

    # do operation
    for j in range(len(inputs)):
        if operation[i][1] == '+':
            total += inputs[j]
        elif operation[i][1] == '*':
            prod *= inputs[j]
    
    if operation[i][1] == '*':
        total += prod

print(total)