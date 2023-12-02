class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        l = 0
        output = ''
        while l<len(command):
            if command[l] == 'G':
                output+=('G')
                l+=1
            elif command[l] == '(' and command[l+1] == ')':
                output+=('o')
                l+=2
            elif command[l] == '(' and command[l+1] == 'a':
                output+=('al')
                l+=4
        return output