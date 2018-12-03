class Claim:
    def __init__(self, string):
        values = string.rstrip().lstrip().split(" ")
        id = values[0].replace("#", "")
        x, y = values[2].replace(":", "").split(",")
        width, height = values[3].split('x')
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

claims = []
with open("../input/day3input.txt", 'r') as inputFile:
    lines = inputFile.readlines()
    for line in lines:
        claims.append(Claim(line))

fabric = {}
for claim in claims:
    for x in range(claim.x, claim.x+claim.width):
        if x not in fabric:
            fabric[x] = {}
        for y in range(claim.y, claim.y+claim.height):
            if y not in fabric[x]:
                fabric[x][y] = []
            fabric[x][y].append(claim.id)

moreThanOne = 0
for x, row in fabric.items():
    for y, value in row.items():
        moreThanOne += 1 if len(value) > 1 else 0

print(moreThanOne)

for claim in claims:
    allForMe = True
    for x in range(claim.x, claim.x+claim.width):
        if not allForMe: break
        for y in range(claim.y, claim.y+claim.height):
            if not allForMe: break

            if len(fabric[x][y]) > 1 or fabric[x][y][0] != claim.id:
                allForMe = False
                break

    if allForMe:
        print(claim.id)
        break