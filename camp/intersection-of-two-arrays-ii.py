class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_1 = {}
        intersection_2 = {}
        output = []

        for x in nums1:
            intersection_1[x] = intersection_1.get(x, 0) + 1
        for x in nums2:
            intersection_2[x] = intersection_2.get(x, 0) + 1

        for key, value in intersection_1.items():
            if key in intersection_2:
                output.extend([key for _ in range(min(value, intersection_2[key]))])
        
        return output