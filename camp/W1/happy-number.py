class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 9 and n!= 7:
            return False

        n = str(n)
        print(n, n[0])
        add = 0
        for x in n:
            add+=int(x)**2

        return self.isHappy(add)