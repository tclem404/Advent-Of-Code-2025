import fileinput

inputArr = fileinput.input('day1\input.txt')

inputArr = [[s[0], int(s[1:])] for s in inputArr]
currPos = 50
countZero = 0
for dir, amount in inputArr:
    if dir == "L":
        currPos -= amount
    elif dir == "R":
        currPos += amount

    currPos %= 100
    countZero += int(currPos == 0)

print(countZero)