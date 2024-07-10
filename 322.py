from typing import List
import math
from collections import defaultdict

INF = 10000000

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Tabulation
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
                
        return dp[amount] if dp[amount] != float("inf") else -1
        
        # Memoization
        # memo = defaultdict(lambda:-2)
        # def helper(amount):
        #     if amount == 0: return 0
        #     if amount < 0: return -1
        #     if memo[amount] != -2: return memo[amount]
            
        #     minCoins = INF
        #     for coin in coins:
        #         res = helper(amount - coin)
        #         if res >= 0: minCoins = min(minCoins, res + 1)
                
        #     memo[amount] = minCoins if minCoins != INF else -1
        #     return memo[amount]
            
        # return helper(amount)
        
        # Recursion
        # def helper(current, steps):
        #     nonlocal best
            
        #     if current > amount:
        #         return INF

        #     if current == amount:
        #         best = min(best, steps)
                
        #         memo[current] = steps
        #         return best
                
        #     for coin in coins:    
        #         if coin != 0:
        #             memo[current] = min(helper(current + coin, steps + 1), memo[current])
                    
        #     return memo[current]
            
        # helper(0, 0)
        # return best if best != INF else -1
        
            
sln = Solution()
# ans = sln.coinChange([3,5], 11)
# ans = sln.coinChange([0,1,2,3], 11)
# ans = sln.coinChange([0,1,2,5], 100)
ans = sln.coinChange([0,1, 2], 100)
# ans = sln.coinChange([2], 1)
print(ans)
        
            