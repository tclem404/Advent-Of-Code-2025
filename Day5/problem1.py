text_file = open("day5\\input.txt", "r")
lines = text_file.readlines()

breakline = lines.index("\n")
ranges = [[int(entry) for entry in l[:-1].split('-')] for l in lines[:breakline]]

ingredients = [int(l[:-1]) for l in lines[breakline + 1:-1]]

def comp(listA):
    return listA[0]

ranges = sorted(ranges, key = comp)

ingredients = sorted(ingredients)

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

i = 0
fresh = 0
for ing in ingredients:
    if i >= len(ranges):
        break

    while i < len(ranges) and ranges[i][1] < ing:
        i += 1

    if i < len(ranges) and ranges[i][0] <= ing:
        fresh += 1

print(fresh)