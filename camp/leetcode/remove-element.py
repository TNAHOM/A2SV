class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = 0
        
        for x in range(len(nums)):
            if nums[x] != val:
                nums[l] = nums[x]
                l+=1
                # print(nums)

        print(l)
        return l
        