class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((n//7)*28 + ((2*(n//7-1)+(n//7-1)*(n//7-2))/2)*7 + ((2*(n%7)+(n%7)*(n%7-1))/2)+ ((n//7)*(n%7)))

        