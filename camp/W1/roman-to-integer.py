class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        

        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]

        roman_dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        if len(s) == 1:
            return roman_dic[s]

        temp = []

        for x in s:
            if x in roman_dic.keys():
                temp.append(roman_dic[x])
        
        print(temp)
        l = 0
        
        output = 0
        while l < len(temp)-1:
            r = l+1
            if temp[l] < temp[r]:
                output += temp[r] - temp[l]
                l+=2
            else:
                output+=temp[l]
                l+=1

        if len(s) >= 2 and temp[-1] <= temp[-2]:
            output+=temp[-1]

        return output
