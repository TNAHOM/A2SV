# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tot = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def root_leaf(root, val):
            if not root:
                return
            if not root.left and not root.right:
                val = val+str(root.val)
                self.tot+=int(val)
                return

            val = val+str(root.val)
            left = root_leaf(root.left, val)
            right = root_leaf(root.right, val)
            
            # print(val)
            return root

        root_leaf(root, '')
        return self.tot