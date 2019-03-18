from IHeap import IHeap
from HeapIsEmptyException import HeapIsEmptyException

from typing import List
import heapq


class DefaultPythonHeap(IHeap):
    def __init__(self, initialElements: List):
        self.heapList = initialElements.copy()
        heapq.heapify(self.heapList)
        self.isHeapSorted: bool = True

    def add(self, element: int) -> None:
        heapq.heappush(self.heapList, element)
        self.isHeapSorted = False

    def isHeapEmpty(self) -> bool:
        return len(self.heapList) == 0

    def getAndRemoveSmallest(self) -> int:
        if self.isHeapEmpty():
            raise HeapIsEmptyException("Heap empty")

        if not self.isHeapSorted:
            heapq.heapify(self.heapList)
            self.isHeapSorted = True

        return heapq.heappop(self.heapList)
