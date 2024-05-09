# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75

from typing import List

INF = 1000000000

class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = [(*entrance, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True

        while len(queue) > 0:
            i, j, level = queue.pop(0)

            if (i in {0, m - 1} or j in {0, n - 1}) and [i, j] != entrance:
                # Level represents the shortest distance from the entrance
                return level

            for x, y in directions:
                x, y = i + x, j + y

                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and maze[x][y] == ".":
                    visited[x][y] = True
                    queue.append((x, y, level + 1))


        return -1

    # def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    #     queue = []
    #     m, n = len(maze), len(maze[0])
    #     visited = [[False] * n for _ in range(m)]
    #     visited[entrance[0]][entrance[1]] = True
    #     queue.append(entrance)
    #     # print(self.possibleMoves(maze, entrance))
    #     possibleExits = []
    #     while len(queue) > 0:
    #         currPos = queue.pop(0)
    #         x, y = currPos
    #         if self.isExit(maze, x, y):
    #             possibleExits.append(currPos)
    #             continue
    #         if visited[x][y]:
    #             continue
    #         visited[x][y] = True
    #         possibleMoves = self.possibleMoves(maze, currPos)
    #         for move in possibleMoves:
    #             queue.append(move)
            
    #     min = INF
    #     for exit in possibleExits:
    #         distance = self.manhattanDistance(m, n, entrance, exit)
    #         if distance < min:
    #             min = distance


    #     return min if min != INF else -1

    # def manhattanDistance(self, m, n, start, end):
    #     startX, startY = start
    #     endX, endY = end

    #     if startX < 0:
    #         startX += 1
    #     if startX >= m:
    #         startX -= 1
    #     if startY < 0:
    #         startY += 1
    #     if startY >= n:
    #         startY -= 1

    #     if endX < 0:
    #         endX += 1
    #     if endX >= m:
    #         endX -= 1
    #     if endY < 0:
    #         endY += 1
    #     if endY >= n:
    #         endY -= 1

    #     distance = abs(startX - endX) + abs(startY - endY)
    #     return distance

    # def isExit(self, maze, newX, newY):
    #     m, n = len(maze), len(maze[0])
        
    #     if newX < 0 or newX >= m or newY < 0 or newY >= n:
    #         return True
    #     return False

    # def possibleMoves(self, maze, currPos):
    #     x, y = currPos
    #     m, n = len(maze), len(maze[0])
    #     pos = maze[x][y]
    #     dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    #     possibleMoves = []
    #     for dir in dirs:
    #         newX, newY = x + dir[0], y + dir[1]
    #         if self.isExit(maze, newX, newY):
    #             possibleMoves.append((newX, newY))
    #         else:
    #             newPos = maze[newX][newY]
    #             if newPos == ".":
    #                 possibleMoves.append((newX, newY))

    #     return possibleMoves


sln = Solution()

ans = sln.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1, 0])
print(ans)