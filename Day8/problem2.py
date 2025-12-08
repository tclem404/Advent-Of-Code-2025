text_file = open("day8\\input.txt", "r")
lines = text_file.readlines()

positions = [[int(_) for _ in line.split(',')] for line in lines]


def dist(x, y):
    return sum([(x[i] - y[i])**2 for i in range(len(x))])

distances = []
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        distances.append([dist(positions[i], positions[j]), i ,j])

groupings = [[i, 1] for i in range(len(positions))]

distances = sorted(distances, key = lambda x : x[0])

def getGroup(a):
    while groupings[a][0] != a:
        a = groupings[a][0]
    
    return a

ind = 0
seen = set()
while len(seen) < len(positions):
    [_, i, j] = distances[ind]
    a = getGroup(i)
    b = getGroup(j)
    ind += 1
    if (a == b):
        continue

    groupings[a][0] = b
    groupings[b][1] += groupings[a][1]
    if (groupings[b][1] == len(positions)):
        print(positions[i][0] * positions[j][0])
        break