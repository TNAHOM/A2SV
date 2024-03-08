# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(max_, arr):
            # print(arr)
            if len(arr) == 0:
                return None
            max_n = max(arr)
            ind = arr.index(max_n)

            left = helper(max_n, arr[:ind])
            right = helper(max_n, arr[ind+1:])

            return TreeNode(max_n, left, right)
        
        
        return helper(0, nums)