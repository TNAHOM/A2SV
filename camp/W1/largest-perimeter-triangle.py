class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        output = 0
        l = 0

        while l < len(nums)-2:
            side_12 = sum(nums[l:l+2])
            if side_12 > nums[l+2]:
                output = max(sum(nums[l:l+3]), output)

            l+=1
        
        return output