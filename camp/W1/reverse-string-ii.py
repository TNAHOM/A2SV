class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        s = list(s)
        jump = 0
        while l < len(s):
            r = (l+k) - 1
            if r >= len(s):
                r = len(s)-1
                while l<r:
                    s[l], s[r] = s[r], s[l]
                    l+=1
                    r-=1
                break
            else:
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l+=1
                    r-=1
                jump+=1
                l = jump*(2*k)

        return ''.join(s)