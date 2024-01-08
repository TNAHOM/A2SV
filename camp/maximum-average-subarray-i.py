class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        output = 0
        l = 0
        r = k
        add = sum(nums[l:r])
        output = add/k

        while r < len(nums):
            add -= nums[l]
            add+=nums[r]
            avg = add/k
            output = max(output, avg)
            l+=1
            r+=1
        return output