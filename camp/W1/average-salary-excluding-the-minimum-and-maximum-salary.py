class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()

        avg = sum(salary[1:-1])/len(salary[1:-1])
        return avg
