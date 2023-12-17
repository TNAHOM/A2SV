class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        status = 1

        for x in range(len(nums)-1):
            if nums[x] <= nums[x+1]:
                continue  

            if x == 0 or nums[x+1] >= nums[x-1]:
                nums[x] = nums[x+1]
            else:
                nums[x+1] = nums[x]
            status -= 1
            
            if status < 0:
                return False

        return True
