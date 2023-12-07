class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for y in range(0, len(nums)+1):
            if y not in nums:
                return y