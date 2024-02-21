class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        output = 0
        tot = 0

        for x in range(len(nums)):
            tot+=nums[x]
            output = max(output, ceil(tot/(x+1)))

        return output