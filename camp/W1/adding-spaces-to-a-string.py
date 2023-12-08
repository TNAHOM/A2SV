class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        s = list(s)

        new_s = [' ' for _ in range(len(spaces))]+s
        l, r = 0, len(spaces)
        curr = 0
        while r < len(new_s) and curr <len(spaces):
            if r-len(spaces) == spaces[curr]:
                l+=1
                curr+=1

            new_s[l], new_s[r] = new_s[r], new_s[l]
            l+=1
            r+=1
            
        return ''.join(new_s)
