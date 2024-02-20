class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        t = len(colSum)
        matrix = [[0 for x in range(t)] for x in range(n)]

        for r in range(n):
            for c in range(t):
                if rowSum[r] < colSum[c]:
                    matrix[r][c] = rowSum[r]
                    temp = rowSum[r]
                    rowSum[r] -= temp
                    colSum[c]-= temp
                    
                else:
                    matrix[r][c] = colSum[c]
                    temp = colSum[c]
                    colSum[c] -= temp
                    rowSum[r]-= temp
                # print(matrix[r][c], rowSum[r], colSum[c])
        # print(rowSum,)
        return matrix