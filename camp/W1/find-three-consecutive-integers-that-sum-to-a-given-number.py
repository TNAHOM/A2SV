class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        
        l=int((num/3) -1)

        while True:
            temp = l + (l+1) + (l+2)
            if temp == num:
                return [l, l+1, l+2]
            elif temp > num:
                return []
            l+=1