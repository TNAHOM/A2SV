class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        min_ = float('inf')
        output = float('-inf')

        for x in range(len(nums)):
            min_ = min(min_, prefix[-1])
            prefix.append(prefix[-1]+nums[x])
            output = max(output, prefix[-1]-min_)

        # print(prefix)  

        return output