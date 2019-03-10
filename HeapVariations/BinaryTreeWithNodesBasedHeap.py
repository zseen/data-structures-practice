from IHeap import IHeap

import queue


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
        self._insertNodeAtInitialPosition(newNode)
        self._moveNodeUp(newNode)

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

    def _moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self._swapNodes(node, node.parent)

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
        if parentNode.left:
            parentNode.left.parent = childNode

        if parentNode.right:
            parentNode.right.parent = childNode

        if parentNode.left is childNode:
            childNode.right, parentNode.right = parentNode.right, childNode.right
            parentNode.left = childNode.left
            childNode.left = parentNode
        else:
            childNode.left, parentNode.left = parentNode.left, childNode.left
            parentNode.right = childNode.right
            childNode.right = parentNode


def main():
    h = Heap()
    h.add(2)
    h.add(4)
    h.add(9)
    h.add(5)
    h.add(7)
    h.add(8)
    h.add(6)
    h.add(10)

if __name__ == '__main__':
    main()
