class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        l = 0
        output = 0
        while l< len(nums):
            r = l+1
            while r < len(nums):
                if nums[l] == nums[r] and (l*r)%k == 0:
                    output+=1
                r+=1
            l+=1
        return output


