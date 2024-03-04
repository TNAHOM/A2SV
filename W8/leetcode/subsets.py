class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(ind, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            ans.append(path[:])

            for i in range(ind, len(nums)):
                path.append(nums[i])
                # print(path)
                helper(i+1, path)
                path.pop()

        helper(0,[])

        return ans