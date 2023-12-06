class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        output = [0]*len(s)

        for letter in range(len(s)):
            output[indices[letter]] = s[letter]
        
        return ''.join(output)