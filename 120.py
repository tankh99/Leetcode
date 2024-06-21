from typing import List
from collections import defaultdict
class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    
    n = len(triangle)
    # max_len = len(triangle[-1])
    mapped = [[-1] * n for _ in range(n)]
    def dp(row, col):
      if row >= n - 1: # 1 >= 1
        return triangle[row][col]

      # if (row,col) in mapped:
      if mapped[row][col] != -1:
          return mapped[row][col]
        
      totalSum = triangle[row][col] + min(dp(row+1, col), dp(row+1, col+1))
      # mapped[(row, col)] = totalSum
      mapped[row][col] = totalSum
      return mapped[row][col]

    return dp(0,0)
  
sln = Solution()
ans = sln.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(ans)