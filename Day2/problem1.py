import fileinput

inputArr = fileinput.input('Day2\\input.txt')

inputArr =[[(l.split("-")[0]), (l.split("-")[1])] for l in inputArr.readline().split(",")]

count = 0
for min, max in inputArr:
    if len(min) % 2 == 0:
        start = int(min[:len(min) // 2])
        if start < int(min[len(min) // 2:]):
            start += 1
    else:
        start = 10**(len(min) // 2)
    
    if len(max) % 2 == 0:
        end = int(max[:len(max) // 2])
        if end > int(max[len(max) // 2:]):
            end -= 1
    else:
        end = 10**(len(max) // 2) - 1
    
    for i in range(start, end + 1):
        count += int(str(i) + str(i))

print(count)