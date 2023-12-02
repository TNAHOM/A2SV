class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)-1
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        output = ''
        while l >= 0:
            if s[l] == '#':
                take = int(s[l-2:l])
                print(take)
                output+=alpha[take-1]
                l-=3
            else:
                where = alpha[int(s[l])-1]
                output+=where
                l-=1
        
        return output[::-1]