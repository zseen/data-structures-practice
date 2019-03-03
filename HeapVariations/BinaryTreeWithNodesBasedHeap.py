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


    def swapNodes(self, childNode: Node, parentNode: Node) -> None:
        parentNode.left = childNode.left
        childNode.right = parentNode.right
        childNode.left = parentNode

        childNode.parent = parentNode.parent

        if parentNode.parent.left == parentNode:
            parentNode.parent.left = childNode
        else:
            parentNode.parent.right = childNode

        parentNode.right = childNode.right
        parentNode.parent = childNode







    def sN(self, childNode: Node, parentNode: Node) -> None:
        parentNode.left = childNode.left

        if parentNode.left:
            print("parentNode.left: ", parentNode.left.value)

        childNode.right = parentNode.right

        if childNode.right:
            print("childNode.right: ", childNode.right.value)

        childNode.left = parentNode
        print("childNode.left: ", childNode.left.value)

        childNode.parent = parentNode.parent
        print("childNode.parent: ", childNode.parent.value)

        childNode.parent.left = childNode

        if childNode.parent.parent:
            print("grandparentNode: ", childNode.parent.parent.value)

        print("rootIterationEnd: ", self.root.value)
        print("leftChildRoot: ", self.root.left.value)

        parentNode.right = childNode.right
        parentNode.parent = childNode


    def add(self, element: int) -> None:
        newNode = self.getNewNodeInsertedAtInitialPosition(element)
        self.moveNodeUp(newNode)

    def getNewNodeInsertedAtInitialPosition(self, element: int) -> Node:
        parentNode = self.findParentOfMissingChild()
        newNode = Node(element)

        if not parentNode.left:
            parentNode.left = newNode
        else:
            parentNode.right = newNode

        newNode.parent = parentNode
        return newNode


    def moveNodeUp(self, node: Node):
        while node.value < node.parent.value:
            print("node: ", node.value)
            print("initialParent: ", node.parent.value)

            if node.parent.right:
                print("parent.right: ", node.parent.right.value)

            if node.left:
                print("node.left: ", node.left.value)
            if node.right:
                print("node.right: ", node.right.value)

            self.swapNodes(node, node.parent)

            print("---")
            print("currNode: ", node.value)
            print("currPar: ", node.parent.value)

            # parentNode.left = childNode.left
            # childNode.right = parentNode.right
            # childNode.left = parentNode
            #
            # childNode.parent = parentNode.parent
            #
            # if parentNode.parent.left == parentNode:
            #     parentNode.parent.left = childNode
            # else:
            #     parentNode.parent.right = childNode
            #
            # parentNode.right = childNode.right
            # parentNode.parent = childNode


            if node.parent is self.root and node.value < self.root.value:
                oldRoot = self.root
                print("oldRoot: ", oldRoot.value)
                print("root.right: ", self.root.right.value)
                print("root.left: ", self.root.left.value)
                print("root.left.left: ", self.root.left.left.value)

                formerLeft = node.left
                print("formerLeft: ", node.left.value)
                formerRight = node.right


                if self.root.right == node:
                    node.right = oldRoot
                    turn = "right"
                else:
                    node.left = oldRoot
                    turn = "left"


                self.root = node

                if turn == "left":
                    self.root.left = oldRoot
                    self.root.right = oldRoot.right
                else:
                    self.root.left = oldRoot.left
                    self.root.right = oldRoot


                print("root.left: ", self.root.left.value)
                oldRoot.left = formerLeft
                formerLeft.parent = oldRoot
                oldRoot.right = formerRight
                if formerRight:
                    formerRight.parent = oldRoot
                oldRoot.parent = node
                self.root.parent = None
                print("root.left: ", self.root.left.value)
                print("root.right: ", self.root.right.value)



                break




            print("node: ", node.value)
            #print("node.parent: ", node.parent.value)

            if node.left:
                print("node.left: ", node.left.value)

            if node.right:
                print("node.right: ", node.right.value)
            print("---")

    def findParentOfMissingChild(self) -> Node:
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
    # h.root = Node(2)
    # h.root.left = Node(4)
    # h.root.left.parent = h.root
    # h.root.left.left = Node(6)
    # h.root.left.left.parent = h.root.left
    # h.root.left.right = Node(7)
    # h.root.left.right.parent = h.root.left
    #
    # h.root.right = Node(5)
    # h.root.right.parent = h.root
    # h.add(1)
    # h.add(8)

    h.root = Node(2)
    h.root.left = Node(4)
    h.root.left.parent = h.root

    h.root.right = Node(5)
    h.root.right.parent = h.root
    h.add(1)


    print("root: ", h.root.value)
    print("root.left: ", h.root.left.value)
    #print("root.left.left: ", h.root.left.left.value)
    print("root.right: ", h.root.right.value)
    print("root.left.left: ", h.root.left.left.value)
    #print("root.left.right", h.root.left.right.value)
    #print("root.left.left.left: ", h.root.left.left.left.value)
    #print("root.right.left: ", h.root.right.left.value)
    #print("root.right.right: ", h.root.right.right.value)
    print("root.right: ", h.root.right.value)



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


    def test_initialThreeLayers_leftHasTwoChildren_rightZero_newNodeSmallerThanRoot_twoSwaps(self):
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

    def test_initialThreeLayers_LeftAndRightTwoChildren_newNodeRootLeftChild_twoSwaps(self):
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
        h.add(3)

        self.assertTrue(h.root.left.value == 3 and h.root.left.right.value == 7 and h.root.left.left.left.value == 6)

    def test_initialTwoLayers_insertedAsChildLeftChild_newNodeSmallerThanRoot_twoSwaps(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(1)

        self.assertTrue(h.root.value == 1 and h.root.left.value == 2 and h.root.right.value == 5 and h.root.left.left.value == 4)







if __name__ == '__main__':
    main()
    #unittest.main()
