import fileinput

inputArr = fileinput.input('Day2\\input.txt')

ranges =[[int(l.split("-")[0]), int(l.split("-")[1])] for l in inputArr.readline().split(",")]

def comp(listA):
    return listA[0]

ranges = sorted(ranges, key = comp)

currComp = 1
i = 0
while currComp < len(ranges):
    while currComp < len(ranges) and ranges[currComp][0] <= ranges[i][1]:
        ranges[i][1] = max(ranges[i][1], ranges[currComp][1])
        currComp += 1
    
    if currComp >= len(ranges):
        break
    ranges[i + 1] = ranges[currComp]
    i += 1
    currComp += 1

ranges = ranges[:i+1]

seen = set()
repeats = 2
total = 0
while int("1"*repeats) < ranges[-1][1]:
    ind = 0
    currNum = 1
    while ind < len(ranges):
        currGuess = int(str(currNum) * repeats)
        while ind < len(ranges) and currGuess > ranges[ind][1]:
            ind += 1

        if ind >= len(ranges):
            break

        if currGuess >= ranges[ind][0] and currGuess not in seen:
            seen.add(currGuess)
            total += currGuess

        currNum += 1
    
    repeats += 1

print(total)