from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

from typing import List
import unittest
import random


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTreeWithNodesBasedHeap(IHeap):
    def __init__(self, initialElements: List):
        self.root = None
        self.currentSize = 0
        for element in initialElements:
            self.add(element)

    def add(self, element: int) -> None:
        newNode = Node(element)
        self._insertNodeAtInitialPosition(newNode)
        self._moveNodeUp(newNode)

    def isHeapEmpty(self) -> bool:
        return self.currentSize == 0

    def getAndRemoveSmallest(self) -> int:
        if self.isHeapEmpty():
            raise HeapIsEmptyException("Heap empty - cannot return data")

        oldRoot: Node = self.root

        if not self.root.right and not self.root.left:
            self.root = None
            self.currentSize -= 1
            return oldRoot.value

        newRoot = self._getLastChild()

        if newRoot.parent.right is newRoot:
            newRoot.parent.right = None
        else:
            newRoot.parent.left = None
        newRoot.parent = None

        self.root = newRoot

        if oldRoot.right:
            oldRoot.right.parent = self.root
        self.root.right = oldRoot.right

        if oldRoot.left:
            oldRoot.left.parent = self.root
        self.root.left = oldRoot.left

        self.currentSize -= 1
        self._moveNodeDown(newRoot)
        return oldRoot.value

    def _insertNodeAtInitialPosition(self, newNode: Node) -> None:
        self.currentSize += 1

        if not self.root:
            self.root = newNode
        else:
            parentNode: Node = self._getLastChild()

            if not parentNode.left:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

            newNode.parent = parentNode

    def _getLastChild(self) -> Node:
        currentNode = self.root
        lastChildPositionInBinary = bin(self.currentSize)

        # lastChildPositionInBinary starts with "0b", and also the first digit is not needed, as thepath starts from the root
        for char in lastChildPositionInBinary[3:]:
            if char == "0":
                if currentNode.left:
                    currentNode = currentNode.left
            elif char == "1":
                if currentNode.right:
                    currentNode = currentNode.right
        return currentNode

    def _moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self._swapNodes(node, node.parent)

    def _moveNodeDown(self, node: Node) -> None:
        while (node.left and node.value > node.left.value) or (node.right and node.value > node.right.value):
            shouldSwapToLeft = (not node.right) or (node.right.value > node.left.value)
            if shouldSwapToLeft:
                self._swapNodes(node.left, node)
            else:
                self._swapNodes(node.right, node)

    def _swapNodes(self, childNode: Node, parentNode: Node) -> None:
        self._directionDependentSwap(childNode, parentNode)
        self._notDirectionDependentSwap(childNode, parentNode)

    def _notDirectionDependentSwap(self, childNode: Node, parentNode: Node) -> None:
        if parentNode is self.root:
            self.root = childNode
            self.root.parent = None
        else:
            childNode.parent = parentNode.parent
            if parentNode.parent.left is parentNode:
                parentNode.parent.left = childNode
            else:
                parentNode.parent.right = childNode

        parentNode.parent = childNode

    @staticmethod
    def _directionDependentSwap(childNode: Node, parentNode: Node) -> None:
        if parentNode.left is childNode:
            if childNode.right:
                childNode.right.parent = parentNode
            if parentNode.right:
                parentNode.right.parent = childNode

            childNode.right, parentNode.right = parentNode.right, childNode.right

            if childNode.left:
                childNode.left.parent = parentNode
            parentNode.left = childNode.left
            childNode.left = parentNode
        else:
            if childNode.left:
                childNode.left.parent = parentNode
            if parentNode.left:
                parentNode.left.parent = childNode

            childNode.left, parentNode.left = parentNode.left, childNode.left

            if childNode.right:
                childNode.right.parent = parentNode
            parentNode.right = childNode.right
            childNode.right = parentNode

    def printUpToThreeLayersOfTreeWithParents(self) -> None:
        if self.isHeapEmpty():
            raise HeapIsEmptyException("Heap empty - cannot print tree")

        print("...")
        if self.root.right:
            if self.root.right.right:
                print("  " + "root.right.right: ", self.root.right.right.value)
                print("  " + "root.right.right.parent: ", self.root.right.right.parent.value)
            if self.root.right.left:
                print("  " + "root.right.left: ", self.root.right.left.value)
                print("  " + "root.right.left.parent: ", self.root.right.left.parent.value)

            print(" " + "root.right: ", self.root.right.value)
            print(" " + "root.right.parent: ", self.root.right.parent.value)

        print("root: ", self.root.value)

        if self.root.left:
            print(" " + "root.left: ", self.root.left.value)
            print(" " + "root.left.parent: ", self.root.left.parent.value)
            if self.root.left.right:
                print("  " + "root.left.right: ", self.root.left.right.value)
                print("  " + "root.left.right.parent: ", self.root.left.right.parent.value)
            if self.root.left.left:
                print("  " + "root.left.left: ", self.root.left.left.value)
                print("  " + "root.left.left.parent: ", self.root.left.left.parent.value)
        print("...")


