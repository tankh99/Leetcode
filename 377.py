from typing import List


class Solution:
    
    def __init__(self):
        self.combinations = []
        
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if num <= i: 
                    dp[i] += dp[i - num]
        
        return dp[-1]
        # dp = [0 * len(nums)] # Contains list of all max possible combinations for each number
        # def helper(target, path):
        #     if target == 0:
        #         self.combinations.append(path)
        #         return
        #     elif target < 0:
        #         return
            
        #     for num in nums:
        #         newPath = path + [num]
        #         helper(target - num, newPath)
                
        # helper(target, [])
        # return len(self.combinations)
            

sln = Solution()
ans = sln.combinationSum4([1,2,3], 4)
# ans = sln.combinationSum4([1,2,3], 10)
# ans = sln.combinationSum4([9], 3)
print(ans)
