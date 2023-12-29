class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sort_num = sorted(nums, reverse=True)
        set_ = set(sort_num)
        min_num = min(nums)
        track = {}

        for x in range(len(sort_num)):
            if sort_num[x] == min_num:
                track[min_num] = 0
            else:
                track[sort_num[x]] = track.get(sort_num[x], 0) + 1
        output = []
        out_sum = 0
        for x,y in track.items():
            output.append(out_sum)
            out_sum+=y
        
        return sum(output)

