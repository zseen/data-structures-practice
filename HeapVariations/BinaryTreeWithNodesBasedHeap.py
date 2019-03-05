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
            if node.parent is self.root:
                self.swapNodeWithRoot(node)
                break

            self.swapNodes(node, node.parent)

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

    def swapNodeWithRoot(self, node: Node) -> None:
        initialRoot: Node = self.root
        initialLeftChildOfNode: Node = node.left
        initialRightChildOfNode: Node = node.right

        if self.root.right == node:
            node.right = initialRoot
            node.left = initialRoot.left
        else:
            node.right = initialRoot.right
            node.left = initialRoot

        self.root = node
        self.root.parent = None
        initialRoot.parent = self.root

        if initialLeftChildOfNode:
            initialRoot.left = initialLeftChildOfNode
            initialLeftChildOfNode.parent = initialRoot

        if initialRightChildOfNode:
            initialRoot.right = initialRightChildOfNode
            initialRightChildOfNode.parent = initialRoot


def main():
    h = Heap()
    h.root = Node(2)
    h.add(1)


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

if __name__ == '__main__':
    #main()
    unittest.main()
