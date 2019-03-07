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
            parentNode: Node = self.findParentOfFirstMissingChild()

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

    def findParentOfFirstMissingChild(self) -> Node:
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

    def findLastChild(self):
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


    def getAndRemoveSmallest(self):
        lastChildInTree: Node = self.findLastChild()
        # print("---")
        print("lastchild: ",lastChildInTree.value)
        # print("lastchild.parent: ", lastChildInTree.parent.value)
        print("root: ", self.root.value)

        if self.root.right:
            print("root.right: ", self.root.right.value)
            if self.root.right.right:
                print("root.right.right: ", self.root.right.right.value)
            if self.root.right.left:
                print("root.right.left: ", self.root.right.left.value)

        if self.root.left:
            print("root.left: ", self.root.left.value)
            if self.root.left.left:
                print("root.left.left: ", self.root.left.left.value)
            if self.root.left.right:
                print("root.left.right: ", self.root.left.right.value)



        # print("root.left: ", self.root.left.value)

        if lastChildInTree.parent.right is lastChildInTree:
            lastChildInTree.parent.right = None
        else:
            lastChildInTree.parent.left = None

        oldRoot = self.root
        self.root = lastChildInTree
        self.root.parent = None

        lastChildInTree.right = oldRoot.right
        if lastChildInTree.right:
            lastChildInTree.right.parent = lastChildInTree

        lastChildInTree.left = oldRoot.left
        if lastChildInTree.left:
            lastChildInTree.left.parent = lastChildInTree

        print("smallest: ", oldRoot.value)


        self.moveNodeDown(lastChildInTree)

        print("root: ", self.root.value)
        if self.root.right:
            print("root.right: ", self.root.right.value)
            if self.root.right.right:
                print("root.right.right: ", self.root.right.right.value)
        if self.root.left:
            print("root.left: ", self.root.left.value)
            if self.root.left.left:
                print("root.left.left: ", self.root.left.left.value)
            if self.root.left.right:
                print("root.left.right: ", self.root.left.right.value)

        print("---")

    def moveNodeDown(self, node: Node):
        while (node.left or node.right):
            if node.left and (node.value > node.left.value or node.value > node.right.value):
                print("HOW TO MAKE IT WORK THAT IT COMPARES LEFT AND RIGHT?")

                if node.right and node.left.value > node.right.value:
                    self._swapNodes(node.right, node)
                else:
                    self._swapNodes(node.left, node)








            #if node.right:
            #self._swapNodes(node.right, node)




def main():
    h = Heap()
    h.add(2)
    h.add(4)
    h.add(5)
    h.add(6)
    h.add(7)

    h.add(8)
    h.add(9)
    h.add(10)

    h.getAndRemoveSmallest()


    h.getAndRemoveSmallest()
    h.getAndRemoveSmallest()

    #h.getAndRemoveSmallest()
    #h.getAndRemoveSmallest()



if __name__ == '__main__':
    main()
