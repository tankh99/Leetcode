import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxSoFar = nums[0]
        pre = post = 1
        for i in range(n):
            if pre == 0: pre = 1
            if post == 0: post = 1
            pre *= nums[i]
            post *= nums[n-i-1]
            maxSoFar = max(maxSoFar, max(pre, post))
        
        return maxSoFar
    
sln = Solution()

# ans = sln.maxProduct([2,-5,-2,-4,3])
ans = sln.maxProduct([50,-3,5,-4,3,-5])
# ans = sln.maxProduct([-4,-3])
# ans = sln.maxProduct([2,3,-2,4])
# ans = sln.maxProduct([50,-3,5,3])
# ans = sln.maxProduct([0,2])
print(ans)