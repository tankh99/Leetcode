from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        nums = set(nums)
        for i, num in enumerate(nums):
            map[num] = i

        best = 0
        for i, num1 in enumerate(nums):
            num = num1
            runningcount = 1
            if num - 1 not in map:
                while num in map:
                    num += 1
                    best = max(runningcount, best)
                    runningcount += 1
            
            # for j, num2 in numera
        return best