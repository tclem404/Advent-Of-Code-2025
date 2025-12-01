import fileinput

inputArr = fileinput.input('day1\input.txt')

inputArr = [[s[0], int(s[1:])] for s in inputArr]
currPos = 50
countZero = 0
for dir, amount in inputArr:
    countZero += amount // 100
    amount %= 100
    if dir == "L":
        if (amount >= currPos and currPos != 0):
            countZero += 1
        currPos -= amount
    elif dir == "R":
        if (currPos + amount >= 100):
            countZero += 1
        currPos += amount

    currPos %= 100

print(countZero)