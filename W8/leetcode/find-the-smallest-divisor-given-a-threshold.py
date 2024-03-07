class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low =   1
        high = max(nums)
        find = float('inf')

        while low<=high:
            mid = (low+high)//2
            tot = 0
            for x in nums: tot+=(ceil(x/mid))

            if tot <= threshold:
                # print(mid, tot)
                high = mid-1
                find = mid
            else:
                low = mid+1
        if find == float('inf'):
            return max(nums)
        
        return find