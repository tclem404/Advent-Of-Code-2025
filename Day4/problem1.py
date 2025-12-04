import fileinput

inputArr = fileinput.input('Day4\\input.txt')
grid = [list(line[:-1]) for line in inputArr]

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
                
                neighbors += (1 if grid[i + iDiff][j + jDiff] == '@' else 0)
        
        removable += (1 if neighbors < 4 else 0)

print(removable)