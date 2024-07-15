from typing import List
from collections import deque

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        target = n * n
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        n, m = len(matrix), len(matrix[0])
        dirs = [(0,1), (1,0),(0,-1),(-1,0)]

        seen = [[False for _ in range(m)] for _ in range(n)]
        
        def isVisitable(r, c):
            return 0 <= r < n and 0 <= c < m and not seen[r][c]

        q = deque()
        q.append((0,0, 1))
        dirIndex = 0
        for i in range(target):
            r, c, val = q.popleft()
            seen[r][c] = True
            matrix[r][c] = val
            
            dir = dirs[dirIndex]
            newR, newC = r + dir[0], c + dir[1]
            if not isVisitable(newR, newC):  
                dirIndex += 1
                dirIndex = dirIndex % len(dirs)
                newDir = dirs[dirIndex]
                newR, newC = r + newDir[0], c + newDir[1]

            q.append((newR, newC, val + 1))
            # for row in range(n):
            #     for col in range(n):
            #         remaining_cols = n - col + 1
            #         remaining_rows = n - row + 1
            #         num = matrix
        # print(matrix)
        return matrix
    
sln = Solution()
sln.generateMatrix(3)