class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = (10**9) +7
        start, end = float('inf'), 0

        for x,y in requests:
            start = min(start, x)
            end = max(end, y)
        
        prefix = [0 for _ in range(end-start+2)]

        for x, y in requests:
            prefix[x-start]+=1
            prefix[y-start+1]-=1

        print(prefix)
        curr = 0
        nums.sort(reverse=True)
        for x in range((len(prefix))):
            curr += prefix[x]
            prefix[x] = curr

        prefix.sort(reverse=True)
        print(prefix)
        print(nums)
        output = 0
        for x in range(end-start+1):
            output+=(nums[x]*prefix[x])

        return output%mod
