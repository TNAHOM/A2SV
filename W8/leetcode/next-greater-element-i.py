class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        output = {}

        for x in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[x]:
                stack.pop()
            

            if not stack:
                output[nums2[x]] = -1
            else:
                output[nums2[x]] = stack[-1]
            stack.append(nums2[x])   
        ans = [] 
        for x in nums1:
            ans.append(output[x])

        return ans