class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0

        for x in range(len(mat)):
            output+=mat[x][x]

        for y in range(len(mat)-1, -1, -1):
            output+=mat[len(mat)-1-y][y]

        if len(mat) % 2 == 0:
            return output
        else:
            size = len(mat) // 2
            return output - mat[size][size]
