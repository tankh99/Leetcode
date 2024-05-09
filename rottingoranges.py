# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def getOranges(self, grid):
        rotten = []
        healthy = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    rotten.append((i, j))
                elif cell == 1:
                    healthy.append((i, j))
        return healthy, rotten
    
    def orangesRotting(self, grid: List[List[int]]) -> int:    
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        healthy, rotten = self.getOranges(grid)
        if len(rotten) == 0 and len(healthy) == 0:
            return 0
        if len(rotten) == 0 and len(healthy) > 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        
        count = 0
        while len(healthy) > 0:
            
            tempRotten = rotten.copy()
            count += 1
            for rottenOrange in tempRotten:
                x, y = rottenOrange
                for i, j in directions:
                    newX, newY = x + i, y + j
                    if newX >= 0 and newX < m and newY >= 0 and newY < n:
                        cell = grid[newX][newY] 
                        if cell == 1:
                            grid[newX][newY] = 2
                
            healthy, rotten = self.getOranges(grid)
            if tempRotten == rotten:
                return -1

        return count

sln = Solution()
# ans = sln.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
ans = sln.orangesRotting([[1,2]])
# ans = sln.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
print(ans)
