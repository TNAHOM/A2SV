# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dict = defaultdict(list)
        self.output = []
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def levelorder(root, count):
            if not root:
                return
            self.dict[count].append(root.val)
            levelorder(root.left, count+1)
            levelorder(root.right, count+1)
        levelorder(root, 0)

        for key, val in self.dict.items():
            if key%2 == 0:
                self.output.append(val)
            else:
                self.output.append(val[::-1])
        return self.output