class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []

        for x in range(n):
            output.append(nums[x])
            output.append(nums[x+n])

        return output