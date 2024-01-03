class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        output = 0
        nums.sort()
        l = 0
        r = len(nums)-1

        while l<r:
            if (nums[l] + nums[r]) < target:
                output+=r-l
                l+=1
            else:
                r-=1

        return output