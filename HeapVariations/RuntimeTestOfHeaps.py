import IHeap
from BinaryTreeInArrayBasedHeap import BinaryTreeInArrayBasedHeap
from SimpleArrayBasedHeap import SimpleArrayBasedHeap
from BinaryTreeWithNodesBasedHeap import BinaryTreeWithNodesBasedHeap
from DefaultPythonHeap import DefaultPythonHeap


from typing import List
import random
import time


INITIAL_ELEMENTS_NUM: int = 10
INITIAL_ELEMENTS_VALUES_RANGE: int = 100
ADD_ELEMENTS_REPEAT_NUM: int = 15000
REMOVE_ELEMENTS_REPEAT_NUM: int = 1500

NUM_TEST_ITERATIONS: int = 20
NUM_DIGITS_AFTER_DECIMAL_POINT: int = 4


def modifyHeap(heap: IHeap, action: str) -> None:
    if action == "add":
        for repeat in range(ADD_ELEMENTS_REPEAT_NUM):
            heap.add(random.randrange(0, 100000))
    elif action == "remove":
        for repeat in range(REMOVE_ELEMENTS_REPEAT_NUM):
            heap.getAndRemoveSmallest()


def benchmarkHeapImplementation(heapImplementation: IHeap) -> None:
    runTimes: List = []
    for test in range(NUM_TEST_ITERATIONS):
        start: float = time.clock()

        executeQueries(heapImplementation)

        end: float = time.clock()
        runTimes.append(end - start)

    print(round(sum(runTimes) / NUM_TEST_ITERATIONS, NUM_DIGITS_AFTER_DECIMAL_POINT))


def executeQueries(h: IHeap) -> None:
    with open("TestingActions.txt") as ta:
        for action in ta:
            modifyHeap(h, action.strip())


def main():
    initialElements: List = [random.randrange(INITIAL_ELEMENTS_VALUES_RANGE) for _ in range(INITIAL_ELEMENTS_NUM)]
    benchmarkHeapImplementation(SimpleArrayBasedHeap(initialElements))  # 11.211
    benchmarkHeapImplementation(BinaryTreeInArrayBasedHeap(initialElements))  # 1.2617
    benchmarkHeapImplementation(BinaryTreeWithNodesBasedHeap(initialElements))  # 3.1434 -> 5.914
    benchmarkHeapImplementation(DefaultPythonHeap(initialElements))  # 0.772


if __name__ == '__main__':
    main()
