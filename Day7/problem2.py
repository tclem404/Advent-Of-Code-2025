import functools

text_file = open("day7\\input.txt", "r")
lines = text_file.readlines()

@functools.lru_cache
def possibilities(i, j):
    if i >= len(lines):
        return 1

    if lines[i][j] == '^':
        outcomes = 0
        if j > 0:
            outcomes += possibilities(i + 1, j - 1)
        
        if j < len(lines[0]) - 1:
            outcomes += possibilities(i + 1, j + 1)
        
        return outcomes
    else:
        return possibilities(i + 1, j)

print(possibilities(0, lines[0].find('S')))