class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        last = 0
        for x in nums:
            last+=x
            output.append(last)
        
        return output