# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dict = defaultdict(int)
        self.max_ = 0
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def mode(root):
            if not root:
                return
            self.dict[root.val]+=1
            self.max_ = max(self.dict[root.val], self.max_)
            mode(root.left)
            mode(root.right)
            return root
        mode(root)

        output = []
        for key, val in self.dict.items():
            if val == self.max_:
                output.append(key)
        
        return output