class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 11110111101111111111
        exists = []
        l = 0
        output = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                exists.append(0)
            if len(exists) != 0:
                output = max(output, (r-l+1)-len(exists))
            else:
                output = max(output, (r-l))
            while len(exists) == 2:
                if nums[l] == 0:
                    exists.pop(-1)
                l+=1
        return output
            