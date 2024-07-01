# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSoFar = -math.inf
        def dp(node):
            if node is None:
                return -math.inf
            leftSum = dp(node.left)
            rightSum = dp(node.right)
            partOfPathSum = node.val + max(leftSum, rightSum)
            closedSum = node.val + leftSum + rightSum
            self.maxSoFar = max(self.maxSoFar, leftSum, rightSum, node.val, partOfPathSum, closedSum)
            return max(partOfPathSum, node.val)
        dp(root)
        return self.maxSoFar