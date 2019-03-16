from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

import math
from typing import List


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
        #self.currentNode = self.root
        self.currentLayerCapacity = 0
        for element in initialElements:
            self.add(element)

    def add(self, element: int) -> None:
        newNode = Node(element)
        self._insertNodeAtInitialPosition(newNode)
        self._moveNodeUp(newNode)

    def isHeapEmpty(self) -> bool:
        return self.root is None

    def getAndRemoveSmallest(self) -> int:
        if self.isHeapEmpty():
            raise HeapIsEmptyException("Heap empty - cannot return data")

        oldRoot: Node = self.root

        if not self.root.right and not self.root.left:
            self.root = None
            return oldRoot.value

        newRoot = self._getLastChild()

        if newRoot.parent.right is newRoot:
            newRoot.parent.right = None
        else:
            newRoot.parent.left = None
        newRoot.parent = None

        self.root = newRoot
        self.currentSize -= 1

        if oldRoot.right:
            oldRoot.right.parent = self.root
        self.root.right = oldRoot.right

        if oldRoot.left:
            oldRoot.left.parent = self.root
        self.root.left = oldRoot.left

        self._moveNodeDown(newRoot)
        return oldRoot.value

    def _insertNodeAtInitialPosition(self, newNode: Node) -> None:
        if not self.root:
            self.root = newNode
            self.currentSize += 1
        else:
            self.currentSize += 1
            currentNode = self.root

            newNodePositionInBinary = self._getBinaryValueOfNodePosition()
            for char in newNodePositionInBinary[3:]:
                if char == "0":
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                elif char == "1":
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode

                newNode.parent = currentNode

    def _getLastChild(self) -> Node:
        currentNode = self.root
        lastChildPositionBinary = self._getBinaryValueOfNodePosition()

        for char in lastChildPositionBinary[3:]:
            if char == "0":
                currentNode = currentNode.left
            elif char == "1":
                currentNode = currentNode.right
        return currentNode

    def _getBinaryValueOfNodePosition(self) -> str:
        nodePosition = self.currentSize - self.currentLayerCapacity
        binaryNodePosition = bin(nodePosition)
        return binaryNodePosition

    def _getLayerCapacity(self) -> int:
        currentLayerCapacity = 0
        if not self.root:
            currentLayerCapacity = 1
        else:
            i = 0
            while math.pow(2, i) < self.currentSize:
                currentLayerCapacity = math.pow(2, i)
                i += 1
        return currentLayerCapacity



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


def main():
    h = BinaryTreeWithNodesBasedHeap([12, 8, 20, 34, 2, 30, 3, 53, 4, 50, 1, 70])

    for _ in range(11):
        print(h.getAndRemoveSmallest())




if __name__ == '__main__':
    main()


