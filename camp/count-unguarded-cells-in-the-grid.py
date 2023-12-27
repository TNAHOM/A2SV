class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = []
        for x in range(m):
            temp = []
            for y in range(n):
                temp.append(0)
            grid.append(temp)

        visited = set()
        set_wall = {(x, y) for x, y in walls}
        set_guard = {(x, y) for x, y in guards}

        for x, y in guards:
            down = x+1
            right = y+1
            left = y-1
            up = x-1

            while down < m:
                print((down, y) in set_wall)
                if (down, y) in set_wall or (down, y) in set_guard:
                    break
                visited.add((down, y))
                down+=1

            while up > -1:
                if (up, y) in set_wall or (up, y) in set_guard:
                    break
                visited.add((up, y))
                up-=1
            
            while right < n:
                if (x, right) in set_wall or  (x, right) in set_guard:
                    break
                visited.add((x, right))
                right+=1

            while left > -1:
                if  (x, left) in set_wall or  (x, left) in set_guard:
                    break
                visited.add((x, left))
                left-=1

        output = (m*n) - len(guards) - len(walls) - len(visited)
        return output
