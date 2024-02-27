class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0: 
                return 1
            if x == 0:
                return 0
            temp = pow(x, n//2) 
            temp = temp*temp

            if n%2 == 1:
                return x*temp
            return temp

        output = pow(x, abs(n))
        if n < 0:
            return 1/output
        return output
