# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorder(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr
        def delete(root, key):
            if not root:
                return
            if root.val > key:
                root.left = delete(root.left, key)
            elif root.val < key:
                root.right = delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                temp = inorder(root.right)
                root.val = temp.val
            
                root.right = delete(root.right, temp.val)
            return root

        return delete(root, key)