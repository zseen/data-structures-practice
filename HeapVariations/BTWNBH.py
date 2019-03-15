from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

import queue
from typing import List
import math


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTreeWithNodesBasedHeap(IHeap):
    def __init__(self):
        self.root = None
        self.currentSize = 0
        self.currentNode = self.root
        self.currentLayerCapacity = 0

    def add(self, element: int):
        newNode = Node(element)
        self.insertNodeAtInitialPosition(newNode)
        self._moveNodeUp(newNode)

    def insertNodeAtInitialPosition(self, newNode: Node):
        if not self.root:
            self.root = newNode
            self.currentSize += 1
        else:
            self.currentNode = self.root
            self.currentSize += 1

            newNodePositionInBinary = self.getBinaryValueOfNodePosition()

            for char in newNodePositionInBinary[3:]:
                if char == "0":
                    if self.currentNode.left:
                        self.goLeft()
                    else:
                        self.currentNode.left = newNode
                        newNode.parent = self.currentNode
                elif char == "1":
                    if self.currentNode.right:
                        self.goRight()
                    else:
                        self.currentNode.right = newNode
                        newNode.parent = self.currentNode

    def goLeft(self):
        self.currentNode = self.currentNode.left

    def goRight(self):
        self.currentNode = self.currentNode.right


    def getLayerCapacity(self):
        if not self.root:
            self.currentLayerCapacity = 1
        else:
            for i in range(1, 10000):
                if math.pow(2, i) > self.currentSize:
                    self.currentLayerCapacity = math.pow(2, i - 1)


    def getNodePositionInLayer(self):
        nodePosition = self.currentSize - self.currentLayerCapacity
        return nodePosition

    def getBinaryValueOfNodePosition(self):
        nodePosition = self.getNodePositionInLayer()
        binaryNodePosition = bin(nodePosition)
        return binaryNodePosition

    def _moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self._swapNodes(node, node.parent)

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
        # if self.isHeapEmpty():
        #     raise HeapIsEmptyException("Heap empty - cannot print tree")

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
    h = BinaryTreeWithNodesBasedHeap()
    h.add(8)
    h.add(2)
    h.add(30)
    h.add(4)
    h.add(50)
    h.add(1)
    h.add(70)

    h.printUpToThreeLayersOfTreeWithParents()



if __name__ == '__main__':
    main()


