class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        output = 0
        status = {}
        max_stat =  0

        for x in range(len(grid)):
            for y in range(len(grid[0])-2):
                key = ((y+1)+len(grid[0])*x)
                if key-2*len(grid[0]) not in status:
                    status[key] = grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x+1][y+1]
                else:
                    status[key - 2*len(grid[0])] += grid[x][y] + grid[x][y+1] + grid[x][y+2]
                    if x < len(grid)-2:
                        status[key] = grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x+1][y+1]

                    max_stat = max(max_stat, status[key - 2*len(grid[0])])
        
        return max_stat
        
            
