class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        double_num = nums + [0]*len(nums)
        for x in range(len(nums), len(double_num)):
            double_num[x] = nums[x-len(nums)]
        
        return double_num