# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans_left = []
        ans_right = []
        def mirror(root, place):
            if not root:
                if place == 'right':
                    ans_right.append('A')
                else:
                    ans_left.append('A')
                return

            if place == 'right':
                ans_right.append(root.val)
                mirror(root.left, 'right')
                mirror(root.right, 'right')
            else:
                ans_left.append(root.val)
                mirror(root.right, 'left')
                mirror(root.left, 'left')
            return root.val
        
        mirror(root.right, 'right')
        mirror(root.left, 'left')
        return ans_left==ans_right