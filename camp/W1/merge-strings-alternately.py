class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ''

        size = min(len(word1), len(word2))

        for x in range(size):
            output += word1[x]
            output += word2[x]
        
        if len(word1) > len(word2):
            return output+word1[size:]
        elif len(word1) < len(word2):
            return output + word2[size:]
        else:
            return output