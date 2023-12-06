class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        output = []
        while l < len(nums)-1:
            for r in range(nums[l]):
                output.append(nums[l+1])
            l+=2
        
        return output
