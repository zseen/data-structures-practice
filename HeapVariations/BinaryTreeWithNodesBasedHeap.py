from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

from typing import List
import unittest
import math


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTreeWithNodesBasedHeap(IHeap):
    def __init__(self, initialElements: List):
        self.root = None
        self._currentSize = 0
        for element in initialElements:
            self.add(element)

    def add(self, element: int) -> None:
        newNode = Node(element)
        self._insertNodeAtInitialPosition(newNode)
        self._moveNodeUp(newNode)

    def isHeapEmpty(self) -> bool:
        return self._currentSize == 0

    def getAndRemoveSmallest(self) -> int:
        if self.isHeapEmpty():
            raise HeapIsEmptyException("Heap empty - cannot return data")

        oldRoot: Node = self.root

        if not self.root.right and not self.root.left:
            assert self._currentSize == 1
            self.root = None
            self._currentSize -= 1
            return oldRoot.value

        newRoot = self.getLastChild()
        self._swapWithRoot(newRoot, oldRoot)

        self._currentSize -= 1
        self._moveNodeDown(newRoot)
        return oldRoot.value

    def _swapWithRoot(self, newRoot, oldRoot) -> None:
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

    def _insertNodeAtInitialPosition(self, newNode: Node) -> None:
        self._currentSize += 1

        if not self.root:
            self.root = newNode
        else:
            parentNode: Node = self.findParentOfFirstMissingChild()

            if not parentNode.left:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

            newNode.parent = parentNode

    def getLastChild(self) -> Node:
        pathString = self._getPathToLastChild()
        currentNode: Node = self.root

        for char in pathString:
            if char == "0":
                if currentNode.left:
                    currentNode = currentNode.left
            elif char == "1":
                if currentNode.right:
                    currentNode = currentNode.right
        return currentNode

    def _getPathToLastChild(self) -> str:
        currentLayerCapacity: int = int(self._getCurrentLayerCapacity())
        lastChildPositionInLevelBinary: str = bin(self._currentSize - currentLayerCapacity)

        lastChildPositionInLevelBinaryStripped: str = lastChildPositionInLevelBinary[2:]  # remove leading "0b"
        pathLength: int = int(math.log(currentLayerCapacity, 2))

        return lastChildPositionInLevelBinaryStripped.zfill(pathLength)

    def _getCurrentLayerCapacity(self) -> int:
        i = 0
        while math.pow(2, i) <= self._currentSize:
            i += 1
        return int(math.pow(2, i - 1))

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

    def isPreviousLevelFull(self):
        return self._currentSize != 0 and ((self._currentSize & (self._currentSize - 1)) == 0)

    def findParentOfFirstMissingChild(self):
        currCap = self._getCurrentLayerCapacity()
        prevCap = int(currCap / 2)
        #lastChild = self.getLastChild()
        #print("lc: ", lastChild.value)
        #lastChildPositionInLevelBinary: str = bin(self._currentSize - currCap)

        print("currCap: ", currCap)
        lastLevelOffset = self._currentSize - 1 - currCap
        print("llo: ", lastLevelOffset)
        previousLevelOffset = math.floor((lastLevelOffset + 1) / 2)
        print("plo: ", previousLevelOffset)

        print("currSize: ", self._currentSize)
        print("...")

        if self.isPreviousLevelFull():
            pathString = "0" * prevCap
            currentNode = self.root
            for _ in range(len(pathString)):
                if currentNode.left:
                    currentNode = currentNode.left
            return currentNode

        lastChildPositionInLevelBinary: str = bin(int(prevCap + previousLevelOffset))

        lastChildPositionInLevelBinaryStripped = lastChildPositionInLevelBinary[3:]  # remove leading "0b"
        pathLength: int = int(math.log(prevCap, 2))

        lastChildPositionInLevelBinaryStripped = lastChildPositionInLevelBinaryStripped.zfill(pathLength)

        #parentNodePath = bin(previousLevelOffset)

        currentNode = self.root
        for char in lastChildPositionInLevelBinaryStripped:
            if char == "0":
                if currentNode.left:
                    currentNode = currentNode.left
            elif char == "1":
                if currentNode.right:
                    currentNode = currentNode.right
        return currentNode


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

    def printTree(self):
        level = 0
        if self.root:
            self._printTree(self.root, level)

    def _printTree(self, node, level):
        if node:
            self._printTree(node.right, level + 1)
            print('  ' * level + str(node.value))
            self._printTree(node.left, level + 1)


def main():
    h = BinaryTreeWithNodesBasedHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    h.printTree()
    #h.findParentOfFirstMissingChild()


class InsertionAndRemovingSmallestElementTester(unittest.TestCase):
    def test_createEmptyHeap_heapIsEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([])

        self.assertTrue(h.isHeapEmpty())

    def test_getFromEmpty_heapIsEmptyExceptionRaised(self):
        h = BinaryTreeWithNodesBasedHeap([])

        with self.assertRaises(HeapIsEmptyException):
            h.getAndRemoveSmallest()

    def test_addOneElement_getAndRemoveSmallest_heapIsEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(2)
        self.assertFalse(h.isHeapEmpty())

        h.getAndRemoveSmallest()
        self.assertTrue(h.isHeapEmpty())

    def test_add_getAndRemoveSmallest_insertedElementIsReturned(self):
        h = BinaryTreeWithNodesBasedHeap([])
        elementToAdd: int = 4
        h.add(elementToAdd)
        elementRemovedValue: int = h.getAndRemoveSmallest()

        self.assertEqual(elementToAdd, elementRemovedValue)

    def test_addTwoElementsInOrder_getAndRemoveSmallest_heapIsEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(1)
        h.add(2)

        removedFirst: int = h.getAndRemoveSmallest()
        self.assertEqual(removedFirst, 1)

        removedSecond: int = h.getAndRemoveSmallest()
        self.assertEqual(removedSecond, 2)
        self.assertTrue(h.isHeapEmpty())

    def test_addTwoElementsNotInOrder_getAndRemoveSmallest_ascendingRemovedValues(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(2)
        h.add(1)

        removedFirst: int = h.getAndRemoveSmallest()
        self.assertEqual(removedFirst, 1)

        removedSecond: int = h.getAndRemoveSmallest()
        self.assertEqual(removedSecond, 2)

    def test_add_getAndRemoveSmallest_add_getAndRemoveSmallest_smallestNumberReturned(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(9)
        h.add(6)
        h.getAndRemoveSmallest()

        h.add(2)
        smallestElementValue: int = h.getAndRemoveSmallest()

        self.assertEqual(smallestElementValue, 2)

    def test_getAndRemoveSmallest_sortedElementsReturned(self):
        initialElementsList: List = [9, 1, 7, 3, 5, 6, 4, 8, 2, 10]
        h = BinaryTreeWithNodesBasedHeap(initialElementsList)

        result: List = []
        for _ in range(10):
            result.append(h.getAndRemoveSmallest())

        self.assertTrue(result == sorted(initialElementsList))

if __name__ == '__main__':
    #unittest.main()
    main()
