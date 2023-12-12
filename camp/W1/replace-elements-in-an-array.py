class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dic = {}
        for x in range(len(nums)):
            dic[nums[x]] = x

        for y, z in operations:
            ind = dic[y]

            nums[ind] = z
            dic[z] = ind
        return nums