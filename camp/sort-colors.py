class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        len_arr = len(nums)-1
        sort = False

        while not sort:
            sort = True
            for x in range(len_arr):
                if nums[x] > nums[x+1]:
                    nums[x], nums[x+1] = nums[x+1], nums[x]
                    sort = False
        return nums
