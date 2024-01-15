class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = 0
        dic = {}
        output = 0
        l = 0

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            if (r-l+1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l+=1
            output = max(output, r-l+1)
            
        return output