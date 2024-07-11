from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        best = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
                    
        for num in dp:
            best = max(num, best)
        return best
    
sln = Solution()
# ans = sln.lengthOfLIS([10,9,2,5,3,7,101,18])
# ans = sln.lengthOfLIS([2,8,10,3,6,9])
ans = sln.lengthOfLIS([0,1,0,3,2,3])
print(ans)