class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = len(min(strs))
        ref = strs[0]
        output = ''

        for i in range(len(ref)):
            for s in strs:
                if i == len(s) or ref[i] != s[i]:
                    return output
            output += strs[0][i]

        
        return output