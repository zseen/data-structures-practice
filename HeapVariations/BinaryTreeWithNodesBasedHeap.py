import IHeap
from typing import List
from queue import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None



class Heap(IHeap.IHeap):
    def __init__(self):
        self.root = None


    def add(self, element: int):


    def findParentOfMissingChild(self):
        missingChild = Node(0)
        missingChild.parent = None
        nodesToVisit = deque()

        nodesToVisit.appendleft(self.root)
        visitedNodes = set()

        while nodesToVisit:
            currentNode = nodesToVisit.pop()
            visitedNodes.add(currentNode)

            #print("currentNode: ", currentNode.value)

            if currentNode.left and currentNode.right:
                nodesToVisit.appendleft(currentNode.left)
                nodesToVisit.appendleft(currentNode.right)
            else:
                missingChild.parent = currentNode
                return missingChild.parent


def main():
    h = Heap()

    h.root = Node(2)
    h.root.left = Node(3)
    #h.root.left.parent = h.root
    h.root.right = Node(4)

    h.root.left.left = Node(5)
    #h.root.right.parent = h.root
    h.root.left.right = Node(6)

    h.root.right.left = Node(7)
    h.root.right.right = Node(8)
    print(h.findParentOfMissingChild().value)



    #print(h.root.value)


if __name__ == '__main__':
    main()
