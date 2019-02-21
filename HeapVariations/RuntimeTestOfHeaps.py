import IHeap
import BinaryTreeInArrayBasedHeap
import SimpleArrayBasedHeap

import random
import time


def modifyHeap(heap, action):
    if action == "add":
        for repeat in range(15000):
            heap.add(random.randrange(0, 100000))
    elif action == "remove":
        for repeat in range(1500):
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
    modifyHeap(h, "add")
    modifyHeap(h, "remove")
    modifyHeap(h, "add")
    modifyHeap(h, "add")
    modifyHeap(h, "remove")
    modifyHeap(h, "add")
    modifyHeap(h, "remove")
    modifyHeap(h, "remove")
    modifyHeap(h, "add")
    modifyHeap(h, "remove")

    print(h.heapList)


def main():
    benchmarkHeapImplementation(SimpleArrayBasedHeap.SimpleArrayBasedHeap([random.randrange(0, 100) for _ in range(10)]))

    # Results when run 10 times:
    #   SimpleArrayBasedHeap: 4.410261s
    #   BinaryTreeInArrayBasedHeap: 1.394079s

if __name__ == '__main__':
    main()