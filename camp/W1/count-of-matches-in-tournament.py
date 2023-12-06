class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n >=2:
            if n % 2 == 0:
                n = n/2
                count+=n
            else:
                n = n//2+1
                count += n-1
        return count
