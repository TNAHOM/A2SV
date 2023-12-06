class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        # 3-same-digit
        # if their are multiple same-3-digit numbers return the largest one
        # if none return ''
        output = ''
        left = 0
        
        while left < len(num)-1:
            right = left+1
            temp = ''

            while right < len(num) and num[left] == num[right] and right-left+1 <=3:
                temp = num[left:right+1]
                right+=1
            
            left+=1
            if len(temp) == 3:
                if output != '':
                    output = str(max(int(output), int(temp)))
                    if output[0] == '0':
                        output = '000'
                else:
                    output = temp

        return output

