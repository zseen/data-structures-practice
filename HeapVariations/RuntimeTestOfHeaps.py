from HeapVariations import IHeap
from HeapVariations import BinaryTreeInArrayBasedHeap
from HeapVariations import SimpleArrayBasedHeap

import random
import time


def modifyHeap(heap, repeatRange, action):
    if action == "add":
        for repeat in range(repeatRange):
            heap.add(random.randrange(0, 100000))
    elif action == "remove":
        for repeat in range(repeatRange):
            print(heap.getAndRemoveSmallest())


def benchmarkHeapImplementation(heapImplementation):
    runTimes = []
    testRange = 10
    for test in range(testRange):
        start = time.clock()

        executeQueries(heapImplementation)

        end = time.clock()
        runTimes.append(end - start)

    print(round(sum(runTimes) / testRange, 6))


def executeQueries(h):
    modifyHeap(h, random.randrange(10000, 20000), "add")
    modifyHeap(h, random.randrange(1000, 2000), "remove")
    modifyHeap(h, random.randrange(10000, 20000), "add")
    modifyHeap(h, random.randrange(10000, 20000), "add")
    modifyHeap(h, random.randrange(1000, 2000), "remove")
    modifyHeap(h, random.randrange(10000, 20000), "add")
    modifyHeap(h, random.randrange(1000, 2000), "remove")
    modifyHeap(h, random.randrange(1000, 2000), "remove")
    modifyHeap(h, random.randrange(10000, 20000), "add")
    modifyHeap(h, random.randrange(1000, 2000), "remove")

    print(h.heapList)


def main():
    benchmarkHeapImplementation(BinaryTreeInArrayBasedHeap.BinaryTreeInArrayBasedHeap([random.randrange(0, 100) for _ in range(10)]))

    # Results when run 10 times:
    #   SimpleArrayBasedHeap: 2.062203
    #   BinaryTreeInArrayBasedHeap: 1.40439

if __name__ == '__main__':
    main()