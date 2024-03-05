class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        path = []

        def helper(idx,path, tot):
            if tot == target:
                ans.add(tuple(path))
                return 
            if tot > target:
                return 
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    # print(i, idx, path, candidates[i])
                    continue
                
                tot+=candidates[i]
                path.append(candidates[i])
                helper(i+1,path, tot)
                path.pop()
                tot-=candidates[i]
        helper(0,path, 0)
        return ans