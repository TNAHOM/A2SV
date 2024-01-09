class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        output = 0
        vowel = set(['a', 'e', 'i', 'o', 'u'])

        for x in s[:k]:
            if x in vowel:
                output+=1
                count+=1
        
        l, r = 0,k
        while r < len(s):
            if s[r] in vowel:
                count+=1
            if s[l] in vowel:
                count-=1
            output = max(output, count)
            
            l+=1
            r+=1
        return output
