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

    def _moveNodeUp(self, node: Node) -> None:
        while node.parent and node.value < node.parent.value:
            self._swapNodes(node, node.parent)

    def _swapNodes(self, childNode: Node, parentNode: Node) -> None:
        self._setChildren(childNode, parentNode)
        self._setParent(childNode, parentNode)

    def _setParent(self, childNode: Node, parentNode: Node) -> None:
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
    def _setChildren(childNode: Node, parentNode: Node) -> None:
        if parentNode.left is childNode:
            childNode.right, parentNode.right = parentNode.right, childNode.right
            parentNode.left = childNode.left
            childNode.left = parentNode
        else:
            parentNode.right = childNode.right
            childNode.right = parentNode
            childNode.left, parentNode.left = parentNode.left, childNode.left

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


def main():
    h = Heap()
    h.add(4)
    print(h.root.value)
    h.add(2)
    print(h.root.value)
    print(h.root.left.value)

if __name__ == '__main__':
    main()
