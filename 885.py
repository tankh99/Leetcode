from typing import List
from collections import deque
import time

class Solution:

    def inbound(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        left, right = cStart, cStart + 1
        up, down = rStart, rStart + 1
        current = 1
        move = 0
        while current <= rows * cols:
            print(left, right, up, down, move)
            for i in range(left + move, right + 1):
                if self.inbound(up, i, rows, cols):
                    ans.append([up, i])
                    current += 1
            left -= 1
            for i in range(up + 1, down + 1):
                if self.inbound(i, right, rows, cols):
                    ans.append([i, right])
                    current += 1
            up -= 1
            for i in range(right - 1, left - 1, -1):
                if self.inbound(down, i, rows, cols):
                    ans.append(down,i)
                    current += 1

            right += 1

            for i in range(down - 1, up-1, -1):
                if self.inbound(i, left, rows, cols):
                    ans.append([i, left])
                    current += 1

            down += 1
            move = 1
        return ans

    # def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    #     n, m = rows, cols
    #     dirs = [(0,1), (1,0),(0,-1),(-1,0)]
    #     seen = [[False for _ in range(m)] for _ in range(n)]

    #     def isVisitable(r, c):
    #         return 0 <= r < n and 0 <= c < m and not seen[r][c]

    #     def checkIfCanGoIn(dirIndex, r, c):
    #         dir = dirs[dirIndex]
    #         if dir == (0,1) and isVisitable(r+1, c): # Right dir = Grid is below
    #             return (r-1, c)
    #         if dir == (1,0) and isVisitable(r, c-1): # Down dir = Grid is left
    #             return (r, c-1)
    #         if dir == (0,-1) and isVisitable(r-1, c): # Left dir = Grid is up
    #             return (r+1, c)
    #         if dir == (-1,0) and isVisitable(r, c+1): # Up dir = Grid is right
    #             return (r, c+1)
    #         return None
        
    #     q = deque()
    #     seenCount = 0
    #     q.append((rStart, cStart))
    #     dirIndex = 0
    #     total = n * m
    #     ans = []

    #     '''
    #     1. Width expands by 1 each time direction changes TWICE
    #     2. Travelled distance increases by 1 each iteration
    #     '''
    #     width = 1
    #     travelled_dist = 0

    #     def change_dir(dirIndex, r, c):
    #         dirIndex = dirIndex + 1
    #         dirIndex = dirIndex % len(dirs)
    #         newDir = dirs[dirIndex]
    #         newR, newC = r + newDir[0], c + newDir[1]
    #         # print("changin dir", dirIndex, newR, newC)
    #         return dirIndex, newR, newC
        
    #     times_switched = 0
    #     oob = False

    #     while q:
    #         r, c = q.popleft()
    #         dir = dirs[dirIndex]

    #         if not isVisitable(r,c):
    #             time.sleep(0.1)
    #             newR, newC = r + dir[0], c + dir[1]
    #             if (dir == (0,1) and newC > m) or (dir == (1,0) and newR > n) or (dir == (0,-1) and newC < -1) or (dir == (-1,0) and newR < -1):
    #                 dirIndex, newR, newC = change_dir(dirIndex, r, c)
    #             newDir = checkIfCanGoIn(dirIndex, r, c)
    #             print(r,c, newDir)
    #             if newDir is not None:
    #                 newR, newC = newDir
    #                 q.append((newR, newC))
    #                 oob = False
    #                 continue
    #             # print(newR, newC)
    #             q.append((newR, newC))
    #         else:
    #             oob = False
    #             seen[r][c] = True
    #             seenCount += 1


    #             ans.append([r,c])

    #             newR, newC = r + dir[0], c + dir[1]
                
    #             hit_dist_limit = travelled_dist == width
    #             # print(travelled_dist, width)
    #             if hit_dist_limit:
    #                 travelled_dist = 0
    #                 times_switched += 1
    #                 if times_switched % 2 == 0:
    #                     width += 1
    #                 dirIndex, newR, newC = change_dir(dirIndex, r, c)

    #             elif not isVisitable(newR, newC):
    #                 print("unvisitable", newR, newC)
    #                 q.append((newR, newC))
    #                 oob = True
    #                 # dirIndex, newR, newC = change_dir(dirIndex, r, c)
                    


    #             # if not seen[newR][newC]:
    #             q.append((newR, newC))
    #             if isVisitable(newR, newC):
    #                 travelled_dist += 1
    #     return ans
        
sln = Solution()
ans = sln.spiralMatrixIII(1, 4, 0, 0)

print(ans)