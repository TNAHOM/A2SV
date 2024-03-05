class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def inbound(n_i, n_j, n, m):
            return 0<= n_i < n and 0 <= n_j < m

        def find(x, y, idx):
            # print(idx, )
            if idx == len(word):
                return True
            
            for i, j in directions:
                n_i = i+x
                n_j = j+y
                
                if inbound(n_i, n_j, len(board), len(board[0])) and  board[n_i][n_j] == word[idx] and (n_i, n_j) not in visited:
                    visited.add((n_i, n_j))
                    # print(visited)
                    val = find(n_i, n_j, idx+1)
                    visited.remove((n_i, n_j))
                    if val: return True

        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if word[0] == board[x][y]:
                    visited.add((x,y))
                    ans = find(x, y, 1)
                    visited.remove((x,y))
                    
                    if ans:
                        return True

        return