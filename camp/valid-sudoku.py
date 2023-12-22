class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for x in range(len(board[0])):
            dir_x = set()
            for y in range(len(board)):
                if board[y][x] != '.':
                    if board[y][x] in dir_x:
                        return False
                    dir_x.add(board[y][x])
        
        for x in range(len(board)):
            dir_y = set()
            for y in range(len(board[0])):
                if board[x][y] != '.':
                    if board[x][y] in dir_y:
                        return False
                    dir_y.add(board[x][y])
        
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                start = [x, y] 

                set_check = set()
                for r in range(start[0], start[0]+3):
                    for c in range(start[1], start[1]+3):
                        if board[r][c] != '.':
                            if board[r][c] in set_check:
                                return False
                            set_check.add(board[r][c])

        return True