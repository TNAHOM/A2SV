class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0: return 0
        runsum, mp = 0, {0: -1}
        ans = float('inf')

        for i,num in enumerate(nums):
            runsum = (runsum + num) % p
            
            x = (runsum - rem) % p
            if x in mp:
                ans = min(ans,i - mp.get(x, 0))
            mp[runsum] = i
        
            
        return ans if ans < len(nums) else -1


        