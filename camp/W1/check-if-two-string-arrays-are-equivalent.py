class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        print(word1, word2, str(word1) == str(word2))
        
        return bool(str(word1) == str(word2))