class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]
            r+=1
        print(l)
        return l+1