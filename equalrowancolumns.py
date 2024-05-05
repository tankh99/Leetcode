# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        n = len(grid)
        for i, row in enumerate(grid):
            rows.append(row)
            col = [grid[j][i] for j in range(n)]
            cols.append(col)
        
        count = 0
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
        return count

sln = Solution()
ans = sln.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
print(ans)
# rows = set()
# rows.add([1,2,3])
# rows.add([1,2,4])
# print(list(rows))