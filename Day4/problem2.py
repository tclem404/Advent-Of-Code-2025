import fileinput

inputArr = fileinput.input('Day4\\input.txt')
grid = [list(line[:-1]) for line in inputArr]

# make it s.t. each entry is number of neighboring rolls
removable = 0
for i, row in enumerate(grid):
    for j, elem in enumerate(row):
        if elem != '@':
            continue

        neighbors = 0
        iDiffs = [0]
        if i != 0:
            iDiffs.append(-1)
        if i != len(grid) - 1:
            iDiffs.append(1)

        jDiffs = [0]
        if j != 0:
            jDiffs.append(-1)
        if j != len(row) - 1:
            jDiffs.append(1)

        for iDiff in iDiffs:
            for jDiff in jDiffs:
                if iDiff == 0 and jDiff == 0:
                    continue
                
                neighbors += (1 if grid[i + iDiff][j + jDiff] != '.' else 0)
        
        grid[i][j] = neighbors

def removeEntry(i,j):
    removed = 1
    grid[i][j] = '.'

    iDiffs = [0]
    if i != 0:
        iDiffs.append(-1)
    if i != len(grid) - 1:
        iDiffs.append(1)

    jDiffs = [0]
    if j != 0:
        jDiffs.append(-1)
    if j != len(row) - 1:
        jDiffs.append(1)

    for iDiff in iDiffs:
        for jDiff in jDiffs:
            if grid[i + iDiff][j + jDiff] != '.':
                grid[i + iDiff][j + jDiff] -= 1
                if grid[i + iDiff][j + jDiff] < 4:
                    removed += removeEntry(i + iDiff, j + jDiff)
    
    return removed

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.' and grid[i][j] < 4:
            removable += removeEntry(i,j)

print(removable)