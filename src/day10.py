import re, sys

Visualize      = False
IterationCount = 100

with open("../input/day10.txt", 'r') as inputFile:
    data = inputFile.readlines()

coordData = []
for line in data:
    values = re.findall(r'(-?\d+)', line)
    coordData.append((int(values[0]), -1*int(values[1]), int(values[2]), -1*int(values[3])))

counter  = 0
lastSize = sys.maxsize
prevPlots = None

while True:
    plots = [(coord[0] + (counter * coord[2]), coord[1] + (counter * coord[3])) for coord in coordData]

    maxY = max(plots, key=lambda x:x[1])[1]
    minY = min(plots, key=lambda x:x[1])[1]
    size = abs(maxY - minY)
    if size < lastSize:
        lastSize  = size
        prevPlots = plots
        counter += 1
        continue

    minY = min(prevPlots, key=lambda x:x[1])[1]
    maxY = max(prevPlots, key=lambda x:x[1])[1]
    minX = min(prevPlots, key=lambda x:x[0])[0]
    maxX = max(prevPlots, key=lambda x:x[0])[0]
    yLen = abs(maxY - minY) + 1
    xLen = abs(maxX - minX) + 1
    rows = [['.' for x in range(xLen)] for y in range(yLen)]
    for i in range(len(prevPlots)):
        rows[prevPlots[i][1]-minY][prevPlots[i][0]-minX] = "#"

    # Part 1
    print("Part 1: ")
    for i in range(yLen - 1, -1, -1):
        print("".join(rows[i]))

    print()

    # Part 2
    print("Part 2: " + str(counter - 1))
    break