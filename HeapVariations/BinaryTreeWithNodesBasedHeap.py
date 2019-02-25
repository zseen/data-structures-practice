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

        while newNode.value < newNode.parent.value:
            initialParent = newNode.parent
            print("initialParent: ", initialParent.value)

            if newNode.parent is self.root:
                print("newNodeParent: ", newNode.parent.value)
                print("newNode: ", newNode.value)
                oldRootValue = self.root.value
                print("oldRoot: ", oldRootValue)
                print("newNode: ", newNode.value)
                self.root.value = newNode.value
                self.root.parent = None
                print("root.left: ", self.root.left.value)
                print("modifiedRoot: ", self.root.value)
                print("newNode: ", newNode.value)

                if not self.root.left:
                    self.root.left.value = oldRootValue
                    break
                else:
                    self.root.right.value = oldRootValue
                    break

            newNode.left = initialParent
            newNode.parent = initialParent.parent

            if initialParent.parent.right == initialParent:
                initialParent.parent.right = newNode
            else:
                initialParent.parent.left = newNode

            #print("newnodeParent: ", newNode.parent.value)
            initialParent.parent = newNode
            print("newnode: ", newNode.value)
            print("newnodeParent: ", newNode.parent.value)

            #newNode.parent = newNode.parent
            print("---")

            #break

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

    h.root = Node(1)
    h.root.left = Node(4)
    h.root.left.parent = h.root
    h.root.left.left = Node(6)
    h.root.left.left.parent = h.root.left
    h.root.left.right = Node(7)
    h.root.left.right.parent = h.root.left

    h.root.right = Node(2)
    h.root.right.parent = h.root
    h.root.right.left = Node(5)
    h.root.right.left.parent = h.root.right
    h.root.right.right = Node(8)
    h.root.right.right.parent = h.root.right


    print("root.right.right: ", h.root.right.right.value)


    #print("parent:",h.findParentOfMissingChild().value)
    h.add(3)

    print("root: ", h.root.value)
    print("left child of root: ", h.root.left.value)
    #print("root.left.left: ", h.root.left.left.value)
    print("right child of root: ", h.root.right.value)
    print("root.left.left: ", h.root.left.left.value)
    #print("root.left.right", h.root.left.right.value)
    print("root.left.left.left: ", h.root.left.left.left.value)



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


    def test_initialThreeLayers_leftHasTwoChildre_rightZero_newNodeSmallerThanRoot_twoSwaps(self):
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
        h.add(1)


        self.assertTrue(h.root.value == 1 and h.root.right.value == 2 and h.root.left.value == 4)



if __name__ == '__main__':
    main()
    #unittest.main()
