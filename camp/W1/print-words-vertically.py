class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.split()
        
        l = 0
        output = []

        while l < len(max(s, key=len)):
            temp = ''
            for x in s:
                if len(x) > l:
                    temp+=x[l]
                else:
                    temp+=' '
            
            output.append(temp.rstrip())
            l+=1
        
        return output