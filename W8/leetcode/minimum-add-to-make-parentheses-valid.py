class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0

        for x in s:
            if x == '(':
                open+=1

            if x == ')' and open >= 1:
                open-=1
            elif open == 0 and x == ')':
                close+=1
        return open+close