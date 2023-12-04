class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        output_1 = ''
        output_2 = ''

        for y in num1:
            for x in range(0, 10):
                if str(x) == y:
                    output_1+=y
                    break
        
        for y in num2:
            for x in range(0, 10):
                if str(x) == y:
                    output_2+=y
                    break
        print(output_1, output_2)
        return str(int(output_1)*int(output_2))