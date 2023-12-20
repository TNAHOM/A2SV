class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = ''
        for x in digits:
            num = num + str(x)
        
        num = int(num) + 1

        num_list = []

        for x in str(num):
            num_list.append(int(x))

        print(num_list)
        return num_list