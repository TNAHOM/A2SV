class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        output = 0
        n = len(grid)
        row = []
        col = []

        for x in range(n):
            row.append(max(grid[x]))
        for x in range(n):
            temp = 0
            for y in range(n):
                temp = max(grid[y][x], temp)
            col.append(temp)

        for r in range(n):
            for c in range(n):
                temp = min(row[r], col[c]) - grid[r][c]
                output+=temp

        return output