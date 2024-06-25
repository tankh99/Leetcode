
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        lca = root
        while True:
            '''
            1. p < lca and q > lca (or vice versa), then return root directly
            2. p < lca and q < lca, then shift lca to left
            3.. p > lca nad q > lca, then shift lca to left
            '''
            isDivergent = (p.val <= lca.val and q.val >= lca.val) or (p.val >= lca.val and q.val <= lca.val)
            if isDivergent:
                # print(p.val, q.val, lca.val)
                return lca
            
            elif p.val < lca.val and q.val < lca.val:
                lca = lca.left
            else:
                lca = lca.right
        
