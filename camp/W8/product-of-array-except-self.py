class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = []
        output= []

        curr = 1
        for x in nums:
            curr*=x
            prefix.append(curr)
        curr = 1
        for x in range(len(nums)-1, -1, -1):
            # curr*=x
            # suffix.append(curr)
            temp = prefix[x] * curr
            output.append(temp)
            curr *= nums[x]

        print(prefix, suffix)
        return output[::-1]
