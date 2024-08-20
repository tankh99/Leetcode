from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        s = (total_sum + target) // 2
        dp = [0 for _ in range(s + 1)]
        dp[0] = 1 # 1 way to choose no elements
        # print(dp)
        for num in nums:
            for i in range(s, num-1, -1):
                dp[i] += dp[i-num]
        return dp[s]

sln = Solution()
print(sln.findTargetSumWays([1,1,1,1,1], 3))
print(sln.findTargetSumWays([2,3,3,4,2,6], 6))
print(sln.findTargetSumWays([1], 2))