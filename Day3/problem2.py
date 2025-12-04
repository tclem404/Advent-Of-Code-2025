import fileinput

inputArr = fileinput.input('Day4\\input.txt')

def largestJoltage(inStr, digits):
    if digits == 0:
        return 0
    
    print(inStr, digits)
    digit = max([int(i) for i in inStr[:(-(digits-1) if digits > 1 else len(inStr))]])
    return digit * 10**(digits-1) + largestJoltage(inStr[inStr.find(str(digit)) + 1:], digits - 1)

voltage = 0
for line in inputArr:
    line = line[:-1] # remove new line
    voltage += largestJoltage(line, 12)

print(voltage)