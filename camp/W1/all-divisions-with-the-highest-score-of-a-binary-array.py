class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        check = {}
        add = sum(nums)
        stat = 0

        stat = 0
        l = 0
        while l <= len(nums):
            if l!= 0 and nums[l-1] == 1:
                add-=1
                stat+=1
                check[l] = (l-stat) + add

            else:
                check[l] = (l-stat) + add
            l+=1
        get_max = max(check.values())

        return [key for key, val in check.items() if val == get_max]
