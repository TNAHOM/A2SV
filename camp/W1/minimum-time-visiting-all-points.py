class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        output = 0

        for x in range(len(points)-1):
            diff_x = abs(points[x][0] - points[x+1][0])
            diff_y = abs(points[x][1] - points[x+1][1])
            output+=min(diff_x, diff_y)
            output+=max(diff_x, diff_y)-min(diff_x, diff_y)
        
        return output