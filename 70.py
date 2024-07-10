class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i):
            if i < 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 2
            elif i in memo:
                return memo[i]
            ans = helper(i - 1) + helper(i - 2)
            memo[i] = ans
            return memo[i]
            
        return helper(n)
    
sln = Solution()
ans = sln.climbStairs(4)
print(ans)