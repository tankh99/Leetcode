from typing import List
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        root = TrieNode()

        def insert(word):
          node = root
          for c in word:
            if c not in node.children:
              node.children[c] = TrieNode()
            node = node.children[c]
          node.isEnd = True
        
        for word in words:
           insert(word)
          
        def getNeighbours(board, r, c):
            possibleDirs = [(0,1), (0,-1), (1,0), (-1,0)]
            res = []
            for dir in possibleDirs:
                newR, newC = r + dir[0], c + dir[1]
                if 0 <= newR < n and 0 <= newC < m:
                    res.append((newR, newC))
            return res

        foundWords = set()

        def dfs(i, j, node, path):
          char = board[i][j]
          if char == "#" or char not in node.children:
             return
          node = node.children[char]
          newPath = path + char
          if node.isEnd:
            foundWords.add(newPath)
            node.isEnd = False

          # newNode = node.children[char]
          board[i][j] = "#"
          for neighbour in getNeighbours(board, i, j):
            newR, newC = neighbour
            dfs(newR, newC, node, newPath)
          board[i][j] = char

        # def bfs(i, j):
        #   q = deque()

        #   q.append(((i, j), root, ""))
        #   seen = [[False for _ in range(m)] for _ in range(n)]
        #   while len(q) > 0:
        #     (r, c), node, path = q.popleft()
        #     char = board[r][c]
        #     # if seen[r][c]:
        #     #   continue
        #     seen[r][c] = True
        #     if char in node.children:
        #       newNode = node.children[char]
        #       newPath = path + char


        #       if newNode.isEnd:
        #         foundWords.add(newPath)

        #       for neighbour in getNeighbours(board, r, c):
        #         newR, newC = neighbour
        #         q.append(((newR, newC), newNode, newPath))
        #         # if not seen[newR][newR]:
        #         #   # seen[r][c] = True
        #         #   q.append(((newR, newC), newNode, newPath))
        #         #   seen[newR][newC] = True

        
        for i in range(n):
            for j in range(m):
                dfs(i,j, root, "")


        return list(foundWords)

sln = Solution()
# ans = sln.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
ans = sln.findWords([["o","a","t", "h"]], ["oath","pea","eat","rain"])
# ans = sln.findWords([["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]], ["abc", "abcd"])
# ans = sln.findWords([["a","a"]], ["aaa"])
# ans = sln.findWords([["a"]], ["a"])
print(ans)
# (a,b), c = ((1,2), 3)
