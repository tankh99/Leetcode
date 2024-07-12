from collections import deque
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      n, m = len(matrix), len(matrix[0])
      dirs = [(0,1), (1,0),(0,-1),(-1,0)]
      ans = []

      seen = [[False for _ in range(m)] for _ in range(n)]

      
      total = n * m
      start = (0,0)

      def isVisitable(r, c):
        return 0 <= r < n and 0 <= c < m and not seen[r][c]

      
      q = deque()
      q.append((0,0))
      dirIndex = 0
      for i in range(total):
        r, c = q.popleft()
        seen[r][c] = True
        ans.append(matrix[r][c])
        
        dir = dirs[dirIndex]
        newR, newC = r + dir[0], c + dir[1]
        if not isVisitable(newR, newC):  
          dirIndex += 1
          dirIndex = dirIndex % len(dirs)
          newDir = dirs[dirIndex]
          newR, newC = r + newDir[0], c + newDir[1]

        q.append((newR, newC))

      return ans
      