class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        output = []

        for x in range(len(nums)):
            right = total - left - nums[x]
            right_size = len(nums) - x - 1

            operation = ((nums[x] * x) - left) + (right - right_size * nums[x])

            left+=nums[x]
            output.append(operation)

        return output 