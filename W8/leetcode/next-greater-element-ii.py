class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for _ in range(len(nums))]

        for x in range(len(nums)*2):
            while stack and nums[stack[-1] ]< nums[x%len(nums)]:
                ans[stack.pop()] = nums[x%len(nums)]
            
            stack.append(x%len(nums))
                 
        return ans