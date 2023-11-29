class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        status = 0
        current = matrix[0][0]
        temp = 0

        for x in range(1,len(matrix)):
            for y in range(1, len(matrix[0])):
                if matrix[x][y] != matrix[x-1][y-1]:
                    return False
                
        return True
