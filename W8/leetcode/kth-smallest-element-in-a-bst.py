# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.smallest = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def smallest(root):
            if not root:
                return
            left = smallest(root.left)
            self.smallest.append(root.val)
            right = smallest(root.right)
            
            return root
        smallest(root)

        return sorted(self.smallest)[k-1]