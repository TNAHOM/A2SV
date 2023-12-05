class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == sum(nums):
            return len(nums)

        output = 0

        for left in range(len(nums)):
            right = left

            while right < len(nums) and nums[left] == 1 and nums[right] == 1:
                right+=1
            
            temp = right - left
            output = max(temp, output)
            
            if right == len(nums):
                return output
        
        return output