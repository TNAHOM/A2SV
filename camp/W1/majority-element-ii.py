class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        output = []
        for x in nums:
            if x in dic.keys():
                dic[x]+=1
            else:
                dic[x] = 1
        
        for key, value in dic.items():
            if value > len(nums)//3:
                output.append(key)

        return output