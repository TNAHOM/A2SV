class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        compare = Counter(p)
        size = len(p)
        output = []
        for x in range(len(s)-len(p)+1):
            compare2 = Counter(s[x:x+size])
            if compare == compare2:
                output.append(x)
        return output