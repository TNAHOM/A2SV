class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        fir = 0
        sec = 0
        common =10**10

        while fir < len(nums1) and sec < len(nums2):
            if nums1[fir] == nums2[sec]:
                return nums1[fir]
            if nums1[fir] < nums2[sec]:
                fir+=1
            else:
                sec+=1
        return -1