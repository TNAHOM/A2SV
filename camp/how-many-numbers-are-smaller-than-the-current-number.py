class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sort = sorted(nums)
        mapping = {}
        result = []

        for x in range(len(nums_sort)):
            if nums_sort[x] not in mapping:
                mapping[nums_sort[x]] = x
        
        for y in range(len(nums)):
            result.append(mapping[nums[y]])
        
        return result
       