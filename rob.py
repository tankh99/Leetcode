# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        return self.helper(nums, n - 1, memo)
    
    def helper(self, nums, i, memo):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        result = max(self.helper(nums, i-1, memo), self.helper(nums, i-2, memo) + nums[i])
        memo[i] = result
        # print(memo)
        return result



sln = Solution()
# ans = sln.rob([2,7,9,3,1])
# print(ans)
# ans = sln.rob([2,10,9,3,5])
# print(ans)
ans = sln.rob([2,1,1,2])
print(ans)