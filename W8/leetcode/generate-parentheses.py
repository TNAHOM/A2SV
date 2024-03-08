class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(open, close, path=[]):
            if len(path) == n*2:
                ans.append(''.join(path))
                return


            if open < n:
                path.append('(')
                helper(open+1, close, path)
                path.pop()
            if close < open:
                path.append(')')
                helper(open, close+1, path)
                path.pop()

        helper(0, 0)
        # print(ans)
        return ans