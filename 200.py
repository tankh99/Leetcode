from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.traverse(grid, visited, i, j)
                    islands += 1

        return islands
    
    def traverse(self, grid, visited, i, j):
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = []
        queue.append((i, j))
        while len(queue) > 0:
            curr = queue.pop(0)
            if visited[curr[0]][curr[1]]:
                continue
            visited[curr[0]][curr[1]] = True
            for dir in dirs:
                newDir = tuple(map(lambda x, y: x + y, curr, dir))
                if self.withinBounds(grid, newDir) and grid[newDir[0]][newDir[1]] == "1":
                    queue.append(newDir)

    def withinBounds(self, grid, coord):
        n, m = len(grid), len(grid[0])
        i, j = coord
        return i >= 0 and i < n and j >= 0 and j < m

sln = Solution()
sln = sln.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
print(f"answer {sln}")