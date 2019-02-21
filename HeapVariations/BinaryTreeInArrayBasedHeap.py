import IHeap
import HeapIsEmptyException
from typing import List


class BinaryTreeInArrayBasedHeap(IHeap.IHeap):
    def __init__(self, listToHeapify: List):
        self.heapList: List = [0]
        self.currentSize: int = 0
        for element in listToHeapify:
            self.add(element)

    def _moveElementUp(self, currentNodeIndex: int):
        parentIndex: int = currentNodeIndex // 2
        if self.heapList[currentNodeIndex] < self.heapList[parentIndex]:
            self.heapList[parentIndex], self.heapList[currentNodeIndex] = self.heapList[currentNodeIndex], self.heapList[parentIndex]
            self._moveElementUp(parentIndex)

    def add(self, element: int):
        self.heapList.append(element)
        self.currentSize += 1
        self._moveElementUp(self.currentSize)

    def _moveElementDown(self, currentNodeIndex: int):
        if currentNodeIndex * 2 <= self.currentSize:
            minValueChildIndex: int = self._getMinimumValueChildIndex(currentNodeIndex)
            if self.heapList[currentNodeIndex] > self.heapList[minValueChildIndex]:
                self.heapList[currentNodeIndex], self.heapList[minValueChildIndex] = self.heapList[minValueChildIndex], self.heapList[currentNodeIndex]
                self._moveElementDown(minValueChildIndex)

    def _getMinimumValueChildIndex(self, currentNodeIndex: int):
        leftChildIndex: int = 2 * currentNodeIndex
        rightChildIndex: int = 2 * currentNodeIndex + 1
        if rightChildIndex > self.currentSize or self.heapList[leftChildIndex] < self.heapList[rightChildIndex]:
            return leftChildIndex

        return rightChildIndex

    def isHeapEmpty(self):
        if self.currentSize == 0:
            return True
        return False

    def getAndRemoveSmallest(self):
        if self.isHeapEmpty():
            raise HeapIsEmptyException.HeapIsEmptyException("Heap empty")

        self.currentSize -= 1
        if self.currentSize == 0:
            minVal: int = self.heapList.pop()
        else:
            minVal: int = self.heapList[1]
            self.heapList[1] = self.heapList.pop()
            self._moveElementDown(1)

        return minVal
