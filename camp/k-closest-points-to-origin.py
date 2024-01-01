class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        check = []
        for x in range(len(points)):
            val = points[x][0]**2 + points[x][1]**2
            check.append((val, tuple(points[x])))

        new_sort = sorted(check)
        output = []
        for x in range(k):
            output.append(list(new_sort[x][1]))

        
        return output