import IHeap
from BinaryTreeInArrayBasedHeap import BinaryTreeInArrayBasedHeap
from SimpleArrayBasedHeap import SimpleArrayBasedHeap

import random
import time


INITIAL_ELEMENTS_NUM: int = 10
INITIAL_ELEMENTS_VALUES_RANGE: int = 100
ADD_ELEMENTS_REPEAT_RANGE: int = 15000
REMOVE_ELEMENTS_REPEAT_RANGE: int = 1500

NUM_TEST_ITERATIONS: int = 10
NUM_DIGITS_AFTER_DECIMAL_POINT: int = 4


def modifyHeap(heap, action: str):
    if action == "add":
        for repeat in range(ADD_ELEMENTS_REPEAT_RANGE):
            heap.add(random.randrange(0, 100000))
    elif action == "remove":
        for repeat in range(REMOVE_ELEMENTS_REPEAT_RANGE):
            heap.getAndRemoveSmallest()


def benchmarkHeapImplementation(heapImplementation):
    runTimes = []
    for test in range(NUM_TEST_ITERATIONS):
        start = time.clock()

        executeQueries(heapImplementation)

        end = time.clock()
        runTimes.append(end - start)

    print(round(sum(runTimes) / NUM_TEST_ITERATIONS, NUM_DIGITS_AFTER_DECIMAL_POINT))


def executeQueries(h):
    with open("TestingActions.txt") as ta:
        for action in ta:
            modifyHeap(h, action.strip())


def main():
    benchmarkHeapImplementation(SimpleArrayBasedHeap([random.randrange(INITIAL_ELEMENTS_VALUES_RANGE) for _ in range(INITIAL_ELEMENTS_NUM)]))


if __name__ == '__main__':
    main()
