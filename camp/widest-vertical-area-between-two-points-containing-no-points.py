class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        output = points[1][0] - points[0][0]
        for x in range(2, len(points)-1):
            output = max(output, (points[x+1][0] - points[x][0]))
        return output