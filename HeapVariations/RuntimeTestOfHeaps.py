import IHeap
from BinaryTreeInArrayBasedHeap import BinaryTreeInArrayBasedHeap
from SimpleArrayBasedHeap import SimpleArrayBasedHeap

import random
import time


INITIAL_ELEMENTS_LIST = [random.randrange(0, 100) for _ in range(10)]
TEST_RANGE = 10
NUM_DIGITS_AFTER_DECIMAL_POINT = 4


def modifyHeap(heap, action):
    if action == "add":
        for repeat in range(15000):
            heap.add(random.randrange(0, 100000))
    elif action == "remove":
        for repeat in range(1500):
            heap.getAndRemoveSmallest()


def benchmarkHeapImplementation(heapImplementation):
    runTimes = []
    for test in range(TEST_RANGE):
        start = time.clock()

        executeQueries(heapImplementation)

        end = time.clock()
        runTimes.append(end - start)

    print(round(sum(runTimes) / TEST_RANGE, NUM_DIGITS_AFTER_DECIMAL_POINT))


def executeQueries(h):
    with open("TestingActions.txt") as ta:
        for action in ta:
            modifyHeap(h, action.strip())


def main():
    benchmarkHeapImplementation(SimpleArrayBasedHeap(INITIAL_ELEMENTS_LIST))


if __name__ == '__main__':
    main()