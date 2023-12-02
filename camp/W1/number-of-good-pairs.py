class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pair = 0

        for l in range(len(nums)):
            r = l+1
            while r < len(nums):
                if nums[l] == nums[r]:
                    good_pair+=1
                r+=1
        
        return good_pair