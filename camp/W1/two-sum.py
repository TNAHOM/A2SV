class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for x in range(len(nums)):
            sub = target-nums[x]
            if nums[x] in dic:
                return [dic[nums[x]], x]
            
            dic[sub] = x
