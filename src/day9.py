with open("../input/day9.txt", 'r') as inputFile:
    data = inputFile.read()

import re
values = re.findall(r'\d+', data)

class Node():
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

    def __repr__(self):
        return str("{} {} {}".format(self.prev.id, self.id, self.next.id))

def getScore(NumPlayers, MaxMarble):
    nodes = {}
    nodes[0] = Node(0)
    nodes[1] = Node(1)
    nodes[0].prev = nodes[1]
    nodes[0].next = nodes[1]
    nodes[1].prev = nodes[0]
    nodes[1].next = nodes[0]

    currentPlayer = 1
    currentMarble = 1
    nextMarble    = 2

    scores = [0] * NumPlayers

    while currentMarble <= MaxMarble:
        if (nextMarble % 23) == 0:
            scores[currentPlayer] += nextMarble

            idx = currentMarble
            for i in range(7):
                idx = nodes[idx].prev.id

            toRemove = nodes[idx]
            scores[currentPlayer] += toRemove.id
            nodes[toRemove.prev.id].next = nodes[toRemove.next.id]
            nodes[toRemove.next.id].prev = nodes[toRemove.prev.id]

            nodes.pop(toRemove.id)
            currentMarble = toRemove.next.id
        else:
            newNode = Node(nextMarble)
            nodes[nextMarble] = newNode

            marble  = nodes[currentMarble].next
            afterMarble = marble.next
            marble.next = newNode
            afterMarble.prev = newNode
            newNode.prev = marble
            newNode.next = afterMarble
            currentMarble = nextMarble
        currentPlayer = (currentPlayer + 1) % NumPlayers
        nextMarble += 1

    return max(scores)

from timeit import default_timer as timer

# Part 1
start = timer()
print(getScore(int(values[0]), int(values[1])))
end = timer()
print("Part 1 Time (s): {:}".format(end - start))

# Part 2
start = timer()
print(getScore(int(values[0]), int(values[1]) * 100))
end = timer()
print("Part 2 Time (s): {:}".format(end - start))

