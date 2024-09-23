"""Heaps and Priority Queues"""

import heapq
from typing import List


def challenge1():
    """pass"""

    def heap_push(heap: List[int], value: int) -> int:
        heapq.heappush(heap, value)
        return heap[0]

    # do not modify below this line
    print(heap_push([1, 2, 3], 4))  # 1
    print(heap_push([1, 2, 3], 0))  # 0
    print(heap_push([1, 2, 3], 2))  # 1
    print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))  # 2
    print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))  # 4


def challenge2():
    """pass"""

    def heap_pop(heap: List[int]):
        return [heapq.heappop(heap) for i in range(len(heap))]

    # do not modify below this line
    print(heap_pop([1, 2, 3]))
    print(heap_pop([1, 3, 2]))
    print(heap_pop([6, 7, 8, 12, 9, 10]))
    # EXPECTED OUTPUT:
    # [1, 2, 3]
    # [1, 2, 3]
    # [6, 7, 8, 9, 10, 12]


def challenge3():
    """pass"""

    def heapify_strings(strings: List[str]) -> List[str]:
        heapq.heapify(strings)
        return strings

    def heapify_integers(integers: List[int]) -> List[int]:
        heapq.heapify(integers)
        return integers

    def heap_sort(nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        return sorted(nums)

    # do not modify below this line
    print(heapify_strings(["b", "a", "e", "c", "d"]))
    print(heapify_integers([3, 4, 5, 1, 2, 6]))
    print(heap_sort([3, 4, 5, 1, 2, 6]))
    # EXPECTED OUTPUT:
    # ['a', 'b', 'e', 'c', 'd']
    # [1, 2, 5, 4, 3, 6]
    # [1, 2, 3, 4, 5, 6]


def challenge4():
    """pass"""

    def get_reverse_sorted(nums: List[int]) -> List[int]:
        nums_heap = []
        for num in nums:
            heapq.heappush(nums_heap, -num)
        max_heap = []
        while nums_heap:
            max_heap.append(-heapq.heappop(nums_heap))
        return max_heap

    # do not modify below this line
    print(get_reverse_sorted([1, 2, 3]))
    print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
    print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
    # EXPECTED OUTPUT:
    # [3, 2, 1]
    # [7, 6, 5, 4, 3, 2, 1]
    # [7, 6, 5, 4, 2, -1, -3, -4]


def challenge5():
    """pass"""

    def get_reverse_sorted(nums: List[int]) -> List[int]:
        max_heap = []
        for num in nums:
            pair = (-num, num)
            heapq.heappush(max_heap, pair)
        max_hp = []
        while max_heap:
            pair = heapq.heappop(max_heap)
            max_hp.append(pair[1])
        return max_hp

    # do not modify below this line
    print(get_reverse_sorted([1, 2, 3]))
    print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
    print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
    # EXPECTED OUTPUT
    # [3, 2, 1]
    # [7, 6, 5, 4, 3, 2, 1]
    # [7, 6, 5, 4, 2, -1, -3, -4]


def challenge6():
    """pass"""


def challenge7():
    """pass"""


print("\nChallenge 1: ")
challenge1()
print("\nChallenge 2: ")
challenge2()
print("\nChallenge 3: ")
challenge3()
print("\nChallenge 4: ")
challenge4()
print("\nChallenge 5: ")
challenge5()
print("\nChallenge 6: ")
challenge6()
print("\nChallenge 7: ")
challenge7()
