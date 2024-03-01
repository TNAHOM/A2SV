# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff = None
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, maxVal, minVal):
            if not root:
                return
            max_ = max(root.val, maxVal)
            min_ = min(root.val, minVal)
            helper(root.left, max_, min_)
            helper(root.right, max_, min_)
            temp = max_ - min_
            if not self.diff or self.diff < temp:
                self.diff = temp
            # print(max_, min_)
            return max_, min_

        out = helper(root, float('-inf'), float('inf'))
        return self.diff