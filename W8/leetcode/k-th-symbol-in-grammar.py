class Solution:
    def __init__(self):
        self.last = '0'
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n, k):
            if n == 1:
                if k == 1:
                    return 0
                else:
                    return 1
            
            if k%2 == 1:
                val = helper(n-1, (k+1)//2)
                if val == 1:
                    return 1
                else:
                    return 0
            else:
                val = helper(n-1, (k+1)//2)
                if val == 1:
                    return 0
                else:
                    return 1
        # print(helper(n, k))
        return helper(n, k)
