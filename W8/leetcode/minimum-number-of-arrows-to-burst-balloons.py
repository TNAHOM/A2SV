class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        a = points[0][0]
        b = points[0][1]

        count = 1
        for x in range(len(points)):
            print(x, len(points)-1)
            if points[x][0] > b:
                count+=1
                a = points[x][0]
                b = points[x][1]
                continue
            a = points[x][0]
            if points[x][1] < b:
                points[x][1] = b
        
        
        return count