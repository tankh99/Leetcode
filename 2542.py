# https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
import heapq

"""
Rationale behind this solution is 
1. We ensure that nums 2 is monotonically decreasing. Meaning it's sorted in descending order
2. Because of this property, when we sum up, numbers from nums1, we can test for the maximum score by multiplying the sum with the current number in nums2
3. Then we compare it against the max score we have so far

Why we can't do it without sorting is because 
1. getting the kth minimum from nums2 would be a whole lot more complicated
2. There's probably another reason...


Note: This solution was adapted from another's solution
"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sum = 0
        heap = []
        maxSum = 0
        for a, b in sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True):
            # print(a, b)
            sum += a
            heapq.heappush(heap, a)
            if len(heap) == k:
                maxSum = max(maxSum, sum * b)
                sum -= heapq.heappop(heap)

        return maxSum

sln = Solution()
ans = sln.maxScore([1,3,3,2], [2,1,3,4], 3) # 
ans = sln.maxScore([4,2,3,1,1], [7,5,10,9,6], 1) # 
ans = sln.maxScore([100,200,500], [3,2,1], 2) # 
print(ans)
