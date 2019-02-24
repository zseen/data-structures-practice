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
        parentNode = self.findParentOfMissingChild()
        newNode = Node(element)

        if not parentNode.left:
            parentNode.left = newNode
        else:
            parentNode.right = newNode

        newNode.parent = parentNode
        print("newNodeCurrentParent: ", parentNode.value)

        while newNode.value < parentNode.value:
            newNode.parent = parentNode.parent
            parentNode.parent.left = newNode
            parentNode.parent = newNode
            newNode.left = parentNode
            newNode = parentNode


        print("newNodeRealParent", newNode.parent.value)

    def findParentOfMissingChild(self):
        missingChild = Node(0)
        missingChild.parent = None
        nodesToVisit = deque()

        nodesToVisit.appendleft(self.root)
        visitedNodes = set()

        while nodesToVisit:
            currentNode = nodesToVisit.pop()
            visitedNodes.add(currentNode)

            if currentNode.left and currentNode.right:
                nodesToVisit.appendleft(currentNode.left)
                nodesToVisit.appendleft(currentNode.right)
            else:
                missingChild.parent = currentNode
                return missingChild.parent


def main():
    h = Heap()

    h.root = Node(2)
    h.root.left = Node(4)
    h.root.left.parent = h.root
    h.root.left.left = Node(6)
    h.root.left.left.parent =  h.root.left

    h.root.right = Node(5)
    h.root.right.parent = h.root

    #h.root.left.left = Node(5)
    #h.root.right.parent = h.root
    #h.root.left.right = Node(6)

    #h.root.right.left = Node(7)
    #h.root.right.right = Node(8)


    #h.add(9)
    #h.add(10)
    #h.add(11)
    print("parent:" ,h.findParentOfMissingChild().value)
    h.add(7)

    print("---")
    print("new left child of root:", h.root.left.value)

    print("right child of parent:", h.root.left.right.value)
    print("parent of most recently added node: ", h.root.left.value)

   




    #print(h.root.value)


if __name__ == '__main__':
    main()
