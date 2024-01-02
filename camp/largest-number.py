class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for x in range(len(nums)-1):
            for y in range(len(nums)-1):
                first = str(nums[y])
                second = str(nums[y+1])
                if first[0] < second[0]:
                    nums[y], nums[y+1] = nums[y+1], nums[y]

                elif first[0] == second[0]:
                    opt_1 = nums[y] * 10**len(second) + nums[y+1]
                    opt_2 = nums[y+1] * 10**len(first) + nums[y]

                    if opt_1 < opt_2:
                        nums[y] , nums[y+1] = nums[y+1], nums[y]
        output = ''
        for x in nums:
            output+=str(x)

        return str(int(output))