def main():
    initialElements: List = [random.randrange(1000) for _ in range(30)]
    h = BinaryTreeWithNodesBasedHeap(initialElements)

    result = []
    for i in range(30):
        h.printUpToThreeLayersOfTreeWithParents()
        result.append(h.getAndRemoveSmallest())

    print(result == sorted(initialElements))
    print("current size of heap: ", h.currentSize)
    print("Heap is empty: ", h.isHeapEmpty())

    h.add(56)
    h.add(31)
    h.add(2)
    print("current size of heap: ", h.currentSize)

    result = []
    for i in range(3):
        result.append(h.getAndRemoveSmallest())
    print(result)


class InsertionAndRemovingSmallestElementTester(unittest.TestCase):
    def test_add_zeroInitialElement_insertThreeNodesInOrder(self):
        h = BinaryTreeWithNodesBasedHeap([1, 2, 3])

        self.assertTrue(h.root.value == 1 and h.root.left.value == 2 and h.root.right.value == 3)

    def test_add_zeroInitialElement_insertThreeNodesRandom_rootSwap(self):
        h = BinaryTreeWithNodesBasedHeap([3, 2, 1])

        self.assertTrue(h.root.value == 1 and h.root.left.value == 3 and h.root.right.value == 2 and h.root.right.parent.value == 1)

    def test_add_fourInitialElements_insertThreeNodesRandom_rootSwap(self):
        h = BinaryTreeWithNodesBasedHeap([9, 3, 6, 8])
        h.add(4)
        h.add(1)
        h.add(7)

        self.assertTrue(h.root.value == 1, h.root.left.value == 4 and h.root.right.value == 3 and h.root.left.parent.value == 1)

    def test_getAndRemoveSmallest_oneInitialElement_heapBecomesEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([2])
        self.assertTrue(h.getAndRemoveSmallest() == 2 and h.isHeapEmpty() and h.currentSize == 0)

    def test_getAndRemoveSmallest_threeInitialElements_removeTwo_onlyRootRemains(self):
        h = BinaryTreeWithNodesBasedHeap([3, 1, 2])
        self.assertTrue(h.getAndRemoveSmallest() == 1 and h.getAndRemoveSmallest() == 2 and h.root.value == 3 and
                        (not h.root.left and not h.root.right))

    def test_getAndRemoveSmallest_tenInitialElements_heapBecomesEmpty(self):
        initialElementsList: List = [9, 1, 7, 3, 5, 6, 4, 8, 2, 10]
        h = BinaryTreeWithNodesBasedHeap(initialElementsList)

        result = []
        for _ in range(10):
            result.append(h.getAndRemoveSmallest())

        self.assertTrue(result == sorted(initialElementsList))

    def test_getAndRemoveAddGetAndRemove_heapBecomesEmpty_notEmpty_emptyAgain(self):
        h = BinaryTreeWithNodesBasedHeap([7, 2, 1])

        firstRounRemovalValues: List = []
        for i in range(3):
            firstRounRemovalValues.append(h.getAndRemoveSmallest())

        for i in range(5):
            h.add(i)

        secondRounRemovalValues: List = []
        for i in range(5):
            secondRounRemovalValues.append(h.getAndRemoveSmallest())

        self.assertTrue(h.isHeapEmpty(), firstRounRemovalValues == [1, 2, 7] and secondRounRemovalValues == [1, 2, 3, 4, 5])


if __name__ == '__main__':
    #main()
    unittest.main()