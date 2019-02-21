import IHeap
import HeapIsEmptyException
from typing import List


class SimpleArrayBasedHeap(IHeap.IHeap):
    def __init__(self, heapList: List):
        self.heapList: List = sorted(heapList)
        self.isHeapSorted: bool = True

    def isHeapEmpty(self):
        if len(self.heapList) == 0:
            return True
        return False

    def getAndRemoveSmallest(self):
        if self.isHeapEmpty():
            raise HeapIsEmptyException.HeapIsEmptyException("Heap empty")

        if not self.isHeapSorted:
            self.heapList.sort()
            self.isHeapSorted = True

        return self.heapList.pop(0)

    def add(self, element: int):
        self.heapList.append(element)
        self.isHeapSorted = False
