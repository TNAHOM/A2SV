class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        greater = []
        mid = []

        for x in nums:
            if x > pivot:
                greater.append(x)
            elif x < pivot:
                less.append(x)
            elif x == pivot:
                mid.append(x)
        
        return less+mid+greater
            