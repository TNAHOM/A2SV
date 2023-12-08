class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        output = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and list1[i] not in output:
                    output[list1[i]] = i+j
        

        return [k for k, v in output.items() if v == min(output.values())]