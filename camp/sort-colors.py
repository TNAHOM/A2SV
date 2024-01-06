class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        find = 0

        for l in range(len(nums)-1):
            for r in range(len(nums)-l-1):

                if nums[r] > nums[r+1]:
                    nums[r], nums[r+1] = nums[r+1], nums[r]
                
