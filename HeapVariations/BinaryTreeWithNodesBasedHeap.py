from IHeap import IHeap

import queue
import unittest


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Heap(IHeap):
    def __init__(self):
        self.root = None

    def add(self, element: int) -> None:
        newNode = Node(element)
        self.insertNodeAtInitialPosition(newNode)
        self.moveNodeUp(newNode)

    def findParentOfFirstMissingChild(self) -> Node:
        nodesToVisit: queue.deque = queue.deque()
        nodesToVisit.appendleft(self.root)
        visitedNodes: set = set()

        while nodesToVisit:
            currentNode = nodesToVisit.pop()
            visitedNodes.add(currentNode)

            if currentNode.left and currentNode.right:
                nodesToVisit.appendleft(currentNode.left)
                nodesToVisit.appendleft(currentNode.right)
            else:
                return currentNode

    def insertNodeAtInitialPosition(self, newNode: Node) -> None:
        parentNode: Node = self.findParentOfFirstMissingChild()

        if not parentNode.left:
            parentNode.left = newNode
        else:
            parentNode.right = newNode

        newNode.parent = parentNode

    def moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self.swapNodes(node, node.parent)

    def swapNodes(self, childNode: Node, parentNode: Node) -> None:
        initialRightChildOfChildNode: Node = childNode.right
        initialLeftChildOfChildNode: Node = childNode.left

        if parentNode.left is childNode:
            childNode.right = parentNode.right
            parentNode.left = initialLeftChildOfChildNode
            childNode.left = parentNode
            parentNode.right = initialRightChildOfChildNode
        else:
            parentNode.right = initialRightChildOfChildNode
            childNode.right = parentNode
            childNode.left = parentNode.left
            parentNode.left = initialLeftChildOfChildNode

        if parentNode.parent:
            childNode.parent = parentNode.parent
            if parentNode.parent.left is parentNode:
                parentNode.parent.left = childNode
            else:
                parentNode.parent.right = childNode
        else:
            self.root = childNode
            self.root.parent = None

        parentNode.parent = childNode


def main():
    h = Heap()
    h.root = Node(2)
    h.root.left = Node(4)
    h.root.left.parent = h.root
    h.root.left.left = Node(6)
    h.root.left.left.parent = h.root.left
    h.root.left.right = Node(7)
    h.root.left.right.parent = h.root.left

    h.root.left.right.left = Node(14)
    h.root.left.right.left.parent = h.root.left.right
    h.root.left.right.right = Node(15)
    h.root.left.right.right.parent = h.root.left.right

    h.root.left.left.left = Node(9)
    h.root.left.left.left.parent = h.root.left.left
    h.root.left.left.right = Node(10)
    h.root.left.left.right.parent = h.root.left.left

    h.root.right = Node(5)
    h.root.right.parent = h.root
    h.root.right.left = Node(8)
    h.root.right.left.parent = h.root.right
    h.root.right.left.right = Node(13)
    h.root.right.left.right.parent = h.root.right.left
    h.root.right.left.left = Node(13)
    h.root.right.left.left.parent = h.root.right.left

    h.root.right.right = Node(11)
    h.root.right.right.parent = h.root.right

    h.root.right.right.left = Node(16)
    h.root.right.right.left.parent = h.root.right.right

    h.add(3)

    print("root: ", h.root.value)
    print("root.left: ", h.root.left.value)
    print("root.right: ", h.root.right.value)
    print("root.right.right: ", h.root.right.right.value)
    print("root.right.left: ", h.root.right.left.value)
    print("root.right.left.right: ", h.root.right.left.right.value)
    print("root.right.right.right: ", h.root.right.right.right.value)
    print("root.right.right.left: ", h.root.right.right.left.value)
    print("root.right.left.right: ", h.root.right.left.right.value)
    print("root.left.left: ", h.root.left.left.value)
    print("root.left.right: ", h.root.left.right.value)
    print("root.left.left.left: ", h.root.left.left.left.value)


class InsertionTester(unittest.TestCase):
    def test_initialThreeLayers_leftChildHasOneChild_insertAsRightChildOfLeft_zeroSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.left.left = Node(6)
        h.root.left.left.parent = h.root.left

        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(7)

        self.assertTrue(h.root.left.right.value == 7 and h.root.right.value == 5 and h.root.left.left.value == 6)

    def test_initialTwoLayers_rootHasTwoChildren_insertAsLeftChildOfLeft_oneSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root

        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(3)

        self.assertTrue(h.root.left.value == 3)

    def test_initialThreeLayers_leftChildHasTwoChildren_insertAsLeftChildOfRight_oneSwap(self):
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

    def test_initialThreeLayers_leftAndRightTwoChildren_insertAsLeftChildOfLeftLeft_newNodeLeftChildOfRoot_twoSwaps(self):
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

    def test_initialOneLayer_insertAsLeftChild_newNodeSmallerThanRoot_oneSwap(self):
        h = Heap()
        h.root = Node(2)
        h.add(1)

        self.assertTrue(h.root.value == 1 and h.root.left.value == 2)

    def test_initialTwoLayers_insertAsRightChild_newNodeSmallerThanRoot_oneSwap(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.add(1)

        self.assertTrue(h.root.value == 1 and h.root.right.value == 2 and h.root.left.value == 4)

    def test_initialThreeLayers_leftHasTwoChildren_insertAsLeftChildOfRight_newNodeSmallerThanRoot_twoSwaps(self):
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

    def test_initialTwoLayers_insertAsLeftChildOfLeftChild_newNodeSmallerThanRoot_twoSwaps(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root

        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.add(1)

        self.assertTrue(h.root.value == 1 and h.root.left.value == 2 and h.root.right.value == 5 and h.root.left.left.value == 4)

    def test_initialThreeLayers_insertAsRightChildOfRightChild_oneSwap(self):
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
        h.root.right.left = Node(8)
        h.root.right.left.parent = h.root.right
        h.add(3)

        self.assertTrue(h.root.right.value == 3 and h.root.right.right.value == 5 and h.root.right.left.value == 8)

    def test_initialFourLayers_leftBranchFull_insertAtRightRightRight_twoSwaps(self):
        h = Heap()
        h.root = Node(2)
        h.root.left = Node(4)
        h.root.left.parent = h.root
        h.root.left.left = Node(6)
        h.root.left.left.parent = h.root.left
        h.root.left.right = Node(7)
        h.root.left.right.parent = h.root.left

        h.root.left.right.left = Node(14)
        h.root.left.right.left.parent = h.root.left.right
        h.root.left.right.right = Node(15)
        h.root.left.right.right.parent = h.root.left.right

        h.root.left.left.left = Node(9)
        h.root.left.left.left.parent = h.root.left.left
        h.root.left.left.right = Node(10)
        h.root.left.left.right.parent = h.root.left.left

        h.root.right = Node(5)
        h.root.right.parent = h.root
        h.root.right.left = Node(8)
        h.root.right.left.parent = h.root.right
        h.root.right.left.right = Node(13)
        h.root.right.left.right.parent = h.root.right.left
        h.root.right.left.left = Node(13)
        h.root.right.left.left.parent = h.root.right.left

        h.root.right.right = Node(11)
        h.root.right.right.parent = h.root.right

        h.root.right.right.left = Node(16)
        h.root.right.right.left.parent = h.root.right.right
        h.add(3)

        self.assertTrue(h.root.value == 2 and h.root.right.value == 3 and h.root.right.right.value == 5
                        and h.root.right.right.right.value == 11 and h.root.right.right.left.value == 16 and h.root.right.left.value == 8)

if __name__ == '__main__':
    main()
    #unittest.main()
