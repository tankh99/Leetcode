from typing import List
from collections import defaultdict

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        dp[0] = 1


        for coin in coins:
            # Update the DP array from the value of the coin to the target amount
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if coin < i: continue
        #         for j in range(coin, amount + 1):
        #             dp[i] += dp[i - coin]

        ans = dp[amount]
        print(dp)
        return ans
sln = Solution()
sln.change(13, [3,7])