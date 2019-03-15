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
    def __init__(self, initialElements: List):
        self.root = None
        self.currentSize = 0
        self.currentNode = None
        self.currentLayerCapacity = 0
        self.isLayerFull = False

    def findInsertionPoint(self, newNode: Node):
        if not self.root:
            self.root = newNode
            self.isLayerFull = True
            self.currentNode = self.root
        self.currentSize += 1

        while self.currentNode.left:
            self.goLeft()


    def goLeft(self):
        self.currentNode = self.currentNode.left


    def getLayerCapacity(self):
        if not self.root:
            self.currentLayerCapacity = 1
        else:
            for i in range(1, 10000):
                if math.pow(2, i) > self.currentSize:
                    self.currentLayerCapacity = math.pow(2, i - 1)

    def isOverHalfWayInLayer(self):
        if 1.5 * self.currentLayerCapacity > self.currentSize:
            return False
        else:
            return True



