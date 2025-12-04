import fileinput

inputArr = fileinput.input('Day3\\input.txt')

voltage = 0
for line in inputArr:
    line = line[:-1] # remove new line
    maxVal = max(int(i) for i in line)
    if line.count(str(maxVal))  > 1:
        voltage += maxVal * 11
    elif line[-1] == str(maxVal):
        voltage += max(int(i) for i in line[:-1]) * 10 + maxVal
    else:
        voltage += 10 * maxVal + max(int(i) for i in line[line.find(str(maxVal)) + 1:])

print(voltage)