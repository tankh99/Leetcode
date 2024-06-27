# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkNodesEqual(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            
            if root.val != subRoot.val:
                return False
            leftEquals = checkNodesEqual(root.left, subRoot.left)
            rightEquals = checkNodesEqual(root.right, subRoot.right)
            return leftEquals and rightEquals
            
        if root is None:
            return False
        if checkNodesEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)