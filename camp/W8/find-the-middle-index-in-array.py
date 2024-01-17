class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        curr = 0

        for x in range(len(nums)):
            temp = tot-nums[x]
            if temp/2 == curr:
                return x
            curr+=nums[x]
        return -1
