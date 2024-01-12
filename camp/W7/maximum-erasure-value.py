class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = set()
        output = 0
        l = 0
        r = 0
        add = 0

        while r < len(nums):
            if nums[r] in dic:
                add-=nums[l]
                dic.remove(nums[l])
                l+=1
            else:
                add+=nums[r]
                dic.add(nums[r])
                r+=1
            if add > output:
                output = add
            
        return output