class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        j = -1
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2:
                j = i
                break
        return num[:j+1]
        