from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numOfPaths = 0
        self.dfs(root, targetSum, 0)
        return self.numOfPaths

    def dfs(self, node, targetSum):
        if not node:
            return
        if node.val == targetSum:
            self.numOfPaths += 1
        self.dfs(node.left, targetSum - node.val)
        self.dfs(node.right, targetSum - node.val)

    # def pathSumFrom(node: TreeNode, targetSum: int, accumSum: int) -> int:
    #     if not node:
    #         return accumSum
    #     # Simple lock mechanism to prevent summing up just a single node
    #     if accumSum is None:
    #         accumSum = node.val
    #     else:
    #         accumSum += node.val
    #         if node.val + accumSum >= targetSum:
    #             count += 1
            
    #     return pathSumFrom(node.left, targetSum, accumSum) + pathSumFrom(node.left, targetSum, accumSum)


sln = Solution()

