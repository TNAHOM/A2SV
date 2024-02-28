# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # print(root.val)
        # print(root.right.val)
        ans = [root.val] if root else []
        def order(root):
            if not root:
                # ans.append('null')

                return
            

            if root.left:
                ans.append(root.left.val)
                order(root.left)
            if root.right:
                ans.append(root.right.val)
                order(root.right)
            return root.val
        order(root)
        return  ans