from Heap.HeapVariations import AbstractClassHeap
from typing import List
import time


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class Heap(AbstractClassHeap.AbstractHeap):
    def __init__(self):
        self.root = None

    def addElementToHeap(self, value):
        if self.root is None:
            self.root = Node(value)
        elif value < self.root.value:
            oldNode = self.root
            self.root = Node(value)
            self._insert(oldNode.value, self.root)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentNode):
        if currentNode.value < value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            elif currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self._insert(value, currentNode.left)
        else:
            oldNode = currentNode
            currentNode = Node(value)
            self._insert(oldNode.value, currentNode.left)




    def removeAndReturnSmallestElement(self):
        oldRoot = self.root
        if oldRoot.left.value < oldRoot.right.value:
            self.root = oldRoot.left
        else:
            self.root = oldRoot.right
        return oldRoot.value





def main():
    h = Heap()

    h.addElementToHeap(3)
    h.addElementToHeap(2)
    h.addElementToHeap(4)
    h.addElementToHeap(1)
    h.addElementToHeap(5)

    h.addElementToHeap(6)
    h.removeAndReturnSmallestElement()
    h.addElementToHeap(7)
    h.removeAndReturnSmallestElement()
    print(h.root.value)


if __name__ == '__main__':
    main()
