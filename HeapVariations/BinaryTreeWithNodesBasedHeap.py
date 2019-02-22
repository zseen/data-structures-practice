import IHeap
from typing import List
import time


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class Heap(IHeap.IHeap):
    def __init__(self):
        self.root = None

    def addElementToHeap(self, value):
        if self.root is None:
            self.root = Node(value)
            #print("root:", self.root.value)
        elif value < self.root.value:
            oldNode = self.root
            self.root = Node(value)
            #print("root:", self.root.value)
            self._insert(oldNode.value, self.root)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentNode):
        #print("value:", value)
        #print("currNodeVal: ", currentNode.value)
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
            self._insert(oldNode.value, currentNode.right)



    def removeAndReturnSmallestElement(self):
        oldRoot = self.root

        if not oldRoot.left:
            if oldRoot.right:
                self.root = oldRoot.right
                return oldRoot.value
        elif not oldRoot.right:
            if oldRoot.left:
                self.root = oldRoot.left
                return oldRoot.value
        else:
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
    print("smallest: ", h.removeAndReturnSmallestElement())
    print("smallest: ", h.removeAndReturnSmallestElement())
    print("smallest: ", h.removeAndReturnSmallestElement())
    print("smallest: ", h.removeAndReturnSmallestElement())
    h.addElementToHeap(7)
    #h.removeAndReturnSmallestElement()
    #print("new root", h.root.value)


if __name__ == '__main__':
    main()
