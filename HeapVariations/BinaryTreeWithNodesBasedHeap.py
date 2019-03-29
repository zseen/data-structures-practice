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
        self._root = None
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

        oldRoot: Node = self._root

        if not self._root.right and not self._root.left:
            assert self._currentSize == 1
            self._root = None
            self._currentSize -= 1
            return oldRoot.value

        newRoot = self._getLastChild()
        self._swapWithRoot(newRoot)

        self._currentSize -= 1
        self._moveNodeDown(newRoot)

        return oldRoot.value

    def _getLastChild(self) -> Node:
        currentLevelCapacity: int = int(self._getCurrentLevelCapacity())
        lastChildPositionInLevelBinary: str = bin(self._currentSize - currentLevelCapacity)

        pathToLastChild = self._generatePath(currentLevelCapacity, lastChildPositionInLevelBinary)
        return self._getLastNodeInPath(pathToLastChild)

    def _generatePath(self, levelCapacity, nodePositionInBinary) -> str:
        pathLength: int = int(math.log2(levelCapacity))

        # if pathLenght is 0, the path is "0", but it should be empty instead as the root is the start and end of the path
        if pathLength == 0:
            path = ""
            return path

        path: str = nodePositionInBinary[2:]  # remove the leading "0b"
        path = path.zfill(pathLength)

        return path

    def _getLastNodeInPath(self, pathString: str) -> Node:
        currentNode: Node = self._root
        for char in pathString:
            if char == "0":
                if currentNode.left:
                    currentNode = currentNode.left
            elif char == "1":
                if currentNode.right:
                    currentNode = currentNode.right
        return currentNode

    def _swapWithRoot(self, newRoot) -> None:
        if newRoot.parent.right is newRoot:
            newRoot.parent.right = None
        else:
            newRoot.parent.left = None
        newRoot.parent = None

        if self._root.right:
            self._root.right.parent = newRoot
        newRoot.right = self._root.right

        if self._root.left:
            self._root.left.parent = newRoot
        newRoot.left = self._root.left

        self._root = newRoot

    def _insertNodeAtInitialPosition(self, newNode: Node) -> None:
        if not self._root:
            self._root = newNode
        else:
            parentNode: Node = self._findParentOfFirstMissingChild()

            if not parentNode.left:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

            newNode.parent = parentNode
        self._currentSize += 1

    def _findParentOfFirstMissingChild(self) -> Node:
        currentLevelCapacity: int = self._getCurrentLevelCapacity()
        previousLevelCapacity: int = int(currentLevelCapacity / 2)

        if self._isCurrentLevelFull():
            pathString: str = "0" * previousLevelCapacity
            return self._getLastNodeInPath(pathString)

        lastChildPositionsInLevel: int = self._currentSize - currentLevelCapacity
        parentPositionInPreviousLevel: int = int(math.floor((lastChildPositionsInLevel + 1) / 2))

        parentPositionInLevelBinary: str = bin(int(parentPositionInPreviousLevel))
        pathToParent = self._generatePath(previousLevelCapacity, parentPositionInLevelBinary)
        return self._getLastNodeInPath(pathToParent)

    def _isCurrentLevelFull(self):
        return self._isPowerOfTwo(self._currentSize + 1)

    def _isPowerOfTwo(self, nodeToAddPosition):
        while nodeToAddPosition > 1:
            if nodeToAddPosition % 2 != 0:
                return False
            nodeToAddPosition /= 2
        return True

    def _getCurrentLevelCapacity(self) -> int:
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
        if parentNode is self._root:
            self._root = childNode
            self._root.parent = None
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

    def printTree(self):
        if self._root:
            self._printTreeRecursive(self._root, 0)

    @staticmethod
    def _printTreeRecursive(node, level):
        if node:
            BinaryTreeWithNodesBasedHeap._printTreeRecursive(node.right, level + 1)
            print('  ' * level + str(node.value))
            BinaryTreeWithNodesBasedHeap._printTreeRecursive(node.left, level + 1)


class InsertionAndRemovingSmallestElementTester(unittest.TestCase):
    def test_createEmptyHeap_heapIsEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([])

        self.assertTrue(h.isHeapEmpty())

    def test_getFromEmpty_heapIsEmptyExceptionRaised(self):
        h = BinaryTreeWithNodesBasedHeap([])

        with self.assertRaises(HeapIsEmptyException):
            h.getAndRemoveSmallest()

    def test_addAndGet_heapIsEmpty(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(2)
        self.assertFalse(h.isHeapEmpty())

        h.getAndRemoveSmallest()
        self.assertTrue(h.isHeapEmpty())

    def test_addAndGet_insertedElementIsReturned(self):
        h = BinaryTreeWithNodesBasedHeap([])
        elementToAdd: int = 4
        h.add(elementToAdd)
        elementRemovedValue: int = h.getAndRemoveSmallest()

        self.assertEqual(elementToAdd, elementRemovedValue)
        self.assertTrue(h.isHeapEmpty())

    def test_addTwoElementsInOrderGetAndRemoveSmallest_ascendingRemovedValues(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(1)
        h.add(2)

        removedFirst: int = h.getAndRemoveSmallest()
        self.assertEqual(removedFirst, 1)
        self.assertFalse(h.isHeapEmpty())

        removedSecond: int = h.getAndRemoveSmallest()
        self.assertEqual(removedSecond, 2)
        self.assertTrue(h.isHeapEmpty())

    def test_addTwoElementsNotInOrderGetAndRemoveSmallest_ascendingRemovedValues(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(2)
        h.add(1)

        removedFirst: int = h.getAndRemoveSmallest()
        self.assertEqual(removedFirst, 1)
        self.assertFalse(h.isHeapEmpty())

        removedSecond: int = h.getAndRemoveSmallest()
        self.assertEqual(removedSecond, 2)
        self.assertTrue(h.isHeapEmpty())

    def test_addAndGetRepeatedly_smallestNumberReturned(self):
        h = BinaryTreeWithNodesBasedHeap([])
        h.add(9)
        h.add(6)
        h.getAndRemoveSmallest()
        self.assertFalse(h.isHeapEmpty())

        h.add(2)
        smallestElementValue: int = h.getAndRemoveSmallest()

        self.assertEqual(smallestElementValue, 2)
        self.assertFalse(h.isHeapEmpty())

    def test_getAndRemoveSmallest_initializedWithList(self):
        initialElementsList: List = [9, 1, 7, 3, 5, 6, 4, 8, 2, 10]
        h = BinaryTreeWithNodesBasedHeap(initialElementsList)

        result: List = []
        for _ in range(10):
            result.append(h.getAndRemoveSmallest())

        self.assertTrue(result == sorted(initialElementsList))
        self.assertTrue(h.isHeapEmpty())

if __name__ == '__main__':
    unittest.main()
