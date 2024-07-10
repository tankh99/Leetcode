from typing import List
import math
from collections import defaultdict

INF = 10000000

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        n = len(coins)
        
        memo = defaultdict(int)
        
        best = INF
        
        def helper(current, steps):
            nonlocal best
            
            if current > amount:
                return INF

            if current == amount:
                best = min(best, steps)
                
                memo[current] = steps
                return best
                
            for coin in coins:    
                if coin != 0:
                    memo[current] = min(helper(current + coin, steps + 1), memo[current])
                    
            return memo[current]
            
        helper(0, 0)
        return best if best != INF else -1
        
            
sln = Solution()
# ans = sln.coinChange([3,5], 11)
# ans = sln.coinChange([0,1,2,3], 11)
# ans = sln.coinChange([0,1,2,5], 100)
ans = sln.coinChange([0,1, 2], 100)
# ans = sln.coinChange([2], 1)
print(ans)
        
            