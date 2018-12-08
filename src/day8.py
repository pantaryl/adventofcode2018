import sys
with open("../input/day8.txt", 'r') as inputFile:
    data = inputFile.read()
data = data.split(" ")

# Part 1
def parseChild(myList):
    mySum = 0
    numChildren = int(myList.pop(0))
    numMetadata = int(myList.pop(0))

    if numChildren > 0:
        for i in range(numChildren):
            addedmySum, newList = parseChild(myList)
            mySum += addedmySum
            myList = newList
    for i in range(numMetadata):
        value = int(myList.pop(0))
        mySum += value
    return mySum, myList

part1Sum, _ = parseChild(data.copy())
print(part1Sum)


# Part 2
class Node():
    def __init__(self):
        self.children = []
        self.metadata = []

def parseChild2(myList, parent):
    newNode = Node()
    if parent is not None:
        parent.children.append(newNode)

    numChildren = int(myList.pop(0))
    numMetadata = int(myList.pop(0))

    if numChildren > 0:
        for i in range(numChildren):
            myList, _ = parseChild2(myList, newNode)
    for i in range(numMetadata):
        value = int(myList.pop(0))
        newNode.metadata.append(value)
    return myList, newNode

def traverseTree(node):
    mySum = 0
    if len(node.children) > 0:
        for i in range(len(node.metadata)):
            childIdx = node.metadata[i] - 1
            if childIdx < len(node.children):
                mySum += traverseTree(node.children[childIdx])
    else:
        mySum += sum(node.metadata)
    return mySum

_, root = parseChild2(data.copy(), None)
print(traverseTree(root))