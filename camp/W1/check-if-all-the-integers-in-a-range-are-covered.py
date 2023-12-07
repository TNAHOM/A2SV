class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        temp = set()

        for x in range(len(ranges)):
            temp.update(range(ranges[x][0], ranges[x][1]+1))
        
        
        return True if set(range(left, right+1)) <= temp else False
        