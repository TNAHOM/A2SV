class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for ind, x in enumerate(nums):
            step = max(step, x+ind)
            if step == ind and len(nums)-1 != ind:
                return False

        return True