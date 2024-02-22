class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for x in s:
            if x != '*':
                stack.append(x)
            elif stack:
                stack.pop()
                
        return ''.join(stack)
