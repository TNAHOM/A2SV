class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [num for num in range(1, n+1)]

        def helper(i, comb):
            if len(comb) == k:

                ans.append(comb[:])
                return
            if i >= n:
                return
            
            # print(comb, 'before app')
            comb.append(nums[i])
            helper(i+1, comb)
            comb.pop()

            helper(i+1, comb)
        
        
        helper(0, [])
        return ans
            