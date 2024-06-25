# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dp(node):
            if node is None:
                return 0
            
            sum = node.val + max(dp(node.left), dp(node.right))
            return sum
            
        return dp(root)