text_file = open("day8\\input.txt", "r")
lines = text_file.readlines()

positions = [[int(_) for _ in line.split(',')] for line in lines]


def dist(x, y):
    return sum([(x[i] - y[i])**2 for i in range(len(x))])

distances = []
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        distances.append([dist(positions[i], positions[j]), i ,j])

groupings = [i for i in range(len(positions))]

distances = sorted(distances, key = lambda x : x[0])

def getGroup(a):
    while groupings[a] != a:
        a = groupings[a]
    
    return a

for ind in range(1000):
    [_, i, j] = distances[ind]
    a = getGroup(i)
    b = getGroup(j)
    groupings[a] = b

groups = {}
for i in range(len(positions)):
    group = getGroup(i)
    if group in groups:
        groups[group] += 1
    else:
        groups[group] = 1

groups = [groups[key] for key in groups.keys()]
groups = sorted(groups)

print(groups[-1] * groups[-2] * groups[-3])