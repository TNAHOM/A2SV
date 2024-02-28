
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 1 0
        # 0 1 1 0
        if rowIndex == 0:
            return [1]
        def helper(n):
            if n == 1:
                return [1,1]
            prev = [0] + helper(n-1) + [0]
            # print(prev)
            
            next = []
            for x in range(1, len(prev)):
                temp = prev[x-1] + prev[x]
                next.append(temp)
            prev = next
            return prev
        return helper(rowIndex)
        