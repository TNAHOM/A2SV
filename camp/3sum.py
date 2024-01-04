class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        # l, r = 0, len(nums)-1
        # output = set()

        # while l < r and l < len(nums):
        #     m = l+1
        #     while m < r:
        #         if nums[l] + nums[r] + nums[m] == 0:
        #             output.add((nums[l], nums[m], nums[r]))
        #         m+=1
        #     if nums[l] + nums[r] + nums[m-1] <= 0:
        #         l+=1
        #     else:
        #         r-=1
        #     print(l, m, r, output)
        output = set()
        
        for l in range(len(nums)-2):
            m = l+1
            r = len(nums)-1
            while m < r:
                if nums[l] + nums[r] + nums[m] == 0:
                    output.add((nums[l], nums[m], nums[r]))
                    m+=1
                    r-=1
                elif nums[l] + nums[r] + nums[m] > 0:
                    r-=1
                else:
                    m+=1
        return output

    