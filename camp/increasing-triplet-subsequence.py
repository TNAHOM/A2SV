class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 2**31
        j = 2**31

        for x in nums:
            if x <= i:
                i = x
            elif x <= j:
                j = x
            elif x > j and x > i:
                return True
        
        return False