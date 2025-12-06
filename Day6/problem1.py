text_file = open("day6\\input.txt", "r")
lines = text_file.readlines()

inputs = [[int(entry) for entry in line.split(' ') if entry != '' and entry != '\n'] for line in lines[:-1]]

operation = [_ for _ in lines[-1].split(' ') if _ != '' and _ != '\n']

print(inputs, operation)

total = 0
for i in range(len(operation)):
    prod = 1
    for j in range(len(inputs)):
        if operation[i] == '+':
            total += inputs[j][i]
        elif operation[i] == '*':
            prod *= inputs[j][i]
    
    if operation[i] == '*':
        total += prod

print(total)