class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def power(n):
            if n == 1:
                return True
            if n < 3:
                return
            # print(n)
            return power(n/3)
            
        
        
        return power(n)
        # return