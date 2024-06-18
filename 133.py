from collections import deque
"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        cloned_nodes = {}
        def dfs(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            clone = Node(node.val) 
            cloned_nodes[node] = clone
            
            for nbr in node.neighbors:
                clone.neighbors.append(dfs(nbr))
                
            return clone
        return dfs(node)
        # if not node:
        #     return None
        # map = {}
        # q = deque()
        # q.append(node)
        
        # newRoot = Node(node.val)
        # map[node.val] = newRoot
        # while q:
        #     curr = q.popleft()
        #     for nbr in curr.neighbors:
        #         if nbr.val not in map:
        #             map[nbr.val] = Node(nbr.val)
        #             q.append(nbr)
        #         map[curr.val].neighbors.append(map[nbr.val])
        # return newRoot

        