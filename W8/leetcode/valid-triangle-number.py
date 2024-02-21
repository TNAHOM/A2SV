class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l = 0
        output = 0

        while l < len(nums):
            m = l+1
            r = len(nums)-1
            while m < r:
                if nums[m] + nums[r] > nums[l]:
                    output+=r-m
                    m+=1
                else:
                    r-=1
                
            l+=1
            

        return output