# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []

        def check(root):
            if not root:
                return
            if root.left:
                check(root.left)
            if root:
                ans.append(root.val)
            if root.right:
                check(root.right)
            return root.val
        
        check(root)
        
        for x in range(len(ans)-1):
            if ans[x] >= ans[x+1]:
                return False
        
        return True