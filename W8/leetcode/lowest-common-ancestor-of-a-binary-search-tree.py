# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev_p = False
        self.prev_q = False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def ancestor(root, p, q):
            if not root:
                return

            if root.val == p or root.val == q:
                return root

            left = ancestor(root.left, p, q)
            right = ancestor(root.right, p, q)

            if left and right:
                return root
            else:
                if left:
                    return left
                elif right:
                    return right
                else:
                    return 
                
        
        return ancestor(root, p.val, q.val)