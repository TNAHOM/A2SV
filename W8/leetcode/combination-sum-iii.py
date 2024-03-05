class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        path = []

        def helper(idx,path, tot):
            if tot == n and len(path) == k:
                ans.add(tuple(path))
                return
            if tot > n and len(path) > k:
                return 

            for i in range(idx,10):
                tot+=i
                path.append(i)
                helper(i+1,path, tot)
                path.pop()
                tot-=i
                
        helper(1,path, 0)
        return ans