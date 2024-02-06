class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = Counter(nums)
        sz_dic = len(dic)
        output = 0


        for l in range(len(nums)):
            r = l
            passed = defaultdict(int)
            size = 0

            while r < len(nums):
                if passed[nums[r]] == 0:
                    size+=1
                passed[nums[r]]+=1

                if size == sz_dic:
                    output+=1
                r+=1

            # print(passed)
            # passed[nums[l]]-=1
            # if passed[nums[l]] == 0:
                # size-=1
        return output
        