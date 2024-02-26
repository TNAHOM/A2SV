class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        def swapper(ind):
            if ind == N//2:
                return
            else:
                s[ind], s[N-ind-1] = s[N-ind-1], s[ind]
                swapper(ind+1)
        swapper(0)
                