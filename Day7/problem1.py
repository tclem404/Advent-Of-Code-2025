text_file = open("day7\\input.txt", "r")
lines = text_file.readlines()

beams = set()
beams.add(lines[0].find('S'))

splitCount = 0
for i in range(1, len(lines)):
    newBeams = set()

    for beam in beams:
        if lines[i][beam] == '^':
            splitCount += 1
            if beam > 0:
                newBeams.add(beam - 1)
            
            if beam < len(lines[0]) - 1:
                newBeams.add(beam + 1)
        else:
            newBeams.add(beam)
    
    beams = newBeams

print(splitCount)