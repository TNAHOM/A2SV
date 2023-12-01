class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_power = int(log(n, 3))
        
        current_sum = 3**max_power

        for x in range(max_power-1, -1, -1):
            if current_sum+3**x <= n:
                current_sum+=3**x

        return current_sum == n