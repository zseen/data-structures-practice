from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

import queue


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTreeWithNodesBasedHeap(IHeap):
    def __init__(self):
        self.root = None

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
        else:
            lastChildInTree: Node = self._findLastChild()

            if lastChildInTree.parent.right is lastChildInTree:
                lastChildInTree.parent.right = None
            else:
                lastChildInTree.parent.left = None

            self.root = lastChildInTree
            self.root.parent = None

            lastChildInTree.right = oldRoot.right
            if lastChildInTree.right:
                lastChildInTree.right.parent = lastChildInTree

            lastChildInTree.left = oldRoot.left
            if lastChildInTree.left:
                lastChildInTree.left.parent = lastChildInTree

            self._moveNodeDown(lastChildInTree)
            return oldRoot.value

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

    def _insertNodeAtInitialPosition(self, newNode: Node) -> None:
        if not self.root:
            self.root = newNode
        else:
            parentNode: Node = self._findParentOfFirstMissingChild()

            if not parentNode.left:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

            newNode.parent = parentNode

    def _findParentOfFirstMissingChild(self) -> Node:
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

    def _findLastChild(self) -> Node:
        nodesToVisit: queue.deque = queue.deque()
        nodesToVisit.appendleft(self.root)
        visitedNodes: set = set()
        currentNode = None

        while nodesToVisit:
            currentNode = nodesToVisit.pop()
            visitedNodes.add(currentNode)

            if currentNode.left and currentNode.right:
                nodesToVisit.appendleft(currentNode.left)
                nodesToVisit.appendleft(currentNode.right)
            else:
                if currentNode.left:
                    return currentNode.left

        return currentNode

    def _moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self._swapNodes(node, node.parent)

    def _moveNodeDown(self, node: Node) -> None:
        while (node.left and node.value > node.left.value) or (node.right and node.value > node.right.value):
            if (not node.right) or (node.right.value > node.left.value):
                self._swapNodes(node.left, node)
            else:
                self._swapNodes(node.right, node)

    def _swapNodes(self, childNode: Node, parentNode: Node) -> None:
        self._swapChildren(childNode, parentNode)
        self._swapParent(childNode, parentNode)

    def _swapParent(self, childNode: Node, parentNode: Node) -> None:
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
    def _swapChildren(childNode: Node, parentNode: Node) -> None:
        if parentNode.left is childNode:
            childNode.right, parentNode.right = parentNode.right, childNode.right
            if parentNode.right:
                parentNode.right.parent = parentNode
            if childNode.right:
                childNode.right.parent = childNode

            parentNode.left = childNode.left
            if parentNode.left:
                parentNode.left.parent = parentNode
            childNode.left = parentNode
        else:
            childNode.left, parentNode.left = parentNode.left, childNode.left
            if parentNode.left:
                parentNode.left.parent = parentNode
            if childNode.left:
                childNode.left.parent = childNode

            parentNode.right = childNode.right
            if parentNode.right:
                parentNode.right.parent = parentNode
            childNode.right = parentNode


def main():
    h = BinaryTreeWithNodesBasedHeap()
    h.add(2)
    h.add(35)
    h.add(4)
    h.add(8)
    h.add(72)
    h.add(5)
    h.add(7)
    h.add(9)
    h.add(6)
    h.add(1)
    h.add(15)
    h.add(27)
    h.add(10)
    h.add(60)
    h.add(14)

    for _ in range(10):
        print(h.getAndRemoveSmallest())

    h.add(34)
    h.add(43)
    h.printUpToThreeLayersOfTreeWithParents()

if __name__ == '__main__':
    main()
