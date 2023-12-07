class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg = [x for x in nums if x<0]
        pos = [x for x in nums if x>0]

        output = []

        for x in range(len(neg)):
            output.append(pos[x])
            output.append(neg[x])
        return output

