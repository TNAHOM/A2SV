class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        fir = 0
        sec = 0

        output = 0
        while fir < len(g) and sec < len(s):
            if s[sec] >= g[fir]:
                output+=1
                sec+=1
                fir+=1
            elif s[sec] < g[fir]:
                sec+=1
            else:
                fir+=1
        return output