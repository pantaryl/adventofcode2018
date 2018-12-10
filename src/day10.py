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
prevPlotX = None
prevPlotY = None

while True:
    plotX = []
    plotY = []
    for coord in coordData:
        plotX.append(coord[0] + (counter * coord[2]))
        yCoord = coord[1] + (counter * coord[3])
        plotY.append(yCoord)

    if abs(max(plotY) - min(plotY)) < lastSize:
        lastSize = abs(max(plotY) - min(plotY))
        prevPlotX = plotX
        prevPlotY = plotY
        counter += 1
        continue

    minY = min(prevPlotY)
    minX = min(prevPlotX)
    yLen = abs(max(prevPlotY) - minY) + 1
    xLen = abs(max(prevPlotX) - minX) + 1
    rows = [['.' for x in range(xLen)] for y in range(yLen)]
    for i in range(len(prevPlotY)):
        rows[prevPlotY[i]-minY][prevPlotX[i]-minX] = "#"

    # Part 1
    print("Part 1: ")
    for i in range(yLen - 1, -1, -1):
        print("".join(rows[i]))

    print()

    # Part 2
    print("Part 2: " + str(counter - 1))
    break