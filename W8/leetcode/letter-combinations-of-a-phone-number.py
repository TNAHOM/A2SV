class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        ans = []
        if not digits:
            return []
        def comb(ind, path):
            if ind == len(digits):
                ans.append(''.join(path[:]))
                return
            
            for y in range(len(dict[int(digits[ind])])):
                path.append(dict[int(digits[ind])][y])
                comb(ind+1, path)
                path.pop()
            return path
        

        comb(0, [])
        return ans