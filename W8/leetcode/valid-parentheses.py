class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', '}':'{', ']':'['}
        open = ['(', '{', '[']
        
        for x in s:
            if x in open:
                stack.append(x)

            else:
                temp = check[x]
                if stack and temp == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
                return False
        return True