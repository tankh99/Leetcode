# https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=study-plan-v2&envId=leetcode-75
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.min = 1
        self.heap = []

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        smallest = self.min
        self.min += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.min and num not in self.heap:
            heapq.heappush(self.heap, num)
        


# Fail. Solution taken from: https://www.youtube.com/watch?v=JQk_nKL-8eA