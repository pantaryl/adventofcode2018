import sys

with open("../input/day11.txt", 'r') as inputFile:
    serialNumber = int(inputFile.read().rstrip())

grid = [[int("{:016d}".format((((x+10)*y)+serialNumber)*(x+10))[-3]) - 5 for x in range(1, 301)] for y in range(1, 301)]

scores = {}

def findMaxSumSquare(size):
    sums = []
    for y in range(len(grid)):
        sums.append([])
        for x in range(len(grid)):
            sums[-1].append(0)

    sums[0][0] = grid[0][0]
    for x in range(1, len(grid)):
        sums[0][x] = grid[0][x] + sums[0][x-1]
    for y in range(1, len(grid)):
        sums[y][0] = grid[y][0] + sums[y-1][0]

    for y in range(1, len(grid)):
        for x in range(1, len(grid)):
            sums[y][x] = grid[y][x] + sums[y-1][x] + sums[y][x-1] - sums[y-1][x-1]

    maxSize = -sys.maxsize
    coord   = (0, 0)
    for y in range(0, len(grid)-size+1):
        for x in range(0, len(grid)-size+1):
            mySum = sums[y][x]

            if y - size >= 0:
                mySum -= sums[y-size][x]
            if x - size >= 0:
                mySum -= sums[y][x-size]
            if y - size >= 0 and x - size >= 0:
                mySum += sums[y-size][x-size]

            if mySum > maxSize:
                maxSize = mySum
                # 'coord - size + 1' accounts for the position in the upper left
                # The additional +1 accounts for the zero-based coordinates I am using.
                coord   = (x-size+1+1, y-size+1+1)

    return coord, maxSize

# Part 1
print("Part 1: {:d},{:d}".format(*findMaxSumSquare(3)[0]))

# Part 2
scores = {}
for size in range(1, 301):
    print('\r{:5.2f}% complete.'.format((size / 300) * 100.0), end='')
    coord, val = findMaxSumSquare(size)
    scores[size] = (coord, val)

sortedVal = sorted(scores.keys(), key=lambda x: scores[x][1])
winner = sortedVal[-1]
print("\rPart 2: {:d},{:d},{:d}".format(scores[winner][0][0], scores[winner][0][1], winner))