class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        output = float('inf')

        for x in range(len(ghosts)):
            diff_x = abs(ghosts[x][0] - target[0])
            diff_y = abs(ghosts[x][1] - target[1])

            output = min(output, (diff_x + diff_y))
        
        return bool(output > abs(target[0]) + abs(target[1]))