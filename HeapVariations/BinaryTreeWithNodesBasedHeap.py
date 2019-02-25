import IHeap
from typing import List
from queue import deque
import unittest


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
        #print("newNodeCurrentParent: ", parentNode.value)

        while newNode.value < parentNode.value:
            newNode.parent = parentNode.parent
            #print("nnn: ", parentNode.parent.value)
            if parentNode.parent.right == parentNode:
                parentNode.parent.right = newNode
            else:
                parentNode.parent.left = newNode
            #print("nnn: ", newNode.parent.value)
            parentNode.parent = newNode
            #print("nnn: ", parentNode.parent.value)
            newNode.left = parentNode
            #print("nnn: ", newNode.parent.value)
            #print("nnn: ", parentNode.parent.value)
            print(parentNode.value)
            print(parentNode.parent.value)
            #parentNode = parentNode.parent
            #print(newNode.parent.value)
            #newNode = newNode.parent
            print("newNode.value", newNode.value)
            print("HOW TO MOVE ON?")
            break

            #print(parentNode.parent.value)
            #print("nnn: ", newNode.parent.value)


        #print("newNodeRealParent", newNode.parent.value)

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
    h.root.left.left.parent = h.root.left
    h.root.left.right = Node(7)
    h.root.left.right.parent = h.root.left

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
    print("parent:",h.findParentOfMissingChild().value)
    h.add(1)

    print("root: ", h.root.value)
    print("right child of root:", h.root.right.value)

    # print("---")
    # print("new right child of root:", h.root.right.value)

    #print("right child of parent:", h.root.left.right.value)
    #print("parent of most recently added node: ", h.root.left.value)


class InsertionTester(unittest.TestCase):
    def test_initialTwoLayers_zeroChildren_insertAsLeftChild_oneSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(3)

        self.assertEqual(h.root.left.value, 3)

    def test_initialThreeLayers_leftChildHasLeftChild_insertAsRightChild_zeroSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.left.left = Node(6)
        h.root.left.left.parent = h.root.left
        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(7)

        self.assertEqual(h.root.left.right.value, 7)


    def test_initialTwoLayers_leftChildHas2Children_insertAsLeftChildOfRightChild_oneSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.left.left = Node(6)
        h.root.left.left.parent = h.root.left
        h.root.left.right = Node(7)
        h.root.left.right.parent = h.root.left
        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(3)

        self.assertTrue(h.root.right.left.value == 5 and h.root.right.value == 3)


if __name__ == '__main__':
    main()
    #unittest.main()
