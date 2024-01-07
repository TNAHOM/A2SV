class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = []
        output = 0
        l = 0
        r = 0

        while r<len(s) and l < len(s):
            if s[r] not in check:
                check.append(s[r])
                r+=1
                output = max(output, r-l)
            else:
                output = max(output, r-l)
                l+=1
                check.pop(0)
                  
        return output